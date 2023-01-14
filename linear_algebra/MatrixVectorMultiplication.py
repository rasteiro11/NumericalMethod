

def multiply(m, v):
    if len(m[0]) != len(v):
        print("Cannot multiply these")
        return 

    c = [] 
    for _ in range(len(v)):
        c.append(0)

    for i in range(len(v)):
        for j in range(len(v)):
          c[i] += m[i][j] * v[j]
        
    return c

def test_matrix_vector_multiplication():
    m = [
        [1, 2, -3],
        [2, 9 , 0],
        [6, -1, -2]
    ]

    v = [2, 3, -1]

    assert multiply(m, v) == [11, 31, 11]


    w = [
        [1, 2],
        [2, 9],
        [6, -1]
    ]

    v = [2, 3, -1]
    

    assert multiply(w, v) == None
