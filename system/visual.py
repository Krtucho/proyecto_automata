import streamlit as st
from streamlit.script_runner import StopException, RerunException
from streamlit.script_request_queue import RerunData

# Importando paquetes necesarios desde el main.py
from pyke_utils.main import *
from dicc import dicc_partes_cuerpos_sintomas

from hospital_class import Pacient

# El comando clave para acceder al apartado del cuestionario sera: /diagnostico
# Se tendra que escribir en el input que sale en la pagina web y dar click en submit

# Side Bar
st.sidebar.text("Comandos")#add_rows(["Commands:", "/diagnostico"])
st.sidebar.text("/diagnostico")

cant_questions=0
sexo = ""
# sintomas_seleccionados=[]
input_answer=False

# choices=[]
# questions=[]


if 'question_number' not in st.session_state:
    st.session_state.question_number=0 # Aqui se le asigna el indice actual de la pregunta en el cuestionario

if 'selected' not in st.session_state:
    st.session_state.selected = [] # Aqui se guardan todas las opciones seleccionadas por el usuario

if 'finished' not in st.session_state:
    st.session_state.finished = False # Variable para saber si ha terminado el cuestionario o no

if 'process' not in st.session_state:
    st.session_state.process = "writing" # Dice si se encuentra escribiendo ciertas consultas(writing) o respondiendo un cuestionario(quiz)

if 'answer' not in st.session_state:
    st.session_state.answer = "" # Ultima respuesta que retorno el sistema experto

if 'choices' not in st.session_state:
    st.session_state.choices = []   # Opciones

if 'questions' not in st.session_state:
    st.session_state.questions = [] # Preguntas

if 'symptoms_frecuencies' not in st.session_state:
    st.session_state.symptoms_frecuencies = {}

# ************************ YOUR CODE HERE *************************** #
if 'indroductory_text' not in st.session_state:
    st.session_state.introductory_text = "your_text" # Asignar a esta variable texto introductorio para mostrar en la 1ra pregunta del cuestionario
# ******************************************************************* #

if 'patients_list' not in st.session_state:
    st.session_state.patients_list = []
    
if 'actual_patient' not in st.session_state:
    st.session_state.actual_patient = Pacient(None, None, [], None)

if 'actual_patient_tumor' not in st.session_state:
    st.session_state.actual_patient_tumor = False

if 'name_input' not in st.session_state:
    st.session_state.name_input = ''
# ************************ YOUR CODE HERE ONLY FOR TEST PURPOSES, SO...DO NOT TOUCH IT NOW *************************** #
# Por el momento estas preguntas y respuestas solamente funcionan para el comando diagnostico 
# Para otros comandos se debe de modificar la variable st.session_state.
# choices = st.session_state.choices # choices = [["1","2","3"], ["1","2"], ["1","2", "4"]] # Posibles opciones a seleccionar por el usuario en cada momento
# questions = st.session_state.questions # questions = ["Sintomas de la cabeza", "brazos", "piernas"] # Escribir Preguntas
# print(st.session_state.finished)
# choices=[]
# questions=[]
# st.session_state.choices=choices
# st.session_state.questions=questions
# ******************************************************************* #

# name_input = None

def build_patient_quiz():
    print("inside build_patient_quiz()")

    st.session_state.questions.append("Seleccione los tumores")
    st.session_state.choices.append(["cerebro","pancreas","pulmones","ovarios","mama"])
    st.session_state.questions.append("Seleccione las terapias")
    st.session_state.choices.append(["cirugia ","quimioterapia","radioterapia","cuidados paulativos","No he recibido terapia en estos ultimos meses"])


def print_actual_patient():
    print("*********************** Actual Patient ****************")
    print(f"name: {st.session_state.actual_patient.name}")
    print(f"possible_tumors: {st.session_state.actual_patient.possibles_tumors}")
    print(f"theraphies: {st.session_state.actual_patient.therapies_receiving}")
    print(f"type_tumor: {st.session_state.actual_patient.type_tumor}")
                
def add_patient_possible_tumors(symptoms):
    possible_tumors =  driver.tumors_has_many_symptoms(symptoms)# Find_tumors
    pos_tumors_list = [key for key,_ in possible_tumors.items()]
    print(pos_tumors_list)
    for tumor in pos_tumors_list:
        st.session_state.actual_patient.possibles_tumors.append(tumor)# = [key for key,_ in possible_tumors.items()]
    return possible_tumors

