# $Id: driver.py 6de8ee4e7d2d 2010-03-29 mtnyogi $
# coding=utf-8
# 
# Copyright © 2007-2008 Bruce Frederiksen
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

'''
    This example shows how people are related.  The primary data (facts) that
    are used to figure everything out are in family.kfb.

    There are four independent rule bases that all do the same thing.  The
    fc_example rule base only uses forward-chaining rules.  The bc_example
    rule base only uses backward-chaining rules.  The bc2_example rule base
    also only uses backward-chaining rules, but with a few optimizations that
    make it run 100 times faster than bc_example.  And the example rule base
    uses all three (though it's a poor use of plans).

    Once the pyke engine is created, all the rule bases loaded and all the
    primary data established as universal facts; there are five functions
    that can be used to run each of the three rule bases: fc_test, bc_test,
    bc2_test, test and general.
'''


import contextlib
import sys
import time
from typing import Tuple
from markupsafe import string

from pyke import knowledge_engine, krb_traceback, goal

# Chunks and Relationships
from chunks import *

from web import Wiki

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

fc_goal = goal.compile('system.has_related($name, $alias, $relationship)')

def fc_test(person1 = 'bruce'):
    '''
        This function runs the forward-chaining example (fc_example.krb).
    '''
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('fc_example')  # Runs all applicable forward-chaining rules.
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    with fc_goal.prove(engine, person1=person1) as gen:
        for vars, plan in gen:
            print("%s, %s are %s" % \
                    (person1, vars['person2'], vars['relationship']))
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("fc time %.2f, %.0f asserts/sec" % \
          (fc_time, engine.get_kb('family').get_stats()[2] / fc_time))

# BEGIN ********************************************** Searching types *******************************
def is_category(category):
    with engine.prove_goal(
               'bc_system.has_recurrent_alias($old_category,$category, $alias, $relationship)',
               old_category=category) \
        as gen:
            if gen:
                for vars, plan in gen:
                    # print("%s, %s are %s" % \
                    #     (category, vars['alias'], vars['relationship']))
                    return True, vars["category"]
    return False, category

def is_relationship(relationship):
    with engine.prove_goal(
               'bc_system.has_recurrent_rel($category1, $category2, $old_relationship, $relationship)',
               old_relationship=relationship) \
        as gen:
            if gen:
                for vars, plan in gen:
                    # print("%s, %s are %s" % \
                    #     (vars['category'], vars['alias'], relationship))
                    return True, vars["relationship"]
    return False, relationship

def is_term(name):
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc_system')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    with engine.prove_goal(
               'bc_system.has_recurrent_term($name, $term)',
               name=name) \
        as gen:
            if gen:
                for vars, plan in gen:
                    # print("%s, %s are %s" % \
                    #     (vars['name'], vars['term']))
                    return True, vars["term"]
    return False, name

def search_type(chunk, terms_found=None) -> str:
    is_cat, cat = is_category(chunk)
    if is_cat:
        return "cat", cat
    is_rel, rel = is_relationship(chunk)
    if is_rel:
        return "rel", rel
    else:
        term_prop = is_term(chunk)
        if not terms_found == None:
            terms_found[term_prop[1]] = term_prop[0]
        return "term", term_prop[1]

# END ********************************************** Searching types *******************************

