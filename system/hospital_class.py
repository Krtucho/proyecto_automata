from enum import Enum

class Type_of_therapy(Enum):
    Quimioterapia = 1
    Radioterapia = 2
    Cirugia = 3
    
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
        self.doctor=None
        self.apparatus=None

class Doctor:
    def __init__(self, specialty, work_hours, pacients, name, id):
        self.specialty=specialty
        self.work_hours=work_hours
        self.pacients=pacients
        self.available=True
        self.name=name
        self.id=id

class Consultation_room:
    def __init__(self):
        self.is_empty=True

class Apparatus:
    def __init__(self, name, id):
        self.id=id
        self.name=name
        # self.type_of_therapy=type_of_therapy
        self.available=True

class Therapy_apparatus(Apparatus):
    def __init__(self, type_of_therapy, name, id):
        super().__init__(name, id)
        self.c=type_of_therapy
        self.available=True

class Cirugia(Apparatus):
    def __init__(self, name, id, total_hours, hours_elapsed):
        super().__init__(name, id)
        self.type_of_therapy=Type_of_therapy.Cirugia
        self.total_hours=total_hours
        self.hours_elapsed=hours_elapsed

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


    def find_edge(self, node1, node2):
        for edge in self.edges:
            if edge.node1.name == node1.name and self.node2.name ==node2.name:
                return edge
        return None

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




class Edge:
    def __init__(self, node1, node2):
        self.node1=node1
        self.node2=node2