def set_choices_and_answers(command):
    """Se supone que en este metodo se cree la maquinaria para que dado un comando, se establescan las preguntas y posibles opciones a seleccionar por el usuario
    \nEx: Si el comando es /diagnostico:
    \n>choices.clear()
    \n>choices.extend(metodo_que_devuelva_opciones(comando))
    \n>questions.clear()
    \n>questions.extend(metodo_que_devuelva_preguntas(comando))"""

    print("this is the way i supose to work")

    if st.session_state.actual_patient_tumor and st.session_state.question_number > 3:
        return


    if command == "/diagnostico":
        if st.session_state.question_number == 0:
            if not ["Femenino", "Masculino"] in st.session_state.choices:
                st.session_state.choices.append(["Femenino", "Masculino"])
            if not "Que sexo presenta?" in st.session_state.questions:
                st.session_state.questions.append("Que sexo presenta?")
        elif st.session_state.question_number == 1:
            # name_input = st.text_input("Write your name")
            st.session_state.name_input = st.text_input("Write your name")
            # print(f"name_input: {name_input}")
            if not "Enter your name" in st.session_state.questions:
                st.session_state.questions.append("Enter your name")
            if not [] in st.session_state.choices:
                st.session_state.choices.append([])
        elif st.session_state.question_number == 2:
            if not "Conoce el tipo de cancer que presenta? Marque si la conoce" in st.session_state.questions:
                st.session_state.questions.append("Conoce el tipo de cancer que presenta? Marque si la conoce")
            if not ["si, lo conozco"] in st.session_state.choices:
                st.session_state.choices.append(["si, lo conozco"])
        elif st.session_state.question_number == 3:
            # st.session_state.actual_patient_tumor = False
            print("*********************** Question 3 *********************")
            print(st.session_state.actual_patient_tumor)
            if st.session_state.actual_patient_tumor:
                build_patient_quiz()

        # elif st.session_state.question_number == 4:
            else:
                sexo=st.session_state.selected
                if not ["en la cabeza","en el estomago","en las extremidades","en el pecho","en la parte baja de la cintura","en la espalda","en el cuello"] in st.session_state.choices:
                    st.session_state.choices.append(["en la cabeza","en el estomago","en las extremidades","en el pecho","en la parte baja de la cintura","en la espalda","en el cuello"])
                if not "Seleccione las parte del cuerpo donde presenta algun malestar o sintoma" in st.session_state.questions:
                    st.session_state.questions.append("Seleccione las parte del cuerpo donde presenta algun malestar o sintoma")
        elif st.session_state.question_number == 4:
            if len(st.session_state.selected) >1:
                print("Entre aquiiiiii")
                parte_cuerpo=[]
                sintomas=[]
                for item in st.session_state.selected:
                    if item in dicc_partes_cuerpos_sintomas:
                        parte_cuerpo.append(item)
                        print("Estoy en set_answer_questions")
                        # if not "Que sintomas presenta "+ item +" ?" in st.session_state.questions:
                        #     st.session_state.questions.append("Que sintomas presenta "+ item +" ?")
                        opciones=[sint for sint in dicc_partes_cuerpos_sintomas[item]]
                        for opc in opciones:
                            if not opc in sintomas:
                                sintomas.append(opc)
                        # if not opciones in sintomas:
                        #     sintomas.extend(opciones)
                            # st.session_state.choices.extend(opciones)
                name=""
                for item in range(0,len(parte_cuerpo)):
                    if item == (len(parte_cuerpo)- 2):
                        name += parte_cuerpo[item] + " y "
                    elif item < (len(parte_cuerpo) - 1):
                        name += parte_cuerpo[item] + ", "
                    else:
                        name += parte_cuerpo[item]
                question="Que sintomas presenta "+ name +" ?"
                if not question in st.session_state.questions:
                    st.session_state.questions.append(question)
                if not sintomas in st.session_state.choices:
                    st.session_state.choices.append(sintomas)
            else:            
                for item in st.session_state.selected:
                    if item in dicc_partes_cuerpos_sintomas:
                        print("Estoy en set_answer_questions")
                        if not "Que sintomas presenta "+ item +" ?" in st.session_state.questions:
                            st.session_state.questions.append("Que sintomas presenta "+ item +" ?")
                        opciones=[sint for sint in dicc_partes_cuerpos_sintomas[item]]
                        if not opciones in st.session_state.choices:
                            st.session_state.choices.append(opciones)
        elif st.session_state.question_number == 5:
            if not ["una semana","dos semanas","tres semanas","un mes","2 meses","mas de 2 meses"] in st.session_state.choices:
                st.session_state.choices.append(["una semana","dos semanas","tres semanas","un mes","2 meses","mas de 2 meses"])
            if not "Cantidad de dias que lleva presentando los sintomas seleccionados" in st.session_state.questions:
                st.session_state.questions.append("Cantidad de dias que lleva presentando los sintomas seleccionados")
        elif st.session_state.question_number == 6:
            if not ["cirugia ","quimioterapia","radioterapia","cuidados paulativos","No he recibido terapia en estos ultimos meses"] in st.session_state.choices:
                st.session_state.choices.append(["cirugia ","quimioterapia","radioterapia","cuidados paulativos","No he recibido terapia en estos ultimos meses"])
            if not "Ha recibido terapia en los ultimos 5 meses? Si es el caso por favor marque la terapia que ha recibido" in st.session_state.questions:
                st.session_state.questions.append("Ha recibido terapia en los ultimos 5 meses? Si es el caso por favor marque la terapia que ha recibido")
        # elif st.session_state.question_number == 5:
        #     pass
            # ************************ YOUR CODE HERE CARLOS *************************** #
            #   eh siguiendo el orden de la hoja de supone que ahora vendria lo de la frecuencia de los sintomas, en realidad este orden no esta bien pero eso 
            #   es lo de menos ahora 
        elif st.session_state.question_number == 7:
            # if not ["cirugia ","quimioterapia","radioterapia","cuidados paulativos"] in st.session_state.choices:
            #     st.session_state.choices.append(["cirugia ","quimioterapia","radioterapia","cuidados paulativos","No he recibido terapia en estos ultimos meses"])
            if not "Cuanto tiempo lleva presentando los sintomas" in st.session_state.questions:
                st.session_state.questions.append("Cuanto tiempo lleva presentando los sintomas")
                final_choices = []
                frecuencies = ["varias veces al dia","diario", "semanal", "mensual"]
                for sym, _ in st.session_state.symptoms_frecuencies.items():
                    for frecuency in frecuencies:
                        final_choices.append(f"{sym}-{frecuency}")

                st.session_state.choices.append(final_choices)
                
            # ******************************************************************* #

            print("Choices")
            print(st.session_state.choices)
            print("Questions")
            print(st.session_state.questions)
            print("Selected")
            print(st.session_state.selected)
        else:
            if not ["Asma","Epilepsia","Diabetes","Hipertension","Obesidad"] in st.session_state.choices:
                st.session_state.choices.append(["Asma","Epilepsia","Diabetes","Hipertension","Obesidad"])
            if not "Presenta alguna enfermedad cronica? Si es el caso por favor marque la enfermedad que presenta" in st.session_state.questions:
                st.session_state.questions.append("Presenta alguna enfermedad cronica? Si es el caso por favor marque la enfermedad que presenta")

        # st.session_state.choices.clear()
        # st.session_state.questions.clear()

        print("questions choices kldkslhjd")
        print(st.session_state.questions)
        print(st.session_state.choices)

        
    # ************************ YOUR CODE HERE *************************** #
    #   choices = metodo_que_devuelva_opciones(comando)
    #   questions = metodo_que_devuelva_preguntas(comando)
    # ******************************************************************* #
    # Remove the next line

        # Asignar texto introductorio
    st.session_state.introductory_text = "your_text" 

