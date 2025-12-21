# memory/session_memory.py

class SessionMemory:
    def __init__(self):
        self.data = {}

    def update(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def is_complete(self):
        return all(k in self.data for k in ["age", "income", "state"])

    def clear(self):
        self.data = {}

memory = SessionMemory()
