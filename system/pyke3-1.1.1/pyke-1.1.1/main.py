import sys
sys.path.append('your_path')

import examples.system.driver as driver

from preprocess import PreprocessText
sentences = PreprocessText.sentence_segmentation("¿Cuáles son los síntomas que presenta el cáncer de páncreas?")

chunks_list = []
for sentence in sentences:
    chunks_list.append(PreprocessText.get_verbs_and_nouns(sentence))

# Cuales son los sintomas que presenta el cancer de pancreas
# chunks = ["sintoma", "presenta", "cancer", "pancreas"]

# Para los casos de palabras compuestas, tendremos que tomar el chunk como una, ej
# Dolor de algo......Se hace necesario tomar un chunk como ambas palabras unidas
# Annadir en archivo preprocess.py un metodo que filtre un chunk por reglas
# @staticmethod
# def filter_by_rules(tokens:list, rules:dict):
# Se espera que list sean un 2-grama o 3-grama, o n-grama
#   target = "".join(_,tokens)
#   return rules[target] != None
# uses bc_example.krb

for chunks in chunks_list:
    words = [l for (w,l,p) in chunks]    
    driver.bc_test('dolor_en_abdomen', PreprocessText.normalize(words)) 