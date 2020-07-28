from collections import deque

def is_a_seller(person):
    return person[-1] == 's'

def breadth_first_search(graph):
    friends = deque()
    friends += graph["you"]

    searched = []
    while friends:
        friend = friends.popleft()
        if friend not in searched:
            if is_a_seller(friend):
                return friend
            else:
                friends += graph[friend]
                searched.append(friend)
    return None

graph = {
    "you": ["vijay", "antony", "geo"],
    "antony": ["jack"],
    "vijay": ["sam", "justin"],
    "geo": ["jack", "mark"],
    "sangeeth": [],
    "jesus": [],
    "mark": [],
    "joe": [],
}

if __name__ == "__main__":
    print(breadth_first_search(graph))
