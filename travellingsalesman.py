from itertools import permutations


def travellingSalesmanProblem(graph, s):

    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)

    min_path_cost = float('inf')
    min_path = None
    next_permutation = permutations(vertex)
    all_paths = {}
    for i in next_permutation:
        current_path = tuple([s] + list(i) + [s])
        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        if min_path_cost > current_pathweight:
            min_path_cost = current_pathweight
            min_path = current_path

        all_paths[current_path] = current_pathweight

    all_paths.pop(min_path)

    return {min_path: min_path_cost}, all_paths


def get_user_input():
    num_nodes = int(input("Enter Number of nodes: "))
    directionl = input("Is the graph directed? (y/n): ")

    distances = [[0] * num_nodes for _ in range(num_nodes)]

    if directionl == "y":
        for i in range(num_nodes):
            print(f"Node {i+1}: ")
            for j in range(num_nodes):
                if i == j:
                    distances[i][j] = 0
                else:
                    distance = input(f"{i+1} -> {j+1} (just press enter if there is no path)): ")
                    distances[i][j] = 0 if distance == "" else int(distance)
    else:
        for i in range(num_nodes):
            print(f"Node {i+1}: ")
            for j in range(i, num_nodes):
                if i == j:
                    distances[i][j] = 0
                else:
                    distance = input(f"{i+1} -> {j+1} (just press enter if there is no path)): ")

                    distances[i][j] = 0 if distance == "" else int(distance)
                    distances[j][i] = distances[i][j]

    start_node = int(input("Enter the start node: ")) - 1

    return distances, start_node


def display_solution(min, rest):
    result = "Best solution:\n"
    result += "Path: " + " -> ".join([str(node + 1)
                                     for node in list(min.keys())[0]]) + "\t"
    result += "Cost: " + str(list(min.values())[0]) + "\n\n"

    result += "Other possible solutions:\n"
    for path in rest.items():
        result += "Path: " + \
            " -> ".join([str(node + 1) for node in path[0]]) + "\t"
        result += "Cost: " + str(path[1]) + "\n"

    print(result)


display_solution(*travellingSalesmanProblem(*get_user_input()))