# BEGIN ********************************************** Searching types *******************************
def search_for_cat_cat_rel(category1=None, category2=None, relationship=None): # Returns
    result = []
    if category1:
        if category2:
            with engine.prove_goal(
                'bc_system.has_related($category1, $category2, $relationship)',
                category1=category1, category2=category2) \
            as gen:
                if gen:
                    for vars, plan in gen:
                        # print("%s, %s are %s" % \
                        #     (vars['category1'], vars['category2'], vars["relationship"]))
                        result.append(Relationship((vars['category2'], vars["relationship"], vars["category1"])))

            with engine.prove_goal(
                    'bc_system.has_related($category1, $category2, $relationship)',
                    category1=category2, category2=category1) \
                as gen:
                    if gen:
                        for vars, plan in gen:
                            # print("%s, %s are %s" % \
                            #     (vars['category1'], vars['category2'], vars["relationship"]))
                            result.append(Relationship((vars['category1'], vars["relationship"], vars["category2"])))
        else:
            with engine.prove_goal(
                    'bc_system.has_related($category1, $category2, $relationship)',
                    category1=category1) \
                as gen:
                    if gen:
                        for vars, plan in gen:
                            # print("%s, %s are %s" % \
                            #     (vars['category1'], vars['category2'], vars["relationship"]))
                            result.append(Relationship((vars['category2'], vars["relationship"], vars["category1"])))

            with engine.prove_goal(
                    'bc_system.has_related($category1, $category2, $relationship)',
                    category2=category1) \
                as gen:
                    if gen:
                        for vars, plan in gen:
                            # print("%s, %s are %s" % \
                            #     (vars['category1'], vars['category2'], vars["relationship"]))
                            result.append(Relationship((vars['category1'], vars["relationship"], vars["category2"])))
    if relationship:
        with engine.prove_goal(
                'bc_system.has_related($category1, $category2, $relationship)',
                relationship=relationship) \
            as gen:
                if gen:
                    for vars, plan in gen:
                        # print("%s, %s are %s" % \
                        #     (vars['category1'], vars['category2'], vars["relationship"]))
                        # result.append((vars['category2'], vars["relationship"]))
                        result.append(Relationship((vars['category1'], vars["relationship"], vars["category2"])))

        # with engine.prove_goal(
        #         'bc_system.has_related($category1, $category2, $relationship)',
        #         relationship=relationship) \
        #     as gen:
        #         if gen:
        #             for vars, plan in gen:
        #                 print("%s, %s are %s" % \
        #                     (vars['category1'], vars['category2'], vars["relationship"]))
        #                 result.append((vars['category1'], vars["category2"]))
    return result

def belongs_to_category(chunk):
    result = []
    belongs = None
    with engine.prove_goal(
            'bc_system.has_category($name, $category, $relationship)',
            name=chunk) \
        as gen:
            if gen:
                for vars, plan in gen:
                    # print("%s, %s are %s" % \
                    #     (vars['name'], vars['category'], vars["relationship"]))
                    # result.append((vars['category'], vars["relationship"]))
                    result.append(Relationship((vars["name"], vars["category"], vars["relationship"])))
                    belongs = vars['category']
    return result, belongs

def tumor_has_symptom(symptom:str)->list:
    """Dado un sintoma, deuelve el tumor(organo) al cual pertenece\nsymptom:str->nombre del sintoma cambiando espacios por _. Devuelve una lista con los tumores(lista de strings)."""
    tumors = []
    

    _, symptom = search_type(symptom)

    # belongs = None
    with engine.prove_goal(
            'bc_system.has_symptom($tumor, $symptom, $relationship)',
            symptom=symptom) \
        as gen:
            if gen:
                for vars, plan in gen:
                    # print("%s, %s are %s" % \
                    #     (vars['name'], vars['category'], vars["relationship"]))
                    # result.append((vars['category'], vars["relationship"]))
                    tumors.append(vars["tumor"])
                    # belongs = vars['category']
    return tumors

def tumors_has_many_symptoms(symptoms:list)-> dict:
    """Dada una lista de sintomas devuelve un diccionario con llaves=tumor, valor=sintomas(lista de strings)"""
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc_system')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time
    
    tumors_dict = {}
    
    for symptom in symptoms:
        for tumor in tumor_has_symptom(symptom):
            if tumors_dict.__contains__(tumor):
                tumors_dict[tumor].append(symptom)
            else:
                tumors_dict[tumor] = [symptom]

    return tumors_dict
    