def set_answer(answer:str):
    """Al entrar en esta parte del metodo se supone que se hayan terminado las preguntas y por tanto el usuario este esperando una respuesta luego de procesar su cuestionario
        \nEl metodo set_answer es para devolver asignar dicha respuesta"""
    st.session_state.answer = answer

@st.cache
def get_question(question_number):
    """Dado un indice, busca las preguntas y opciones posibles a seleccionar y retorna estas"""
    q_choices = []
    q = ""

    print("Llegue a este metodoooooooo")
    print(question_number)
    print(len(st.session_state.questions))


    
    if not st.session_state.finished:
        print("Estoy dentro de get_question")
        
                    # st.session_state.question_number+=1
        # print(question_number)
        # print(st.session_state.selected)
        
        if question_number < len(st.session_state.questions):
            q = st.session_state.questions[question_number]
            q_choices = st.session_state.choices[question_number]

    return  q, q_choices

def process_query(query:str):
    """Este metodo se supone que llame a algo del main.py y se procese la consulta brindada por el usuario"""
    # La idea esta en pasar una lista de comandos y escoger cual de todos matchea con la consulta, igual.
    # En caso de que ninguno matchee habria que buscar lo que devuelve el procesamiento de la consulta(nlp) y ver si se desea llamar a algun comando
    # Lista con todos los posibles comandos:
    # ************************ YOUR CODE HERE *************************** #
    command_list = ["/diagnostico"]
    # ******************************************************************* #
    if query in command_list: # Si se escribe este comando se llama al quiz para que este se ejecute y salga el menu interactivo
        st.session_state.process = "quiz"
        st.session_state.selected = []
        st.session_state.finished = False
        st.session_state.question_number = 0
        set_choices_and_answers(command=query) # Para este caso query sera nuestro comando. Tenerlo en cuenta.
    else:
        return ask(query)
    return ""
    
