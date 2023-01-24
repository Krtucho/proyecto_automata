colors={
    '0':'white',
    '1':'orage',
    '2':'grey',
    '3':'black',
    '4':'red',
    '5':'yellow'}

def read_origin(g):
    archive = open("Parsing/data/original-states.originals")
    text = ''
    line = archive.readline()
    while(line):
        if  line[:-1]== '[Original States Data]' or line[:-1] == '[Grid]'  :
            line = archive.readline()
        elif line[:-1] != '':
            if line[:-1] == '[States]':
                line = archive.readline()
                #l = l[:-1]
            if line == '[EOF]':
                print('Llegue')
                archive.close()
                break
            
            l = line[:-1]    
            l = l.split(':')
            id_color = l[1]
            l.pop(1)
            l = l[0].split(',')        
            x = l[0]
            y = l[1]
           # z = l[2]
            #text= x + y + z
            text= x + y 
            #g.add_node(text,x =int(x),y=int(y),z=int(z),color=colors[id_color])
            g.add_node(text,x =int(x),y=int(y),color=colors[id_color])
            g.nodes[text]['size'] = 40
        line = archive.readline() 
    archive.close()
    return text

def read(index,g):
    archive = open('data/'+str(index)+'.generation')
    resto = []
    add = 0
    text = ''
    line = archive.readline()
    pt_line = None
    id_color = None
    start = False
    while(line):
        l = line[:-1]
        if  l== '[Generation Data]' or l == '[Grid]'  or l == ' ':
            line = archive.readline()
        
        elif l == '[Tumors]' :
            line = archive.readline()
            id_color = '3'
            start= True
            
        elif l == '[Migra]':
            line = archive.readline()
            id_color = '4'
            start= True

        elif l == '[Micros]':
            line = archive.readline()
            id_color = '5'
            start= True
        else:
            pt_line = line.split(":")
            if start: 
                remove(pt_line,4)        
                start = False
            
            while len(pt_line):
                coma_line = pt_line[0].split(',')
                if len(resto):
                    for item in coma_line:
                        resto.append(item)
                    coma_line = resto
                    resto = []
                if len(coma_line)>=4:
                    x = coma_line[0]
                    y = coma_line[1]
                    #z = coma_line[2]
                    #text= x + y + z
                    text= x + y
                    #g.add_node(text,x =int(x),y=int(y),z=int(z),color=colors[id_color])
                    g.add_node(text,x =int(x),y=int(y),color=colors[id_color])
                else:
                    resto = coma_line
            pt_line.pop(0)    
                    
        line = archive.readline() 
    archive.close()
    return text

def remove(pt_line,n):
    k = 0
    while k<n:
        pt_line.pop(0)
        k= k+1 

def parser(index,graph):
    if index ==-1:
        read_origin(graph)
    else:
        read(index,read_origin)    
    

        