import sys
# Descomentar la siguiente linea
# sys.path.append('your_path') # Ex: 'system/pyke_utils'

sys.path.append('/home/krtucho/School/IA_Sim/github/proyecto_automata/system/pyke_utils')

import examples.system.driver as driver

from preprocess import PreprocessText

rules = {"n_grams":3, "types":["VERB", "NOUN", "PROPN"]} # Default Rules
# temp = PreprocessText.filter_by_rules("dolores y dolor en abdomen muy malos", rules=rules)
# print(temp)
# Metodo principal de este archivo Descomentar las siguientes lineas para hacer uso de el desde otro archivo
def ask(query:str, rules:dict=rules) -> str:
    """Dada una pregunta se devuelve la respuesta a la misma luego de ser procesada por el sistema experto"""
    try:
        sentences = PreprocessText.sentence_segmentation(query)

        chunks_list = []
        for sentence in sentences:
            chunks_list.append(PreprocessText.filter_by_rules(sentence, rules=rules))

        # for chunks in chunks_list:
        #     words = [l for (w,l,p) in chunks]  
        output = ""

        print(chunks_list)
        for index, chunks in enumerate(chunks_list):
            output += driver.get_answer(sentences[index], PreprocessText.normalize(chunks))

        return output#driver.get_answer(query, chunks)
    except Exception as e:
        print(e)
        return "Error! :("


# sentences = PreprocessText.sentence_segmentation("¿Cuáles son los síntomas que presenta el cáncer de páncreas?")


# chunks_list = []
# for sentence in sentences:
#     chunks_list.append(PreprocessText.get_verbs_and_nouns(sentence))

# Cuales son los sintomas que presenta el cancer de pancreas
chunks = ["sintoma", "presentar", "cancer", "pancreas"]
# chunks = ["sintomas", "cancer"]
# chunks = ["tumor", "pancreas"]

# Para los casos de palabras compuestas, tendremos que tomar el chunk como una, ej
# Dolor de algo......Se hace necesario tomar un chunk como ambas palabras unidas
# Dolor en algo
# algo del
# algo a
# Annadir en archivo preprocess.py un metodo que filtre un chunk por reglas
# @staticmethod
# def filter_by_rules(tokens:list, rules:dict):
# Se espera que list sean un 2-grama o 3-grama, o n-grama
#   target = "".join(_,tokens)
#   return rules[target] != None
# uses bc_example.krb

# for chunks in chunks_list:
#     words = [l for (w,l,p) in chunks]    
tumors_dict = driver.tumors_has_many_symptoms(['dolores_de_cabeza', 'dificultad_para_tomar_decisiones', 'ictericia']) # Metodo para obtener tumores de sintomas

# Para probar como se comporta el sistema experto con la consulta que se encuentra en la variable chunks(procesada por nlp) descomente la siguiente linea
# resp = driver.get_answer('dolor_en_abdomen', chunks)#PreprocessText.normalize(words)) 
# print(ask("sintomas de cancer de pancreas"))
# ask("ictericia y gases")

ask("tumor")

# enfermedad etapa
# enfermedad sintoma

# enfermedad tratamiento