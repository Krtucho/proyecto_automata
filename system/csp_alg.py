doctors_graph = []
aparatos_graph = []

relations = {}

def domain(x_i):
    pass

def check_domain():
    for item in domains:
        if item.domain == None:
            return False
    return True

def delete_from_domain(x_i):
    pass

def remove_inconsistent_values(x_i, x_j): # returns true iff succeeds
    removed = False
    for x in domain[x_i]:
        if not :
            delete_from_domain(x_i)
            removed = True
    return removed

def neighbors(x_i):
    return doctors_graph.neighbors(x_i)

def ac_3(csp, doctors_queue, aparatos_queue): # returns the CSP, posibly with reduced domains
    # doctors_queue
    while len(doctors_queue) > 0:
        x_i, x_j = doctors_queue.pop()
        if remove_inconsistent_values(x_i, x_j, type="doctors"):
            for x_k in neighbors(x_i):
                doctors_queue.append((x_i, x_j))
        
        # aparatos_queue
        while len(aparatos_queue) > 0:
            x_i, x_j = aparatos_queue.pop()
            if remove_inconsistent_values(x_i, x_j, type="aparatos"):
                for x_k in neighbors(x_i):
                    aparatos_queue.append((x_i, x_j))

    if check_domain():
        return csp
    else:
        return None

def backtracking_search(csp): # Returns solution/failure
    return ac_3(csp, doctors_queue, aparatos_queue)