def exit_quiz():
    """Metodo para detener la ejecucion del cuestionario luego de haber dado una respuesta al usuario y haber presionado el boton para volver a escribirle al sistema experto"""
    st.session_state.process = "writing"
    st.session_state.selected = []
    st.session_state.finished = False
    st.session_state.question_number = 0
    st.session_state.answer = ""


q, q_choices =  None, None # Preguntas y respuestas temporales para el quiz
chk = {}    # Diccionario con llaves como strings(opciones) y valores como checkboxes con el contenido de las opciones.
            # Se utiliza para luego agregarlo a las opciones que ha seleccionado el usuario. Se asume que todas las opciones disponibles son distintas

btn_submit = None
write_btn = None

clear_users_btn = None
make_test_btn = None


if st.session_state.process == "quiz": # Si se encuentra realizando el quiz se les dara valores a las variables necesarias, sino, todas se van con None

    print("Estoy en el if de quiz el primero")

    set_choices_and_answers("/diagnostico")

    q, q_choices = get_question(st.session_state.question_number)

    if st.session_state.question_number == 0:
        st.text(f"{st.session_state.introductory_text}")

    if not st.session_state.finished:
        st.text(f"Please select some answers:\n {q}")

    if st.session_state.finished:
        st.text(f"You have finished the quiz:\n Answer:\n{st.session_state.answer}")
        write_btn = st.button("Talk with the expert system again.")
    
    print("Choice")
    for choice in q_choices:
        chk[choice] = st.checkbox(choice)
        print(choice)
elif st.session_state.process == "writing":
    st.text("Talking with the expert system:")
    query = st.text_input("Write your query")

    btn_submit = st.button('Submit')
    if st.session_state.answer != "":
        st.text(f"Answer:\n {st.session_state.answer}")

