import numpy as np
from numpy import linalg as la

m = np.array([[5,2], [2, 2]])
w, v = la.eig(m)

print(v)


