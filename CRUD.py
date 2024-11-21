class CRUD:
    def __init__(self, allowed_class):
        if not isinstance(allowed_class, type):
            raise TypeError(f"Not a class")
        self._storage = []
        self._allowed_class = allowed_class

    def create(self, item):
        if not isinstance(item, self._allowed_class):
            raise TypeError(f"It not object of {self._allowed_class.__name__}.")
        self._storage.append(item)
        return item

    def read(self, index):
        if 0 <= index < len(self._storage):
            return self._storage[index]
        return None

    def update(self, index, item):
        if not isinstance(item, self._allowed_class):
            raise TypeError(f"It not object of {self._allowed_class.__name__}.")
        if 0 <= index < len(self._storage):
            self._storage[index] = item
            return True
        return False

    def delete(self, index):
        if 0 <= index < len(self._storage):
            del self._storage[index]
            return True
        return False

    def list(self):
        return self._storage