from Queue import *
from mazegen import *
import time
import random
from sys import setrecursionlimit
setrecursionlimit(5000)
#rec_flag=True
size=50
maze = GrowingTree(size)
maze.generate_maze()
depth_dict={}
parent_dict={}

def bfs(maze):
    sorted_maze=[]
    sorted_maze = sorted(maze.tree)
    for n in sorted_maze:
        depth_dict[n] = -1
        parent_dict[n] = -1
    root=sorted_maze[0]
    depth_dict[root] = 0
    parent_dict[root] = 'God'
    Q = Queue()
    Q.put(root)

    while Q.qsize():
            current = Q.get()
            if current!=(maze.size-1,maze.size-1):
                for n in neighbour(current):
                    if depth_dict[n] == -1:# if it is a unvisited node
                        depth_dict[n] = depth_dict[current]+ 1
                        parent_dict[n] = current
                        #global bfs_nodes
                        #bfs_nodes = bfs_nodes+1
                        Q.put(n)
            else: return trace(current)
def trace(node):
    #print 'Found'
    n=['Goal',node]
    m=node
    while n[-1]!='God':
        n.append(parent_dict[m])
        m=parent_dict[m]
    #print 'Used nodes: BFS',
    print n
    return n
def neighbour(node):
    neighbours=[]
    legit_moves=list(set(maze.get_classes_for_node(node).split()))
    #print legit_moves
    for n in legit_moves:
        if n =='W':neighbours.append((node[0],node[1]+1))
        if n =='E':neighbours.append((node[0],node[1]-1))
        if n =='S':neighbours.append((node[0]+1,node[1]))
        if n =='N':neighbours.append((node[0]-1,node[1]))
    return neighbours
def solution_to_java(solv_list):
    solv=[]
    solv=solv_list[1:-1]
    solv.reverse()
    js='''
    <button onclick="myFunction()">Run Solution</button>
    <script>
    async function myFunction() {

    '''
    for n in range(len(solv)):
        if n+1 > len(solv)-1 : break
        if solv[n+1][0]>solv[n][0]: js+='MAZE.moveDown();\n'
        if solv[n + 1][0] < solv[n][0]: js+='MAZE.moveUp();\n'
        if solv[n + 1][1] > solv[n][1]: js+='MAZE.moveRight();\n'
        if solv[n + 1][1] < solv[n][1]: js+='MAZE.moveLeft();\n'
    js+='''}</script>'''
    return js
def insert_js(content,filename):
    f = open(filename, mode='a')
    #from renderer import render_static_html
    #result = render_static_html(self)
    f.write(content)
    f.close()
def sleep_in_js(filename):
    f = open(filename, mode='a')
    #from renderer import render_static_html
    #result = render_static_html(self)
    f.write(
        '''<script>function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms));}</script>'''
    )
    f.close()
def recursive_dfs(node):
    global dfs_nodes
    dfs_nodes=dfs_nodes+1
    if node==(maze.size-1,maze.size-1):
        #print 'Done'
        return
    nodes_set=[]
    nodes_set=neighbour(node)
    #time.sleep(1)
    rnd=0
    rnd=random.SystemRandom().randint(0, len(nodes_set)-1)

    #print neighbour(node)[rnd]
    recursive_dfs(neighbour(node)[rnd])
    return
def chebydis(node):
    return (abs(node[0] - maze.size + 1) + abs(node[1] - maze.size+1))-(maze.size-1-node[0])
def heuristic(node):
    #print len(list(set(maze.get_classes_for_node(node).split())))
    return -len(list(set(maze.get_classes_for_node(node).split())))
    #return chebydis(node)+offset
    #return (abs(node[0] - maze.size + 1) + abs(node[1] - maze.size+1))
def a_star_search(start,goal):
    Q = PriorityQueue()
    Q.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while Q.qsize():
        current = Q.get()
        if current == goal:
            break
        for next in neighbour(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next)
                Q.put(next, priority)
                global nodes_count
                nodes_count=nodes_count+1
                #print nodes_count
                came_from[next] = current
    print 'Used nodes: A*',nodes_count
    return came_from
def trace_a_star(dict_came_from):
    new=(maze.size-1,maze.size-1)
    new_node=[new]
    #print 'n'
    while new_node[-1]!=(0,0):
        new=dict_came_from[new]
        #print 't'
        new_node.append(new)
        #print new_node
    #rst=new_node.reverse()
    return new_node


#print trace_a_star(a_star_search(sorted(maze.tree)[0],(maze.size-1,maze.size-1)))
#bfs(maze)
#global nodes__count
#global bfs_nodes
#global dfs_nodes
#for time in range(5):
    #print heuristic(sorted(maze.tree)[0])
#maze = GrowingTree(size)
#maze.generate_maze()
    #print heuristic(sorted(maze.tree)[0])
#    for offset in range(5):
        #print heuristic(sorted(maze.tree)[0])
#        nodes_count =0
#        dfs_nodes=0
#        bfs_nodes=0
#        a_star_search(sorted(maze.tree)[0],(maze.size-1,maze.size-1))
#bfs(maze)
#    print '==================='
#// DO NOT TOUCH
maze.draw_maze('t1.html')
#recursive_dfs(sorted(maze.tree)[0])
#print 'Used nodes: DFS',dfs_nodes
#sleep_in_js('t1.html')
insert_js(solution_to_java(bfs(maze)),'t1.html')
#sleep_in_js('t1.html')