def check_relationship(chunk, chunk_type, left_chunk=None, left_chunk_type=None, left_chunk_rel=None): # La idea en este punto es buscar como se relaciona el chunk actual con el anterior, si es el 1er chunk entonces solamente habra que buscar en donde aparece relacionado con alguien
    relationships = []
    if left_chunk:
        if chunk_type == "cat":
            if left_chunk_type == "cat":

                relationships = search_for_cat_cat_rel(category1=chunk, category2=left_chunk)
                # print(relationships)
            # elif left_chunk_type == ""
        elif chunk_type == "rel":
            relationships = search_for_cat_cat_rel(relationship=chunk)
            # print(relationships)
        else:
            # Look if this chunk belogs to any category
            relationships = belongs_to_category(chunk)[0]
    else:
        if chunk_type == "cat":
            relationships = search_for_cat_cat_rel(category1=chunk)
            # print(relationships)
        elif chunk_type == "rel":
            relationships = search_for_cat_cat_rel(relationship=chunk)
            # print(relationships)
        else:
            # Look if this chunk belogs to any category
            relationships = belongs_to_category(chunk)[0]

    return relationships

# Busca todos los elementos que pertenecen a la categoria chunk
def search_instance_category(chunk):
    result = []
    with engine.prove_goal(
            'bc_system.has_category($name, $category, $relationship)',
            category=chunk) \
        as gen:
            if gen:
                for vars, plan in gen:
                    # print("%s, %s are %s" % \
                    #     (vars['name'], vars['category'], vars["relationship"]))
                    # result.append((vars['category'], vars["relationship"]))
                    result.append(Relationship((vars["name"], vars["category"], vars["relationship"])))
    return result

# def search_instance_term(chunk):

# END ********************************************** Searching types *******************************

# BEGIN ********************************************** Chunk's types *******************************
def create_basic_chunk_type(chunk, chunk_type, terms_found)-> Chunk:
    if chunk_type == "cat":
        relationships = search_instance_category(chunk)
        return CatChunk(chunk,cat_instances=relationships)
    elif chunk_type == "term":
        # Look if this chunk belogs to any category
        relationships = belongs_to_category(chunk)[0]
        # found:bool = relationships == None
        found = terms_found[chunk]
        return TermChunk(chunk,term_instances=relationships, found=found)
    elif chunk_type == "rel":
        relationships = search_for_cat_cat_rel(relationship=chunk)
        return RelChunk(chunk, rel_instances=relationships)
# END ********************************************** Chunk's Types *******************************

cat_cat_method = {("tumor", "organ"):"",
                  ("organ", "tumor"):""}


# def create_relationship(ca)

