from hospital_class import *



pacientes_rel_doct_sala_apar={}

doctor1=Doctor("pancrea", 10, None, "Doctor1")
doctor2=Doctor("General", 10, None, "Doctor2")
doctor3=Doctor("ovario", 10, None, "Doctor3")
doctor4=Doctor("General", 10, None, "Doctor4")
doctor5=Doctor("cerebro", 10, None, "Doctor5")

aparato1=Apparatus("AparatoP", 1)
aparato2=Apparatus("X-Ray", 2)
aparato3=Apparatus("X-Ray", 3)
aparato4=Apparatus("AparatoO1", 4)
aparato5=Apparatus("AparatoO2", 5)

paciente1=Pacient(None, None, ["pancrea"], "1")
paciente2=Pacient("pancrea", "X-Ray", None, "2")
paciente3=Pacient(None, None, ["cerebro"], "3")
paciente4=Pacient(None, None, ["ovario"],"4")
paciente5=Pacient("ovario", "AparatoO1", None, "5")

pacientes=[paciente1, paciente2, paciente3, paciente4, paciente5]
doctors=[doctor1, doctor2, doctor3, doctor4, doctor5]
aparatos=[aparato1, aparato2, aparato3, aparato4, aparato5]

enfermedad_dicc={"pancrea":Solution(), "ovario":Solution(), "cerebro":Solution()}
terapias_dicc={"pancrea":Solution(), "ovario":Solution(), "cerebro":Solution()}

enfermedad_dicc["pancrea"].apparatus.append(aparato1)
enfermedad_dicc["ovario"].apparatus.append(aparato4)
enfermedad_dicc["ovario"].apparatus.append(aparato5)

for doctor in doctors:
    if doctor.specialty == 'General':
        for terapia in terapias_dicc.keys():
            if not doctor in terapias_dicc[terapia].doctors:
                terapias_dicc[terapia].doctors.append(doctor)
    else:
        if not doctor in terapias_dicc[doctor.specialty].doctors and not doctor in enfermedad_dicc[doctor.specialty].doctors:
            enfermedad_dicc[doctor.specialty].doctors.append(doctor)
            terapias_dicc[doctor.specialty].doctors.append(doctor)

print("Despues de agregar doctores")
print(enfermedad_dicc)
print(terapias_dicc)

for aparato in aparatos:
    if aparato.name == "X-Ray":
        for item in enfermedad_dicc.keys():
            if not aparato in enfermedad_dicc[item].apparatus and not aparato in terapias_dicc[item].apparatus:
                enfermedad_dicc[item].apparatus.append(aparato)
                terapias_dicc[item].apparatus.append(aparato)
    elif aparato.name == "Quimioterapia" or aparato.name == "Radioterapia" or aparato.name == "Cirugia" or aparato.name == "Cuidados paliativos":
        for terapia in terapias_dicc.keys():
            if not aparato in terapias_dicc[terapia].apparatus:
                terapias_dicc[terapia].apparatus.append(aparato)

print("Despues de agregar aparatos")
print(enfermedad_dicc)
print(terapias_dicc)


for paciente in pacientes:
    pacientes_rel_doct_sala_apar[paciente]=Solution()
    temp=pacientes_rel_doct_sala_apar[paciente]
    if not paciente.type_tumor == None:
        for doctor in terapias_dicc[paciente.type_tumor].doctors:
            if doctor.available:
                temp.doctors.append(doctor)
        for aparato in terapias_dicc[paciente.type_tumor].apparatus:
            if aparato.available and aparato.name == paciente.therapies_receiving:
                temp.apparatus.append(aparato)
    else:
        for tumor in paciente.possibles_tumors:
            for doctor in enfermedad_dicc[tumor].doctors:
                if doctor.available:
                    temp.doctors.append(doctor)
            for aparato in enfermedad_dicc[tumor].apparatus:
                if aparato.available:
                    temp.apparatus.append(aparato)

print("Pacientes")
print(pacientes)

doctors_graph=Graph(pacientes)
aparatos_graph=Graph(pacientes)

print(doctors_graph)
print(aparatos_graph)

for paciente1 in pacientes:
    for paciente2 in pacientes:
        if not paciente1.name == paciente2.name:
            if not paciente1.type_tumor == None and not paciente2.type_tumor == None:

                if paciente1.type_tumor == paciente2.type_tumor:
                    # doctors_graph.insert(paciente1, paciente2)
                    aparatos_graph.insert(paciente1, paciente2)
                elif paciente1.therapies_receiving == paciente2.therapies_receiving:
                    aparatos_graph.insert(paciente1, paciente2)
                # else:
                doctors_graph.insert(paciente1, paciente2)

            elif not paciente1.type_tumor == None and not paciente2.possibles_tumors == None:
                if paciente1.type_tumor in paciente2.possibles_tumors:
                    doctors_graph.insert(paciente1, paciente2)
                    aparatos_graph.insert(paciente1, paciente2)
                else:
                    aparatos_graph.insert(paciente1, paciente2)

            elif not paciente1.possibles_tumors == None and not paciente2.type_tumor == None:
                if paciente2.type_tumor in paciente1.possibles_tumors:
                    doctors_graph.insert(paciente1, paciente2)
                    aparatos_graph.insert(paciente1, paciente2)
                else:
                    aparatos_graph.insert(paciente1, paciente2)

            elif not paciente1.possibles_tumors == None and not paciente2.possibles_tumors == None:
                for tumor1 in  paciente1.possibles_tumors:
                    if tumor1 in paciente2.possibles_tumors:
                        doctors_graph.insert(paciente1, paciente2)
                        aparatos_graph.insert(paciente1, paciente2)
                        break

