def print_towers():
    for i, j in towers.items():
        print(i, ":", *j)


def tower_of_hanoi(n, source, auxiliary, destination):
    if "counter" not in dir(tower_of_hanoi): tower_of_hanoi.counter = 1
    if n == 1:
        towers[source].remove(1)
        towers[destination].append(1)
        print_towers()
        print(f"Step {tower_of_hanoi.counter}: Move disk 1 from source {source} to destination {destination}")
        tower_of_hanoi.counter += 1
        return
    
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    towers[source].remove(n)
    towers[destination].append(n)
    print_towers()
    print(f"Step {tower_of_hanoi.counter}: Move disk {n} from source {source} to destination {destination}")

    tower_of_hanoi.counter += 1
    
    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))
towers = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

tower_of_hanoi(n, 'A', 'B', 'C')