if st.session_state.process == "quiz" and not st.session_state.finished: # Si esta en el quiz, sigue pidiendo las siguientes preguntas
    if st.button('Next question'):
        print("Ahora estoy aqui dentro")
        print(chk)
            
        print("********************* Name ******************")
        # print(st.session_state.name_input)
        if st.session_state.question_number == 1:
            st.session_state.actual_patient.name = st.session_state.name_input

        # if st.session_state.question_number == 2:
        #     print("******************* Question Number 2 ******************")
        #     print(chk)

        for item in chk.items():
            if item[1]:
                st.session_state.selected.append(item[0])
                print("*********************************** Taking *************************")
                print(item[0])
                print(item[1])
                print(st.session_state.question_number)

                if st.session_state.question_number == 2:
                    st.session_state.actual_patient_tumor = True
                    print(st.session_state.actual_patient_tumor)

                if st.session_state.actual_patient_tumor:
                    if st.session_state.question_number == 3:
                        st.session_state.actual_patient.type_tumor = item[0]
                    elif st.session_state.question_number == 4:
                        st.session_state.actual_patient.therapies_receiving = item[0]
                        
                    continue
                # Newwwwwwwwwwwww
                # Si es una pregunta del tipo de enfermedad-frecuencia, annadelo al diccionario que contiene las enfermedades con su frecuencias
                if st.session_state.question_number == 4:# Si se encuentra en la pregunta de sintoma
                    st.session_state.symptoms_frecuencies[item[0]] = []
                if st.session_state.question_number == 7:# Si se encuentra en la pregunta de sintoma-frecuencia
                    substr:str = item[0]
                    try:
                        substr = substr.split('-')[0]
                        st.session_state.symptoms_frecuencies[substr].append(item[0])
                        print("**************************** Inside symptoms-frecuencies ********************")
                        print(substr)
                        print(st.session_state.symptoms_frecuencies[substr])
                    except Exception as e:
                        print(e)
                # End Newwwwwwwwww

                # st.session_state.question_number += 1
        print(st.session_state.selected)

        if st.session_state.actual_patient_tumor:
            if st.session_state.question_number == 4:
                print_actual_patient()
                st.session_state.finished = True

        # if cant_questions < len(st.session_state.questions):
        st.session_state.question_number += 1
            # cant_questions=len(st.session_state.questions)
        
        print("st.session_state.question_number")
        print(st.session_state.question_number)

        # if st.session_state.question_number == 3:
        #     sintomas_seleccionados=st.session_state.selected[2]
        
        print("sintomas_seleccionados")
        print(st.session_state.selected)
        
        if st.session_state.question_number > len(st.session_state.questions) or len(st.session_state.questions) == 8: # Modified 5->6
            print("termino")
            print("symptoms frecuencies")
            for t,f in st.session_state.symptoms_frecuencies.items():
                print(f"{t}: {f}")
            st.session_state.finished = True

            # sintomas_seleccionados=st.session_state.selected
            # lista=[]
            # lista.append(st.session_state.selected[2])
            #  = driver.tumors_has_many_symptoms(lista)
            tumors_dict = add_patient_possible_tumors([st.session_state.selected[2]])
            st.session_state.patients_list.append(st.session_state.actual_patient)
            print("tumors dict")
            print(tumors_dict)
            print(tumors_dict.keys())
                    # **************** YOUR CODE HERE ********************** # Primero procesar el contenido de la variables st.session_state.selected(lista con todas las respuestas seleccionadas por el usuario) y luego llamar al metodo set_answer
            set_answer(tumors_dict) # Al entrar en esta parte del metodo se supone que se hayan terminado las preguntas y por tanto el usuario este esperando una respuesta luego de procesar su cuestionario
                                        # El metodo set_answer es para asignar dicha respuesta a las variables o codigos que renderizaran este texto
                    # ****************************************************** #
            print_actual_patient()



        # print("Despues set answer y demas")
        # # print(st.session_state.question_number)
        # print(questions)
        # print(choices)

        # chk = {}
        # # st.session_state.choices = [] 

        # print("st.session_state.finished")
        # print(st.session_state.finished)

        # # print("q")
        # # print(q)
        # # print("q_choices")
        # # print(q_choices)

        # q, q_choices = get_question(st.session_state.question_number)

        # if not st.session_state.finished:
        #     st.text(f"Please select some answers:\n {q}")
            
        # for choice in q_choices:
        #     print("Se supone que aqui tiene que entrar")
        #     chk[choice] = st.checkbox(choice)
        #     print(choice)
        #     print(chk)

        st.experimental_rerun()
            
elif write_btn:
    exit_quiz() # Se ha terminado el quiz y se restablecen las variables
    st.experimental_rerun()
else:
    if btn_submit: # Se ha subido una consulta para ser procesada(Puede que haya que hacer uso del menu interactivo o puede que no)
            answer = process_query(query)
            # print(query)
            # print(answer)
            # print(st.session_state.process )
            if st.session_state.process == "writing": # Si se ha encontrado con que no es necesario comenzar con el menu interactivo. Se establece como ultima respuesta del sistema experto la que este acaba de dar a la consulta realizada por el usuario
                set_answer(answer)

            st.experimental_rerun()

#*********************************
# get name
# if st.session_state.question_number == :
#     query = st.text_input("Write your name")


def add_patient_name(name):
    st.session_state.actual_patient.name = name


if not st.session_state.process == "quiz":
    clear_users_btn = st.button('Vaciar lista de pacientes')
    make_test_btn = st.button('Correr Horario')

if clear_users_btn:
    st.session_state.patients_list = []
elif make_test_btn:
    answer = "csp(st.session_state.patients_list)"
    set_answer(answer)