print(doctors_graph)
print(aparatos_graph)

def edge_sort():
    nodes_sort=doctors_graph.nodes.copy()
    for i in range(0,len(doctors_graph.nodes)):
        for j in range(0,len(doctors_graph.nodes)):
            node1=nodes_sort[i]
            node2=nodes_sort[j]
            if len(pacientes_rel_doct_sala_apar[node1].doctors) < len(pacientes_rel_doct_sala_apar[node2].doctors):
                # node=nodes_sort[i]
                nodes_sort[i]=node2
                nodes_sort[j]=node1

    edges_sort=[]
    for node in nodes_sort:
        for edge in doctors_graph.edges:
            if edge.node1.name == node.name and not edge in edges_sort:
                edges_sort.append(edge)
    return edges_sort






def domain(x_i, domain_type="doctors"):
    if domain_type == "doctors":
        return pacientes_rel_doct_sala_apar[x_i].doctors
    elif domain_type == "aparatos":
        return pacientes_rel_doct_sala_apar[x_i].apparatus

def check_domain(pacient_dicc):
    for item in pacient_dicc.values():
        if item.doctors == []:
            return False
    return True


def delete_from_domain(x_i, x, domain_type="doctors"):
    if domain_type=="doctors":
        solution:list = pacientes_rel_doct_sala_apar[x_i].doctors
        solution.remove(x)
    elif domain_type=="aparatos":
        solution:list = pacientes_rel_doct_sala_apar[x_i].apparatus
        solution.remove(x)



def remove_inconsistent_values(x_i, x_j, domain_type="doctors"): # returns true iff succeeds
    removed = False
    dom=domain(x_i, domain_type=domain_type).copy()
    for x in dom:
        if x in domain(x_j, domain_type=domain_type):
            delete_from_domain(x_i, x, domain_type=domain_type)
            removed = True
    return removed

def neighbors(x_i):
    return doctors_graph.neighbors(x_i)

def actualizar_dominio(paciente1, doctor1, pacient_dicc):
    pacient_dicc_copy=pacient_dicc.copy()
    for paciente in pacient_dicc_copy:
        doctors=pacient_dicc_copy[paciente].doctors
        doct=doctors.copy()
        for doctor in doct:
            if paciente.name == paciente1.name:
                if not doctor.name == doctor1.name:
                    pacient_dicc[paciente].doctors.remove(doctor)
            else:
                if doctor.name == doctor1.name:
                    pacient_dicc[paciente].doctors.remove(doctor)

def valid_solution(pacient_dicc):
    for solution in pacient_dicc.values():
        if not len(solution.doctors) == 1:
            return False
    return True


def ac_3(csp,doctors_queue, pacient_dicc): # returns the CSP, posibly with reduced domains
    if valid_solution(pacient_dicc) and len(doctors_queue) == 0:
        return pacient_dicc
    else:
    # doctors_queue
        while len(doctors_queue) > 0:
            edge = doctors_queue.pop()
            x_i = edge.node1
            x_j = edge.node2
            doctors1=pacient_dicc[x_i].doctors.copy()
            doctors2=pacient_dicc[x_j].doctors.copy()
            for doctor1 in doctors1:
                for doctor2 in doctors2:
                    if not doctor1 == doctor2:
                        x_i.doctor=doctor1
                        x_j.doctor=doctor2
                    # if remove_inconsistent_values(x_i, x_j, domain_type="doctors"):
                        print("doctors_graph.neighbors(x_i)")
                        print(doctors_graph.neighbors(x_i))

                        actualizar_dominio(x_i, doctor1, csp.copy())
                        actualizar_dominio(x_j, doctor2, csp.copy())

                        if check_domain(csp.copy()):
                            for x_k in neighbors(x_i):
                                doctors_queue.append(Edge(x_k, x_i))

                            aparatos_queue
                        while len(aparatos_queue) > 0:
                            edge = aparatos_queue.pop()
                            x_i = edge.node1
                            x_j = edge.node2
                            if remove_inconsistent_values(x_i, x_j, domain_type="aparatos"):
                                for x_k in neighbors(x_i):
                                    aparatos_queue.append(Edge(x_k, x_j))
                                ac_3(csp, doctors_queue, pacient_dicc)


        if valid_solution(csp):
            return csp

        





# def backtracking_search(csp, doctors_queue=doctors_graph.edges, aparatos_queue=aparatos_graph.edges): # Returns solution/failure
#     return ac_3(csp, doctors_queue, aparatos_queue)

def backtracking_search(csp=pacientes_rel_doct_sala_apar.copy(), doctors_queue=edge_sort(), pacient_dicc=pacientes_rel_doct_sala_apar.copy()): # Returns solution/failure
    return ac_3(csp, doctors_queue, pacient_dicc)

for pacient,solution in backtracking_search().items():
    print("Proximo paciente")
    print(pacient.name)
    for doctor in solution.doctors:
        print(doctor.name)
    # print("aparatos")
    # for aparat in solution.apparatus:
    #     print(aparat.id)
# for edge in edge_sort():
#     print("Aristas")
#     print(edge.node1.name)
#     print(edge.node2.name)

# for item in doctors_graph.nodes:
#     print(item.name)
#     print("Vecinos")
#     for vecino in doctors_graph.neighbors(item):
#         print(vecino.name)
#     print("termine")


# print(backtracking_search(pacientes_rel_doct_sala_apar))
