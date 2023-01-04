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
from markupsafe import string

from pyke import knowledge_engine, krb_traceback, goal

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
def is_category(category) -> bool:
    with engine.prove_goal(
               'bc_system.has_alias($category, $alias, $relationship)',
               category=category) \
        as gen:
            if gen:
                for vars, plan in gen:
                    print("%s, %s are %s" % \
                        (category, vars['alias'], vars['relationship']))
                    return True
    return False

def is_relationship(relationship) -> bool:
    with engine.prove_goal(
               'bc_system.has_related($category, $alias, $relationship)',
               relationship=relationship) \
        as gen:
            if gen:
                for vars, plan in gen:
                    print("%s, %s are %s" % \
                        (vars['category'], vars['alias'], relationship))
                    return True
    return False

def search_type(chunk) -> str:
    if is_category(chunk):
        return "cat"
    if is_relationship(chunk):
        return "rel"
    else:
        return "term"

# END ********************************************** Searching types *******************************

# BEGIN ********************************************** Searching types *******************************
def search_for_cat_cat_rel(category1=None, category2=None, relationship=None): # Returns
    result = []
    if category1:
        with engine.prove_goal(
                'bc_system.has_related($category1, $category2, $relationship)',
                category1=category1) \
            as gen:
                if gen:
                    for vars, plan in gen:
                        print("%s, %s are %s" % \
                            (vars['category1'], vars['category2'], vars["relationship"]))
                        result.append((vars['category2'], vars["relationship"]))

        with engine.prove_goal(
                'bc_system.has_related($category1, $category2, $relationship)',
                category2=category1) \
            as gen:
                if gen:
                    for vars, plan in gen:
                        print("%s, %s are %s" % \
                            (vars['category1'], vars['category2'], vars["relationship"]))
                        result.append((vars['category1'], vars["relationship"]))
    if relationship:
        with engine.prove_goal(
                'bc_system.has_related($category1, $category2, $relationship)',
                relationship=relationship) \
            as gen:
                if gen:
                    for vars, plan in gen:
                        print("%s, %s are %s" % \
                            (vars['category1'], vars['category2'], vars["relationship"]))
                        result.append((vars['category2'], vars["relationship"]))

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

def check_relationship(chunk, chunk_type, left_chunk=None, left_chunk_type=None, left_chunk_rel=None): # La idea en este punto es buscar como se relaciona el chunk actual con el anterior, si es el 1er chunk entonces solamente habra que buscar en donde aparece relacionado con alguien
    if left_chunk:
        pass
    else:
        if chunk_type == "cat":
            relationships = search_for_cat_cat_rel(category1=chunk)
            print(relationships)
        elif chunk_type == "rel":
            pass
        else:
            # Look if this chunk belogs to any category
            pass

# END ********************************************** Searching types *******************************

def bc_test(person1 = 'bruce', chunks=[]):
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc_system')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    try:
        # For a traves de todos los chunks buscando su tipo: Los tipos son Categoria, Relacion, Termino
        chunk_types = [search_type(chunk) for chunk in chunks] 

        #Luego de hallar los tipos itero por cada uno y veo si se puede relacionar con el anterior
        relationships = []
        for index, chunk in enumerate(chunks):
            if index == 0:
                relationships[index] = check_relationship(chunk, chunk_types[index])
            else:
                relationships[index] = check_relationship(chunk, chunk_types[index], chunks[index-1], chunk_types[index-1], relationships[index-1])

        # Luego de hallar las relaciones existentes entre cada chunk y su anterior, se supone que obtengamos las relaciones que existen entre todos los chunks en general 
        
        # actual = chunks[2]
        # with engine.prove_goal(
        #        'bc_system.has_related($name, $alias, $relationship)',
        #        name=actual) \
        #   as gen:
        #     for vars, plan in gen:
        #         print("%s, %s are %s" % \
        #                 (actual, vars['alias'], vars['relationship']))
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