def make_relationships(rel_chunk:Chunk, left_chunk=None, right_chunk=None)-> RelCatTermChunk:
    result = []
    
    if left_chunk:
        if right_chunk:
            if left_chunk.chunk_type == "cat":
                if right_chunk.chunk_type == "cat_term":
                    with engine.prove_goal(
                        'bc_system.has_cat_cat_rel($category1, $category2, $instance1, $instance2, $relationship)', # 'bc_system.has_cat_term_rel($cat_term, $cat, $symptom, $tumor, $relationship)', # cat_term=right_chunk.terms_cat, cat=left_chunk.chunk, tumor=right_chunk.term) \ Esta que esta comentada funciono!!!
                            category1=right_chunk.terms_cat, category2=left_chunk.chunk, instance1=right_chunk.term) \
                        as gen:
                            if gen:
                                for vars, plan in gen:
                                    # print("%s, %s are %s" % \
                                    #     (vars['name'], vars['category'], vars["relationship"]))
                                    # result.append((vars['category'], vars["relationship"]))
                                    tags = (right_chunk.terms_cat, left_chunk.chunk, right_chunk.term, "$instance2", rel_chunk.chunk)
                                    result.append(Relationship((vars["category1"], vars["category2"], vars["instance1"], vars["instance2"], vars["relationship"]), tags=tags))
                elif right_chunk.chunk_type == "cat":
                    with engine.prove_goal(
                        'bc_system.has_cat_cat_rel($category1, $category2, $instance1, $instance2, $relationship)', # 'bc_system.has_cat_term_rel($cat_term, $cat, $symptom, $tumor, $relationship)', # cat_term=right_chunk.terms_cat, cat=left_chunk.chunk, tumor=right_chunk.term) \ Esta que esta comentada funciono!!!
                            category1=right_chunk.chunk, category2=left_chunk.chunk) \
                        as gen:
                            if gen:
                                for vars, plan in gen:
                                    # print("%s, %s are %s" % \
                                    #     (vars['name'], vars['category'], vars["relationship"]))
                                    # result.append((vars['category'], vars["relationship"]))
                                    tags = (right_chunk.chunk, left_chunk.chunk, "$instance1" "$instance2", "$relationship")
                                    result.append(Relationship((vars["category1"], vars["category2"], vars["instance1"], vars["instance2"], vars["relationship"]), tags=tags))
            elif left_chunk.chunk_type == "cat_term":
                if right_chunk.chunk_type == "cat":
                    with engine.prove_goal(
                        'bc_system.has_cat_cat_rel($category1, $category2, $instance1, $instance2, $relationship)', # 'bc_system.has_cat_term_rel($cat_term, $cat, $symptom, $tumor, $relationship)', # cat_term=right_chunk.terms_cat, cat=left_chunk.chunk, tumor=right_chunk.term) \ Esta que esta comentada funciono!!!
                            category1=left_chunk.terms_cat, category2=right_chunk.chunk, instance1=left_chunk.term) \
                        as gen:
                            if gen:
                                for vars, plan in gen:
                                    # print("%s, %s are %s" % \
                                    #     (vars['name'], vars['category'], vars["relationship"]))
                                    # result.append((vars['category'], vars["relationship"]))
                                    tags = (left_chunk.terms_cat, right_chunk.chunk, left_chunk.term, "$instance2", "$relationship")
                                    result.append(Relationship((vars["category1"], vars["category2"], vars["instance1"], vars["instance2"], vars["relationship"]), tags=tags))
                elif right_chunk.chunk_type == "cat_term":
                    with engine.prove_goal(
                        'bc_system.has_cat_cat_rel($category1, $category2, $instance1, $instance2, $relationship)', # 'bc_system.has_cat_term_rel($cat_term, $cat, $symptom, $tumor, $relationship)', # cat_term=right_chunk.terms_cat, cat=left_chunk.chunk, tumor=right_chunk.term) \ Esta que esta comentada funciono!!!
                            category1=left_chunk.terms_cat, category2=right_chunk.terms_cat, instance1=left_chunk.term, instance2=right_chunk.term) \
                        as gen:
                            if gen:
                                for vars, plan in gen:
                                    # print("%s, %s are %s" % \
                                    #     (vars['name'], vars['category'], vars["relationship"]))
                                    # result.append((vars['category'], vars["relationship"]))
                                    tags = (left_chunk.terms_cat, right_chunk.terms_cat, left_chunk.term, right_chunk.term, "$relationship")
                                    result.append(Relationship((vars["category1"], vars["category2"], vars["instance1"], vars["instance2"], vars["relationship"]), tags=tags))
        else:
            if left_chunk.chunk_type == "cat_term":
                with engine.prove_goal(
                        'bc_system.has_cat_cat_rel($category1, $category2, $instance1, $instance2, $relationship)', # 'bc_system.has_cat_term_rel($cat_term, $cat, $symptom, $tumor, $relationship)', # cat_term=right_chunk.terms_cat, cat=left_chunk.chunk, tumor=right_chunk.term) \ Esta que esta comentada funciono!!!
                            category1=left_chunk.terms_cat, category2=left_chunk.chunk, instance1=left_chunk.term, relationship=rel_chunk.chunk) \
                        as gen:
                            if gen:
                                for vars, plan in gen:
                                    # print("%s, %s are %s" % \
                                    #     (vars['name'], vars['category'], vars["relationship"]))
                                    # result.append((vars['category'], vars["relationship"]))
                                    tags = (left_chunk.terms_cat, left_chunk.chunk, left_chunk.term, "$instance2", rel_chunk.chunk)
                                    result.append(Relationship((vars["category1"], vars["category2"], vars["instance1"], vars["instance2"], vars["relationship"]), tags=tags))
            else:
                result = left_chunk.relationships
        return RelCatTermChunk(relationships=result)
    # return result
            # has_sympton_organ_term()
    if right_chunk:
        if right_chunk.chunk_type == "cat_term":
                with engine.prove_goal(
                        'bc_system.has_cat_cat_rel($category1, $category2, $instance1, $instance2, $relationship)', # 'bc_system.has_cat_term_rel($cat_term, $cat, $symptom, $tumor, $relationship)', # cat_term=right_chunk.terms_cat, cat=left_chunk.chunk, tumor=right_chunk.term) \ Esta que esta comentada funciono!!!
                            category1=right_chunk.terms_cat, category2=right_chunk.chunk, instance1=right_chunk.term, relationship=right_chunk.chunk) \
                        as gen:
                            if gen:
                                for vars, plan in gen:
                                    # print("%s, %s are %s" % \
                                    #     (vars['name'], vars['category'], vars["relationship"]))
                                    # result.append((vars['category'], vars["relationship"]))
                                    tags = (right_chunk.terms_cat, right_chunk.chunk, right_chunk.term, "$instance2", right_chunk.chunk)
                                    result.append(Relationship((vars["category1"], vars["category2"], vars["instance1"], vars["instance2"], vars["relationship"]), tags=tags))
        else:
            result = left_chunk.relationships
    return RelCatTermChunk(relationships=result)

