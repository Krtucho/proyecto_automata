import sys
sys.path.append('/home/krtucho/School/IA+Sim/github/proyecto_automata/pyke3-1.1.1/pyke-1.1.1')

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
# uses bc_example.krb

for chunks in chunks_list:
    driver.bc_test('dolor_en_abdomen', chunks) 