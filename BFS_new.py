from collections import deque

def get_integer_input(prompt, error_message="Please enter a valid integer."):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print(error_message)

while True:
    while True:
        num_of_nodes = input("Enter the number of nodes: ")
        if num_of_nodes.isdigit():
            num_of_nodes = int(num_of_nodes)
            if num_of_nodes > 0:
                break
            else:
                print("Enter a positive integer greater than zero.")
        else:
            print("Please enter a valid integer.")

    while True:
        root_node = input("Enter the root node: ")
        if root_node.isdigit():
            root_node = int(root_node)
            break
        else:
            print("Please enter a valid integer.")

    nodes = [root_node]

    i = 0
    while len([x for x in nodes if x != '-']) < num_of_nodes:
        if nodes[i] != '-':
            children = input(f"Enter the child nodes for {nodes[i]} (separated by spaces")
            children = children.strip().split()
            if len(children) == 1:
                children.append('-')
            elif len(children) > 2:
                print("Please enter at most two children.")
                continue
            valid = all(child.isdigit() or child == '-' for child in children)
            if not valid:
                print("Please enter valid integers or '-' for no child.")
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

    def optimal_path(nodes, target):
        if nodes[0] == '-':
            return "Element not found" 
        queue = deque([(0, [])]) 
        visited = set()
        while queue:
            current_index, path = queue.popleft()
            if current_index in visited:
                continue
            visited.add(current_index)
            current_value = nodes[current_index]
            new_path = path + [current_value]
            if current_value == target:
                return new_path
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            if left_child_index < len(nodes) and nodes[left_child_index] != '-':
                queue.append((left_child_index, new_path))
            if right_child_index < len(nodes) and nodes[right_child_index] != '-':
                queue.append((right_child_index, new_path))
        return

    while True:
        key = input("Enter element to search: ")
        if key.isdigit():
            key = int(key)
            break
        else:
            print("Please enter a valid integer.")
    if key in nodes:
        print("Path found successfully")
        print("BFS path: ", end="")
        for ele in nodes:
            if ele != '-':
                print(f" --> {ele}", end="")
                if ele == key:
                    break
    else:
        print("Element not found in the tree.")

    path = optimal_path(nodes, key)
    if isinstance(path, list):
        print("\nOptimal path: ", end="")
        print(" --> ".join(map(str, path)))
    else:
        print(path)
    
    exit_code = input("Do you want to exit? (yes/no): ").strip().lower()
    if exit_code == "yes":
        break