def make_cat_relationship(chunk: CatChunk, right_chunk: CatChunk):
    result = []
    related = False
    with engine.prove_goal(
    'bc_system.has_cat_cat_rel($category1, $category2, $instance1, $instance2, $relationship)', # 'bc_system.has_cat_term_rel($cat_term, $cat, $symptom, $tumor, $relationship)', # cat_term=right_chunk.terms_cat, cat=left_chunk.chunk, tumor=right_chunk.term) \ Esta que esta comentada funciono!!!
        category1=chunk.chunk, category2=right_chunk.chunk) \
    as gen:
        if gen:
            for vars, plan in gen:
                related = True
                # print("%s, %s are %s" % \
                #     (vars['name'], vars['category'], vars["relationship"]))
                # result.append((vars['category'], vars["relationship"]))
                result.append(Relationship((vars["category1"], vars["category2"], vars["instance1"], vars["instance2"], vars["relationship"])))
    
    return CatCatChunk(chunk, right_chunk, result if related else chunk.relationships + right_chunk.relationships)

def make_cat_cat_term_relationship(cat_chunk: CatChunk, cat_term_chunk: CatTermChunk):
    result = []
    with engine.prove_goal(
                        'bc_system.has_cat_cat_rel($category1, $category2, $instance1, $instance2, $relationship)', # 'bc_system.has_cat_term_rel($cat_term, $cat, $symptom, $tumor, $relationship)', # cat_term=right_chunk.terms_cat, cat=left_chunk.chunk, tumor=right_chunk.term) \ Esta que esta comentada funciono!!!
                            category1=cat_term_chunk.terms_cat, category2=cat_chunk.chunk, instance1=cat_term_chunk.term) \
                        as gen:
                            if gen:
                                for vars, plan in gen:
                                    # print("%s, %s are %s" % \
                                    #     (vars['name'], vars['category'], vars["relationship"]))
                                    # result.append((vars['category'], vars["relationship"]))
                                    tags = (cat_term_chunk.terms_cat, cat_chunk.chunk, cat_term_chunk.term, "$instance2", "$relationship")
                                    result.append(Relationship((vars["category1"], vars["category2"], vars["instance1"], vars["instance2"], vars["relationship"]), tags=tags))

    # result = left_chunk.relationships
    return RelCatTermChunk(relationships=result)

def find_chunk_types(chunks, terms_found={}):
    """Busco si cada chunk de mi oracion es una Categoria, Relacion o Termino"""
    # terms_found = {}
    chunk_types = [search_type(chunk, terms_found) for chunk in chunks] 
    chunks = [chunk for (_,chunk) in chunk_types]
    chunk_types = [chunk_type for (chunk_type,_) in chunk_types]

    return chunk_types, chunks

