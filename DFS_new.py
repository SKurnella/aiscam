from collections import deque

while True:
    num_of_nodes = input("Enter the number of nodes (or type 'exit' to quit): ")
    if num_of_nodes.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        exit()
    if num_of_nodes.isdigit():
        if int(num_of_nodes) != 0:
            num_of_nodes = int(num_of_nodes)
            break
        else:
            print("Please enter a valid positive integer.")
    else:
        print("Please enter a valid integer.")

while True:
    root_node = input("Enter the root node (or type 'exit' to quit): ")
    if root_node.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        exit()
    if root_node.isdigit():
        root_node = int(root_node)
        break
    else:
        print("Please enter a valid integer.")

nodes = [root_node]
print("Enter the child nodes for each node. If there are no children, leave a space:")

i = 0
while True:
    valid_nodes = [x for x in nodes if x != '-']
    if len(valid_nodes) == num_of_nodes:
        break
    if len(valid_nodes) == num_of_nodes + 1:
        print(f"Limit reached, so extra node {nodes[-1]} is deleted.")
        nodes.pop()
        break
    if nodes[i] != '-':
        children = input(f"{nodes[i]} : ")
        if len(children) == 0:
            print("Please enter child nodes.")
            continue
        if not all(c.isalnum() or c.isspace() for c in children):
            print("Please enter only letters, digits, or spaces.")
            continue
        children = children.strip().split()
        if len(children) == 1:
            children.append('-')
        if len(children) > 2:
            print("Invalid input. Each node can have at most two children.")
            continue
        nodes += children
    else:
        nodes += ['-', '-']
    i += 1

for i in range(len(nodes)):
    if nodes[i] != '-' and str(nodes[i]).isdigit():
        nodes[i] = int(nodes[i])

def print_tree(nodes):
    max_level = 0
    while 2**max_level - 1 < len(nodes):
        max_level += 1
    for level in range(max_level):
        spaces = (2 ** (max_level - level - 1)) - 1
        space_between = (2 ** (max_level - level)) - 1
        line = " " * (spaces * 3)
        for i in range(2**level - 1, min(2**(level + 1) - 1, len(nodes))):
            if nodes[i] == '-':
                line += " " * 3
            else:
                line += f"{str(nodes[i]):^3}"
            line += " " * (space_between * 3)
        print(line)
        print()

print_tree(nodes)

def dfs(nodes, key, index=0):
    if index >= len(nodes) or nodes[index] == '-':
        return False
    print(f" --> {nodes[index]}", end="")
    if nodes[index] == key:
        return True
    if dfs(nodes, key, 2 * index + 1) or dfs(nodes, key, 2 * index + 2):
        return True
    return False

def optimal(nodes, key, index=0, path=None):
    if path is None:
        path = []
    if index >= len(nodes) or nodes[index] == '-':
        return False
    path.append(nodes[index])
    if nodes[index] == key:
        return True
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    if (left_child < len(nodes) and optimal(nodes, key, left_child, path)) or \
       (right_child < len(nodes) and optimal(nodes, key, right_child, path)):
        return True
    path.pop()
    return False

while True:
    key_input = input("Enter element to search (or type 'exit' to quit): ")
    if key_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        exit()
    if key_input.isdigit():
        key = int(key_input)
        break
    else:
        print("Please enter a valid integer.")

print("DFS path:", end="")
if not dfs(nodes, key):
    print("\nElement not found.")

path = []
if optimal(nodes, key, path=path):
    print("\nOptimal path:", " --> ".join(map(str, path)))
else:
    print("Element not found.")