import sys
from collections import deque

class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.value = sys.maxint
        self.heurivalue = sys.maxint

f = open('input.txt','r')
graph = {}
algo = f.readline().rstrip()
start = f.readline().rstrip()
end = f.readline().rstrip()
live_num = int(f.readline())

for i in range(live_num):
    live_traffic = f.readline().split(' ')
    if graph.get(live_traffic[0], None) == None:
        graph[live_traffic[0]] = []
    graph[live_traffic[0]].append((live_traffic[1], int(live_traffic[2])))

heuri_dict = {}
heuri_num = int(f.readline())

for i in range(heuri_num):
    heuri_input = f.readline().split(' ')
    heuri_dict[heuri_input[0]] = int(heuri_input[1])

if start == end:
    output = open('output.txt', 'w')
    output.write(start + " " + str(0) +"\n")
    output.close()
    exit(0)
if graph == {}:
    output = open('output.txt', 'w')
    output.close()
    exit(0)

def bfs(graph, start, end):
    queue = []
    queue.append([start.name])
    visited = []
    while queue:
        path = queue.pop(0)
        nodename = path[-1]
        if nodename == end.name:
            return path
        for adjacent in graph.get(nodename, [])[:]:
            #why list here
            new_path = list(path)
            if adjacent != []:
                #in case of loops
                if adjacent[0] not in new_path:
                    new_path.append(adjacent[0])
                else:
                    continue
            queue.append(new_path)
        # print path

def dfs(graph, start, end):
    if start.name == end.name:
        return start
    visited = set()
    open_stack = [start]
    #print start.name
    while open_stack != []:
        p_node = open_stack.pop()
        visited.add(p_node.name)
        if p_node.name == end.name:
            return p_node
        children = graph.get(p_node.name, [])[:]
        children.reverse()
        for child in children:
            child_node = Node(child[0])
            child_node.parent = p_node
            if child_node.name not in [open_node.name for open_node in open_stack] \
                    and child_node.name not in visited:
                open_stack.append(child_node)
    return None

#start and end are nodes
def ucs(graph, start, end):
    start.value = 0
    visited = []
    open_queue = [start]
    while True:
        if open_queue == []:
            return None
        open_queue.sort(key=lambda x:x.value)
        min_node = open_queue.pop(0)
        if min_node.name == end.name:
            visited.append(min_node)
            return min_node
        #children is a list of tuples(name, distance to min_node)
        children = graph.get(min_node.name,[])[:]
        children.sort(key=lambda x:x[1])
        while children != []:

            #init the child node
            child = children.pop(0)
            child_node = Node(child[0])
            child_node.parent = min_node
            child_node.value = min_node.value + child[1]

            visited_name = [visitnode.name for visitnode in visited]
            open_name = [opennode.name for opennode in open_queue]

            if child[0] not in visited_name + open_name:
                open_queue.append(child_node)

            #could child in both open and closed?
            elif child[0] in open_name:
                index = open_name.index(child[0])
                if child_node.value < open_queue[index].value:
                    open_queue.pop(index)
                    open_queue.append(child_node)

            elif child[0] in visited_name:
                index = visited_name.index(child[0])
                if child_node.value < visited[index].value:
                    visited.pop(index)
                    open_queue.append(child_node)
        # visited[min_item[0]] = min_item[1]
        visited.append(min_node)

def astar(graph, start, end):
    start.value = 0
    start.heurivalue = heuri_dict[start.name]
    visited = []
    open_queue = [start]
    while True:
        if open_queue == []:
            return None
        # print [opennode.name for opennode in open_queue]
        open_queue.sort(key=lambda x:x.heurivalue)
        min_node = open_queue.pop(0)

        if min_node.name == end.name:
            visited.append(min_node)
            return min_node

        #children is a list of tuples(name, distance to min_node)
        children = graph.get(min_node.name,[])[:]
        # children.sort(key=lambda x:x[1])

        while children != []:
            #init the child node
            child = children.pop(0)
            child_node = Node(child[0])
            child_node.parent = min_node
            child_node.value = min_node.value + child[1]
            child_node.heurivalue = child_node.value + heuri_dict[child_node.name]

            # if child_node.heurivalue < min_node.heurivalue:
            #     child_node.heurivalue = min_node.heurivalue

            visited_name = [visitnode.name for visitnode in visited]
            open_name = [opennode.name for opennode in open_queue]

            if child[0] not in visited_name + open_name:
                open_queue.append(child_node)

            #could child in both open and closed?
            elif child[0] in open_name:
                index = open_name.index(child[0])
                if child_node.heurivalue < open_queue[index].heurivalue:
                    open_queue.pop(index)
                    open_queue.append(child_node)

            elif child[0] in visited_name:
                index = visited_name.index(child[0])
                if child_node.heurivalue < visited[index].heurivalue:
                    visited.pop(index)
                    open_queue.append(child_node)

        # visited[min_item[0]] = min_item[1]
        visited.append(min_node)

output = open('output.txt', 'w')

if algo == "BFS":
    iter = 0
    result = bfs(graph, Node(start), Node(end))
    if result != None:
        for i in bfs(graph, Node(start), Node(end)):
            output.write(i + " " + str(iter) + "\n")
            # print(i + " " + str(iter))
            iter += 1

elif algo == "DFS":
    iter = 0
    endnode = dfs(graph, Node(start), Node(end))
    if endnode != None:
        node_list = []
        while endnode != None and endnode.parent != None :
            node_list.append(endnode)
            endnode = endnode.parent
        node_list.append(endnode)
        node_list.reverse()
        iter = 0
        for node in node_list:
            output.write(node.name + " " + str(iter) + "\n")
            # print(node.name + " " + str(iter))
            iter += 1

elif algo == "UCS":
    endnode = ucs(graph, Node(start), Node(end))
    if endnode != None:
        node_list = []
        while endnode != None and endnode.parent != None:
            node_list.append(endnode)
            endnode = endnode.parent
        node_list.append(endnode)
        node_list.reverse()
        for node in node_list:
            output.write(node.name + " " + str(node.value) + "\n")
            # print(node.name + " " + str(node.value))

elif algo == "A*":
    endnode = astar(graph, Node(start), Node(end))
    if endnode != None:
        node_list = []
        while endnode != None and endnode.parent != None:
            node_list.append(endnode)
            endnode = endnode.parent
        node_list.append(endnode)
        node_list.reverse()
        for node in node_list:
            output.write(node.name + " " + str(node.value) + "\n")
            # print(node.name + " " + str(node.value))

output.close()