def create_chunks(chunk_types, chunks, terms_found):
    """Creo las instancias de tipo Cat-Term, Cat, Term y Rel"""
    relationships = [] # Se ubicaran todos los chunks transformados a instancias de tipo Chunk
    index = 0
    while index < len(chunks):
        if index < len(chunks) - 1:
            left_chunk = chunks[index]
            left_chunk_type = chunk_types[index]

            right_chunk = chunks[index+1]
            right_chunk_type = chunk_types[index+1]

            cat_chunk = left_chunk if left_chunk_type == "cat" else right_chunk
            term_chunk = left_chunk if left_chunk_type == "term" else right_chunk

            if ( left_chunk_type == "cat" and right_chunk_type == "term") or (left_chunk_type == "term" and right_chunk_type == "cat"): # Si tengo la combinacion Cat-Term o Term-Cat:
                
                term_instances, terms_cat = belongs_to_category(term_chunk)
                
                # relationship = []
                # relationship = search_for_cat_cat_rel(terms_cat, cat_chunk)
                # if terms_cat == cat_chunk:
                #     relationship = term_instances

                relationships.append(CatTermChunk(left_chunk, right_chunk,  left_chunk_type, right_chunk_type,
                cat_chunk,
                term_chunk,
                search_instance_category(cat_chunk), # Hechos de la categoria
                None,
                term_instances,    # Hechos del termino
                terms_cat,
                search_for_cat_cat_rel(terms_cat, cat_chunk)
                ))
                index += 2
            else:
                relationships.append(create_basic_chunk_type(chunks[index], chunk_types[index], terms_found))
                index += 1
        elif index == len(chunks) - 1:
            relationships.append(create_basic_chunk_type(chunks[index], chunk_types[index], terms_found))
            index += 1

    return relationships

def get_answer(query, chunks=[]):
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc_system')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    max_unknown_terms = 5

    print("doing proof")
    try:
        terms_found = {}
        # For a traves de todos los chunks buscando su tipo: Los tipos son Categoria, Relacion, Termino
        chunk_types, chunks = find_chunk_types(chunks, terms_found)

        #Luego de hallar los tipos itero por cada uno y creo las instancias de tipo Cat-Term, Cat, Term y Rel, uniendo estos(Cat-Term) para luego pasar a analizar los de tipo relations
        relationships = create_chunks(chunk_types, chunks, terms_found)

        # Luego de tener todos en una lista de las formas Cat, Cat-Term, Rel, pasamos a buscar las relaciones que se puedan crear con Cat-Term Rel Cat-Term o Cat Rel Cat y luego con Cat-Cat. 
        # En caso de quedar Term solos, se veran en codigo estos casos en otro momento
        # TODO: Analizar casos en los que queden Term

        result = [] # Creo una nueva lista para ir agregando los resultados que saldran de relacionar loas Cat-Term que esten a la izquierda del Rel con los Cat-Term que esten a su derecha

        index =  0
        types = ["cat_term", "cat"]
        while index < len(relationships):
            if relationships[index].chunk_type == "rel":
                if index == 0:
                    if relationships[index+1].chunk_type in types: # index+1 < len(relationships)
                        relationship = make_relationships(relationships[index], left_chunk=None, right_chunk=relationships[index+1])
                        index += 2
                    index += 1
                elif index == len(relationships) -1:
                    relationship = make_relationships(relationships[index])
                else:
                    left_chunk = relationships[index-1]
                    right_chunk = relationships[index+1]

                    
                    if not left_chunk.chunk_type in types:
                        left_chunk = None
                    if not right_chunk.chunk_type in types:
                        right_chunk = None
                    relationship = make_relationships(relationships[index], left_chunk, right_chunk)
                    result.append(relationship)
                    index += 2
            else:
                if index < len(relationships) -1 and relationships[index+1].chunk_type !=  "rel" or (index == len(relationships) - 1):
                    result.append(relationships[index])
                index += 1

        # Hallando relaciones del tipo Cat-Term Rel Cat-Term o Cat Rel Cat
        relationships = result
        result = [] # Creo una nueva lista para ir agregando los resultados que saldran de relacionar los Cat-Cat

        index =  0
        types = ["cat_term", "cat"]
        while index < len(relationships):
            if relationships[index].chunk_type in types:#== "cat":
                if index < len(relationships)-1 and relationships[index+1].chunk_type in types:
                    cat_term = relationships[index] if relationships[index].chunk_type == "cat_term" else relationships[index+1]
                    if cat_term.chunk_type != "cat_term":
                        cat_term = None
                        relationship = make_cat_relationship(relationships[index], relationships[index+1])
                        result.append(relationship)
                    else:
                        cat_chunk = relationships[index] if cat_term == relationships[index] else relationships[index+1]
                        relationship = make_cat_cat_term_relationship(cat_chunk, cat_term)
                        result.append(relationship)
                    index += 2
                else:
                    result.append(relationships[index])
                    index += 1
            else:
                result.append(relationships[index])
                index += 1

        unknown_terms = []

        output = "" # Respuesta de la consulta hecha por el usuario

        print(result)

        # Luego de hallar las relaciones existentes entre cada chunk y su anterior, se supone que obtengamos las relaciones que existen entre todos los chunks en general 
        for chunk in result:
            if chunk.chunk_type == "term":
                if not chunk.found:
                    unknown_terms.append(chunk.chunk)
                    # Buscar definicion en wikipedia
                    continue
            if chunk.relationships:
                output += str(chunk)

        if len(unknown_terms) > max_unknown_terms:
            #return Wiki.search_on_wiki(query) # Si la cantidad de terminos que se desconocen es mayor que la cant de terminos aceptados, pues se busca en wikipedia
            pass
            # for relationship in chunk.relationships:
            #     if relationship:
            #         print(relationship) # Aqui se supone que haya que printear cosas diferentes en dependencia del tipo de Chunk que sea
        # print(output)
        
        # if output == "":
            # try:
            #     return Wiki.search_on_wiki(query)
            # except Exception as e:
            #     print(e)
            #     return "We did not find anything. Sorry :("
        return output
    except Exception as e:
        print(e)
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("bc time %.2f, %.0f goals/sec" % \
          (prove_time, engine.get_kb('bc_system').num_prove_calls / prove_time))

