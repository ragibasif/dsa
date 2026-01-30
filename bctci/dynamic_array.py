class DynamicArray:
    def __init__(self):
        self._sz = 0
        self._cap = 64
        self._buf = [None] * self._cap

    def __expand(self):
        self._cap <<= 1
        buf = [None] * self._cap
        for i in range(len(self._buf)):
            buf = self._buf[i]
        buf,self._buf = self._buf,buf

    def __shrink(self):
        self._cap >>= 1
        buf = [None] * self._cap
        for i in range(len(self._buf)):
            buf = self._buf[i]
        buf,self._buf = self._buf,buf

    def __is_valid(self,i,low=0,high=self._sz):
        return i >= low and i < high

    def __str__(self):
        return str(self._buf[:self._sz])

    def append(self,x):
        """
        Worst-case time: O(N)
        Amortized time: O(1)
        """
        if self._sz + 1 >= self._cap:
            self.__expand()
        self._buf[self._sz] = x
        self._sz += 1
    def get(self,i):
        if not self.__is_valid(i):
            raise IndexError("Out of bounds")
        return self._buf[i]
    def set(self,i,x):
        if not self.__is_valid(i):
            raise IndexError("Out of bounds")
        self._buf[i] = x
    def size(self):
        return self._sz
    def pop_back(self):
        """
        Worst-case time: O(N)
        Amortized time: O(1)
        """
        if not self._sz > 0:
            raise IndexError("Pop from empty array")
        self._sz -= 1
        if self._sz / self._cap < 0.25 and self._cap > 64:
            self.__shrink()
        return self._buf[self._sz]
    def pop(self,i):
        if not self.__is_valid(i):
            raise IndexError("Out of bounds")
        ret = self._buf[i]
        for j in range(i,self._sz-1):
            self._buf[j] = self._buf[j+1]
        self.pop_back()
        return ret
    def contains(self,x):
        for i in range(self._sz):
            if self._buf[i] == x:
                return True
        return False
    def insert(self,i,x):
        if not self.__is_valid(i,high=self._sz+1):
            raise IndexError("Out of bounds")
        self.append(x)
        for j in range(self._sz - 1, i,-1):
            self._buf[j] = self._buf[j-1]
        self._buf[i] = x
    def remove(self,x):
        pos = -1
        for i in range(self._sz):
            if self._buf[i] == x:
                pos = i
                for j in range(i,self._sz-1):
                    self._buf[j] = self._buf[j+1]
                break
        if pos == -1:
            return pos
        self.pop(pos)
        return pos


    

a = DynamicArray()
for i in range(20):
    a.append(i)
print(a)
print(a.size())
