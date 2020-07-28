
def print_lineage_with_cost(parents, costs):
    steps = ["finish"]
    while steps[-1] != 'start':
        steps.append(parents[steps[-1]])
    print(steps[::-1], sep=" -> ")

def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def dijkstra(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    print_lineage_with_cost(parents, costs)
    print(f"shortest path cost: {costs['finish']}")

if __name__ == "__main__":
    """
    # Graph 1
    """
    graph1 = {
        "start": {"A": 6, "B": 2},
        "A": {"finish": 1},
        "B": {"A": 3, "finish": 5},
        "finish": {}
    }
    costs1 = {
        "A": 6,
        "B": 2,
        "finish": float("inf")
    }
    parents1 = {
        "A": "start",
        "B": "start",
        "finish": None
    }
    dijkstra(graph1, costs1, parents1)

    """
    # Graph 2
    """
    graph2 = {
        "start": {"A": 5, "B": 2},
        "B": {"A": 8, "D": 7},
        "A": {"C": 4, "D": 2},
        "C": {"D": 6, "finish": 3},
        "D": {"finish": 1},
        "finish": {}
    }
    costs2 = {
        "A": 5,
        "B": 2,
        "C": float("inf"),
        "D": float("inf"),
        "finish": float("inf")
    }
    parents2 = {
        "A": "start",
        "B": "start",
        "C": None,
        "D": None,
        "finish": None
    }
    dijkstra(graph2, costs2, parents2)

    """
    # Graph 3
    """
    graph3 = {
        "start": {"A": 10},
        "A": {"B": 20},
        "B": {"C": 1, "finish": 30},
        "C": {"A": 1},
        "finish": {}
    }
    costs3 = {
        "A": 10,
        "B": float("inf"),
        "C": float("inf"),
        "finish": float("inf")
    }
    parents3 = {
        "A": "start",
        "B": None,
        "C": None,
        "finish": None
    }
    dijkstra(graph3, costs3, parents3)