def bc2_test(person1 = 'bruce'):
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc2_example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    try:
        with engine.prove_goal(
               'bc2_example.how_related($person1, $person2, $relationship)',
               person1=person1) \
          as gen:
            for vars, plan in gen:
                print("%s, %s are %s" % \
                        (person1, vars['person2'], vars['relationship']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("bc time %.2f, %.0f goals/sec" % \
          (prove_time,
           engine.get_kb('bc2_example').num_prove_calls / prove_time))

def test(person1 = 'bruce'):
    engine.reset()      # Allows us to run tests multiple times.

    # Also runs all applicable forward-chaining rules.
    start_time = time.time()
    engine.activate('example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    try:
        # In this case, the relationship is returned when you run the plan.
        with engine.prove_goal(
               'example.how_related($person1, $person2)',
               person1=person1) \
          as gen:
            for vars, plan in gen:
                print("%s, %s are %s" % (person1, vars['person2'], plan()))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("fc time %.2f, %.0f asserts/sec" % \
          (fc_time, engine.get_kb('family').get_stats()[2] / fc_time))
    print("bc time %.2f, %.0f goals/sec" % \
          (prove_time, engine.get_kb('example').num_prove_calls / prove_time))
    print("total time %.2f" % (fc_time + prove_time))

# Need some extra goodies for general()...
from pyke import contexts, pattern

def general(person1 = None, person2 = None, relationship = None):

    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc2_example')      # same rule base as bc2_test()
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    args = {}
    if person1: args['person1'] = person1
    if person2: args['person2'] = person2
    if relationship: args['relationship'] = relationship
    try:
        with engine.prove_goal(
               'bc2_example.how_related($person1, $person2, $relationship)',
               **args
        ) as gen:
            for vars, plan in gen:
                print("%s, %s are %s" % (vars['person1'],
                                         vars['person2'],
                                         vars['relationship']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("bc time %.2f, %.0f goals/sec" % \
          (prove_time,
           engine.get_kb('bc2_example').num_prove_calls / prove_time))

import types

def make_pattern(x):
    if isinstance(x, str):
        if x[0] == '$': return contexts.variable(x[1:])
        return pattern.pattern_literal(x)
    if isinstance(x, (tuple, list)):
        return pattern.pattern_tuple(tuple(make_pattern(element)
                                             for element in x))
    return pattern.pattern_literal(x)
