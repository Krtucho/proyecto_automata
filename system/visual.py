import streamlit as st
from streamlit.script_runner import StopException, RerunException
from streamlit.script_request_queue import RerunData

# Importando paquetes necesarios desde el main.py
from pyke_utils.main import *


# El comando clave para acceder al apartado del cuestionario sera: /diagnostico
# Se tendra que escribir en el input que sale en la pagina web y dar click en submit

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

# ************************ YOUR CODE HERE *************************** #
# Por el momento estas preguntas y respuestas solamente funcionan para el comando diagnostico 
# Para otros comandos se debe de modificar la variable st.session_state.
choices = [["1","2","3"], ["1","2"], ["1","2", "4"]] # Posibles opciones a seleccionar por el usuario en cada momento
questions = ["Sintomas de la cabeza", "brazos", "piernas"] # Escribir Preguntas
# ******************************************************************* #


def set_choices_and_answers(command):
    """Se supone que en este metodo se cree la maquinaria para que dado un comando, se establescan las preguntas y posibles opciones a seleccionar por el usuario
    \nEx: Si el comando es /diagnostico:
    \n>choices = metodo_que_devuelva_opciones(comando)
    \n>questions = metodo_que_devuelva_preguntas(comando)"""
    # ************************ YOUR CODE HERE *************************** #
    #   choices = metodo_que_devuelva_opciones(comando)
    #   questions = metodo_que_devuelva_preguntas(comando)
    # ******************************************************************* #
    # Remove the next line
    pass

def set_answer(answer:str):
    """Al entrar en esta parte del metodo se supone que se hayan terminado las preguntas y por tanto el usuario este esperando una respuesta luego de procesar su cuestionario
        \nEl metodo set_answer es para devolver asignar dicha respuesta"""
    st.session_state.answer = answer

@st.cache
def get_question(question_number):
    """Dado un indice, busca las preguntas y opciones posibles a seleccionar y retorna estas"""
    q_choices = []
    q = ""
    if not st.session_state.finished:
        # print(question_number)
        # print(st.session_state.selected)
        if question_number < len(questions):
            q = questions[question_number]
            q_choices = choices[question_number]

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
        return "We are working on it"
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
if st.session_state.process == "quiz": # Si se encuentra realizando el quiz se les dara valores a las variables necesarias, sino, todas se van con None
    q, q_choices = get_question(st.session_state.question_number)

    if not st.session_state.finished:
        st.text(f"Please select some answers answer:\n {q}")

    if st.session_state.finished:
        st.text(f"You have finished the quiz:\n Answer:\n{st.session_state.answer}")
        write_btn = st.button("Talk with the expert system again.")
        
    for choice in q_choices:
        chk[choice] = st.checkbox(choice)
elif st.session_state.process == "writing":
    st.text("Talking with the expert system:")
    query = st.text_input("Write your query")

    btn_submit = st.button('Submit')
    if st.session_state.answer != "":
        st.text(f"Answer:\n {st.session_state.answer}")

if st.session_state.process == "quiz" and not st.session_state.finished: # Si esta en el quiz, sigue pidiendo las siguientes preguntas
    if st.button('Next question'):
        for item in chk.items():
            if item[1]:
                st.session_state.selected.append(item[0])
        st.session_state.question_number += 1

        # print(st.session_state.finished)
        # print(len(questions))
        if st.session_state.question_number >= len(questions):
            st.session_state.finished = True
            # **************** YOUR CODE HERE ********************** # Primero procesar el contenido de la variables st.session_state.selected(lista con todas las respuestas seleccionadas por el usuario) y luego llamar al metodo set_answer
            set_answer("The End!") # Al entrar en esta parte del metodo se supone que se hayan terminado las preguntas y por tanto el usuario este esperando una respuesta luego de procesar su cuestionario
                                   # El metodo set_answer es para devolver asignar dicha respuesta
            # ****************************************************** #
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