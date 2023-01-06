import sys
sys.path.append('/home/krtucho/School/IA+Sim/github/proyecto_automata/pyke3-1.1.1/pyke-1.1.1')

import examples.system.driver as driver

# Cuales son los sintomas que presenta el cancer de pancreas
chunks = ["sintoma", "presenta", "cancer", "pancreas"]

# Para los casos de palabras compuestas, tendremos que tomar el chunk como una, ej
# Dolor de algo......Se hace necesario tomar un chunk como ambas palabras unidas
# uses bc_example.krb
driver.bc_test('dolor_en_abdomen', chunks) 