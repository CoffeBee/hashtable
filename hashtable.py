#pylint: disable=R0903
'''Hash table modula'''
class HashTableError(Exception):
    '''Hash table Error class'''
    pass


class HashTable:
    '''Hash table class'''
    def __init__(self):
        self._data = [[] for i in range(1 << 17)]
        self.__size = 2
        self.__count = 0

    def __len__(self):
        return self.__count

    def size(self):
        '''Get size method'''
        return self.__size

    def __iter__(self):
        return HashTableIterator(self._data)

    def __contains__(self, key):
        return (key, key) in self._data[hash(key) % self.__size]

    def add(self, key):
        '''Add element method'''
        if self.check(key):
            return
        if self.__count * 1.5 >= self.__size:
            self.__size *= 2
            newdata = [[] for i in range(self.__size)]
            for i in self._data:
                for j in i:
                    newdata[hash(j[0]) % self.__size].append(j)
            self._data = newdata
        val = key
        try:
            if self._data[hash(key) % self.__size] in (key, val):
                return
            self.__count += 1
            self._data[hash(key) % self.__size].append((key, val))
        except:
            raise HashTableError("Unhashable type")

    def check(self, key):
        '''Check element method'''
        try:
            for i in self._data[hash(key) % self.__size]:
                if i[0] == key:
                    return True
            return False
        except:
            raise HashTableError("Unhashable type")

    def remove(self, key):
        '''Remove element method'''
        if self.__count * 3 < self.__size:
            self.__size //= 2
            newdata = [[] for i in range(self.__size)]
            for i in self._data:
                for j in i:
                    newdata[hash(j[0]) % self.__size].append(j)
            self._data = newdata
        try:
            for i in self._data[hash(key) % self.__size]:
                if i[0] == key:
                    self.__count -= 1
                    self._data[hash(key) % self.__size].remove(i)
                    break
        except:
            raise HashTableError("Unhashable type")


class HashTableIterator:
    '''Hash table iterator class'''
    def __init__(self, table):
        self.__table = table
        self._indexi = 0
        self._indexj = 0

    def __next__(self):
        if self._indexi == len(self.__table):
            raise StopIteration
        while self._indexj == len(self.__table[self._indexi]):
            self._indexj = 0
            self._indexi += 1
            if self._indexi == len(self.__table):
                raise StopIteration
        ans = self.__table[self._indexi][self._indexj]
        self._indexj += 1
        return ans[0]
