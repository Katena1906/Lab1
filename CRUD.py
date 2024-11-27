class CRUD:
    def __init__(self, allowed_class):
        if not isinstance(allowed_class, type):
            raise TypeError(f"Not a class")
        self.__storage = []
        self.__current_id = 0
        self.__allowed_class = allowed_class


    def create(self, item):
        if not isinstance(item, self.__allowed_class):
            raise TypeError(f"It not object of {self.__allowed_class.__name__}.")
        self.__storage.append(item)
        self.__current_id += 1
        return item

    def read(self, index):
        if 0 <= index < len(self.__storage):
            return self.__storage[index]
        return None

    def update(self, index, item):
        if not isinstance(item, self.__allowed_class):
            raise TypeError(f"It not object of {self.__allowed_class.__name__}.")
        if 0 <= index < len(self.__storage):
            self.__storage[index] = item
            return True
        return False

    def delete(self, index):
        if 0 <= index < len(self.__storage):
            del self.__storage[index]
            return True
        return False

    def list(self):
        return self.__storage

