
class Pacient:
    def __init__(self, type_tumor, therapies_receiving, possibles_tumors, name): #sex, symptoms, days_with_symptoms, therapies_received, frecuency_symptoms, chronic_diseases,'"""" type_tumor, therapies_receiving, possibles_tumors):
        # self.sex=sex
        # self.symptoms=symptoms
        # self.days_with_symptoms=days_with_symptoms
        # self.therapies_received=therapies_received
        # self.frecuency_symptoms=frecuency_symptoms
        # self.chronic_diaseases=chronic_diseases
        #Trabajo en CSP
        self.type_tumor=type_tumor
        self.therapies_receiving=therapies_receiving
        self.possibles_tumors=possibles_tumors
        self.name=name

    def __str__(self) -> str:
        return self.name

class Doctor:
    def __init__(self, specialty, work_hours, pacients, name):
        self.specialty=specialty
        self.work_hours=work_hours
        self.pacients=pacients
        self.available=True
        self.name=name

    def __str__(self) -> str:
        return self.name

class Consultation_room:
    def __init__(self):
        self.is_empty=True

class Apparatus:
    def __init__(self, name, id):
        self.id=id
        self.name=name
        self.available=True
    
    def __str__(self) -> str:
        return self.name

class Therapy_apparatus(Apparatus):
    def __init__(self, type_of_therapy, name, id):
        self.id=id
        self.type_of_therapy=type_of_therapy
        self.name=name
        self.available=True

class Medical_consultation:
    def __init__(self, doctor, pacient, consultation_room, duration):
        self.doctor=doctor
        self.pacient=pacient
        self.consultation_room=consultation_room
        self.duration=duration

class Solution:
    def __init__(self):
        self.doctors=[]
        self.apparatus=[]

    def __str__(self) -> str:
        return str(self.doctors) + "\n" + str(self.apparatus)

class Graph:
    def __init__(self, nodes):
        self.nodes=nodes
        self.edges=[]

        self.adj_list = {node:[] for node in nodes}
        
    def neighbors(self, node):
        neighbors_list=[]
        for edge in self.edges:
            if edge.node1==node:
                neighbors_list.append(edge.node2)
            elif edge.node2 == node:
                neighbors_list.append(edge.node1)
        return neighbors_list

    def has_edge(self, node1, node2):
        if self.adj_list[node1]:
            if node2 in self.adj_list[node1]:
                return True
        return False

    def insert(self, node1, node2):
        if not self.has_edge(node1, node2):
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)
            self.edges.append(Edge(node1, node2))

    def get_unidirected_edges(self):
        pass




class Edge:
    def __init__(self, node1, node2):
        self.node1=node1
        self.node2=node2

