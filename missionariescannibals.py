class State:
    def __init__(self, lm, lc, b, rm, rc):
        self.lm, self.lc, self.b, self.rm, self.rc = lm, lc, b, rm, rc

    def is_valid(self, tm, tc):
        return (
            0 <= self.lm <= tm and
            0 <= self.lc <= tc and
            0 <= self.rm <= tm and
            0 <= self.rc <= tc and
            (self.lm == 0 or self.lc <= self.lm) and
            (self.rm == 0 or self.rc <= self.rm)
        )

    def is_goal(self):
        return self.lm == self.lc == 0

    def __eq__(self, other):
        return (self.lm, self.lc, self.b, self.rm, self.rc) == \
               (other.lm, other.lc, other.b, other.rm, other.rc)

    def __hash__(self):
        return hash((self.lm, self.lc, self.b, self.rm, self.rc))

def successors(state, tm, tc):
    children = []
    ob = "left" if state.b == "right" else "right"
    
    for m in range(tm + 1):
        for c in range(tc + 1):
            if 0 < m + c <= 2:  # Assuming bc is always 2 as per your code
                new_state = State(
                    state.lm + (-1 if state.b == "left" else 1) * m,
                    state.lc + (-1 if state.b == "left" else 1) * c,
                    ob,
                    state.rm + (1 if state.b == "left" else -1) * m,
                    state.rc + (1 if state.b == "left" else -1) * c,
                )
                if new_state.is_valid(tm, tc):
                    children.append((new_state, (m, c)))
    return children

def print_boat_contents(m, c):
    print(f"Missionaries and cannibals on boat: {m}M {c}C")

def dfs(initial_state, tm, tc):
    visited, stack = set(), [(initial_state, [])]

    while stack:
        state, path = stack.pop()
        if state.is_goal():
            return path + [state]
        if state not in visited:
            visited.add(state)
            children = successors(state, tm, tc)
            stack.extend((child_state, path + [(child_state, boat_contents)]) for child_state, boat_contents in children)

def print_path(path):
    for i, (state, boat_contents) in enumerate(path):
        print(f"Step {i + 1}:")
        l, r = ("Left", "Right") if state.b == "left" else ("Right", "Left")
        if l=='left':
            print(f"{l}: {state.lm}M {state.lc}C => boat is on {state.b}")
            print(f"{r}: {state.rm}M {state.rc}C")
        else:
            print(f"{l}: {state.rm}M {state.rc}C => boat is on {state.b}")
            print(f"{r}: {state.lm}M {state.lc}C")
        print_boat_contents(*boat_contents)
        print()
        if state.lm == 0 and state.lc == 0:
            return

if __name__ == "__main__":
    tm = int(input("Enter the total number of missionaries: "))
    tc = int(input("Enter the total number of cannibals: "))
    bc = 2
    
    if tm == tc:
        initial_state = State(tm, tc, "left", 0, 0)
        solution_path = dfs(initial_state, tm, tc)
        
        if solution_path:
            print("Solution found!\n")
            print("Step 0:")
            print(f"Left: {tm}M {tc}C")
            print("Right: 0M 0C\n")
            print_path(solution_path)
        else:
            print("No solution found.")
    else:
        print("Solution not possible")
 