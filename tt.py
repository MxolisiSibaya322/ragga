import turtle as t
from queue import Queue
graph = []
max_y= 5
max_x = 5
def get_graph():
    
    for x_loop in range(-max_x,max_x+1):
        for y_loop in range(max_y,-max_y-1,-1):
            graph.append((x_loop,y_loop))
    
    

get_graph()


adjecency_matrix = {}
def get_neighbours():
    adjecency_matrix = {key :[] for key in graph }
    for location in adjecency_matrix.keys():
        x,y = location
        neighbours = []
        up = (x,y+1)
        if up in graph:
            neighbours.append(up)
        down = (x,y-1)
        if down in graph:
            neighbours.append(down)
        left = (x-1,y)
        if left in graph:
            neighbours.append(left)
        right = (x+1,y)
        if right in graph:
            neighbours.append(right)
        
        adjecency_matrix[location]= neighbours
    return adjecency_matrix

adjecency_matrix = get_neighbours()



final_matrix = {}
obs =[]


for key,value in adjecency_matrix.items():
    
    if len(value)>1:
        obs.append(value.pop(0))
    final_matrix[key]= value

print(obs)

box_size = 40
path = []
path = []
visited ={}
parent = {}
level = {}
path_finder =[]

def bfs (starting,end):
    
    queue = Queue()

    for location in final_matrix.values():
        for loc in location:
            visited[loc]= False
            parent[loc]= None
            level[loc] =-1



    

    visited[starting]=True
    level[starting]=0
    queue.put(starting)
    while not queue.empty():
        node = queue.get()
        path_finder.append(node)

        for neighbour in final_matrix[node]:

            if not visited[neighbour]:
                visited[neighbour] = True
                parent[neighbour] = node
                level[neighbour] = level[node]+1
                queue.put(neighbour)

    while end is not None:

        path.append(end)

        end = parent[end]
        
    path.reverse()

        

bfs((0,0),(5,-2))
def draw_cell(fill:bool):
    if fill:
        t.begin_fill()
        for i in range(4):
            t.fd(box_size)
            t.rt(90)
        t.end_fill()
    else:
        for i in range(4):
            t.fd(box_size)
            t.rt(90)
def build_maze():
    t.tracer(False)

    for location in graph:
        x,y = location
        x= (x)*box_size
        y =(y+1) * box_size
        t.penup()
        t.goto(x,y)
        t.pendown()
        
        fill= False
        if location in obs:
            fill = True
        draw_cell(fill)
        
    t.penup()
    t.home()
    t.goto(box_size//2,box_size//2)
    # print(t.pos())
    t.seth(90)
    t.tracer(True)
    t.exitonclick()



build_maze()
