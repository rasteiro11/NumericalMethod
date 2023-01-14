
from typing_extensions import override


class IMul:
    def mul(self, a, b):
        raise Exception("Must be overriden")

class Matrix(IMul):

    def __init__(self, i, j):
        c = []
        for _ in range(i):
            temp = []
            for _ in range(j):
                temp.append(0)
            c.append(temp)
        self.data = c

    def __repr__(self) -> str:
        return f"{self.data}"

    @override
    def mul(self, b):
        c = []
        for _ in range(len(self.data)):
            temp = []
            for _ in range(len(b[0])):
                temp.append(0)
            c.append(temp)

        for i in range(len(self.data)):
            for j in range(len(b[0])):
                for k in range(len(self.data[0])):
                    c[i][j] += self.data[i][k] * b[k][j]
        return c

    def set_data(self, m):
        self.data = m

        
if __name__ == "__main__":
    m = Matrix(2, 2)
    m.set_data([[1, 2],[3, 4]])

    b = [
        [1, 2],
        [3, 4]
    ]

    res = m.mul(b)

    print(res == [[7, 10], [15, 22]])
    
