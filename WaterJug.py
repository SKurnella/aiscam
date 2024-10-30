from collections import deque
from math import gcd

def is_valid_state(state, X, Y):
    return 0 <= state[0] <= X and 0 <= state[1] <= Y

def bfs(X, Y, Z):
    visited = set()
    queue = deque([(0, 0)])  
    parent = {}  

    while queue:
        a, b = queue.popleft()

        if a == Z or b == Z:
            path = []
            while (a, b) != (0, 0):
                path.append((a, b))
                a, b = parent[(a, b)]
            path.append((0, 0))
            path.reverse()
            return path
        
        if (a, b) in visited:
            continue
        visited.add((a, b))

        next_states = [
            (X, b),
            (a, Y), 
            (0, b),
            (a, 0),
            (a - min(a, Y - b), b + min(a, Y - b)),
            (a + min(b, X - a), b - min(b, X - a)),
        ]

        for state in next_states:
            if is_valid_state(state, X, Y) and state not in visited:
                queue.append(state)
                parent[state] = (a, b)
    
    return None  

def water_jug_problem():
    while True:
        try:
            print("\nWelcome to the Water Jug Problem Solver!")
            print("To exit, type 'exit' at any prompt.")
            X_input = input("Enter the capacity of Jug 1: ")
            if X_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
            X = int(X_input)
            if X <= 0:
                print("Capacities and target must be non-negative integers ans non zero. Please try again.")
                continue
            Y_input = input("Enter the capacity of Jug 2: ")
            if Y_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
            Y = int(Y_input)
            if Y <= 0:
                print("Capacities and target must be non-negative integers. Please try again.")
                continue
            Z_input = input("Enter the target amount of water: ")
            if Z_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
            Z = int(Z_input)
            if X <= 0 or Y <= 0 or Z < 0:
                print("Capacities and target must be non-negative integers. Please try again.")
                continue
            if Z > max(X, Y):
                print("No solution possible since the target is greater than both jug capacities.")
                continue
            solution = bfs(X, Y, Z)

            if solution:
                print(f"\nSolution found to get exactly {Z} liters!")
                for step in solution:
                    print(f"Jug 1: {step[0]} liters, Jug 2: {step[1]} liters")
            else:
                print(" No solution exists for the given inputs.")
        
        except ValueError:
            print("Error: Invalid input. Please enter valid integers for jug capacities and the target amount.")
water_jug_problem()