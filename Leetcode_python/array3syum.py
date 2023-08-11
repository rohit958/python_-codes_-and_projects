class Container:
    def __init__(self, index, a, b):
        self.index = index
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a < other.a

def main():
    n, k = map(int, input().split())  # Number of containers, Number of distinct balls needed
    containers = []

    for i in range(n):
        a, b = map(int, input().split())  # Cost of opening container, Cost of each ball
        containers.append(Container(i + 1, a, b))

    containers.sort()

    cost = 0
    selected_balls = set()

    for container in containers:
        if len(selected_balls) >= k:
            break

        cost += container.a

        for i in range(1, k - len(selected_balls) + 1):
            if i not in selected_balls:
                selected_balls.add(i)
                cost += container.b

    print(cost)

if __name__ == "__main__":
    main()