"""
class Repository
    commit(message, [filename]) -> commit_id
    log(start_id, end_id) -> prints the messages in order of stored in repo in the id range
    checkout(id) -> prints the filenames associated to the id
"""
import uuid

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Respository():

    def __init__(self):
        self.commits = {}
        self.commit_list = []

    def generate_commit_id(self):
        return uuid.uuid4()

    def add_to_list(self, commit_id):
        node = Node(commit_id)
        if len(self.commit_list) == 0:
            self.commit_list.append(node)
        last_commit = self.commit_list[-1]
        last_commit.next = node
        self.commit_list[-1] = node

    def commit(self, message, filenames):
        commit_id = self.generate_commit_id()
        commit_info = tuple([message, filenames])

        self.commits[commit_id] = commit_info
        self.add_to_list(commit_id)

        print(self.commits)

        return commit_id

    def get_range_of_commits(self, start_commit_id, end_commit_id):
        if not start_commit_id or not end_commit_id:
            return []

        node = self.commit_list[0]
        commits_to_select = []

        range_started = False
        while node:
            if node.data == start_commit_id:
                range_started = True
            elif node.data == end_commit_id:
                commits_to_select.append(node.data)
                break

            if range_started:
                commits_to_select.append(node.data)

            node = node.next

        return commits_to_select

    def log(self, start_commit_id, end_commit_id):
        commit_ids = self.get_range_of_commits(start_commit_id, end_commit_id)
        for commit_id, commit_info in self.commits.items():
            if commit_id in commit_ids:
                print(commit_info)

    def checkout(self, commit_id):
        commit = self.commits.get(commit_id, None)
        if not commit:
            return []
        return commit[1]


repo = Respository()
commit_id_1 = repo.commit("first commit", ["file1", "file2", "file3"])
commit_id_2 = repo.commit("second commit", ["file3"])
repo.log(commit_id_1, commit_id_2)
