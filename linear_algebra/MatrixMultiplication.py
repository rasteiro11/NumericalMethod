def multiply(a, b):
    if len(a[0]) != len(b):
        print("Not able to multiply")
        return
    else:
        c = []
        for _ in range(len(a)):
            temp = []
            for _ in range(len(b[0])):
                temp.append(0)
            c.append(temp)

        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    c[i][j] += a[i][k] * b[k][j]
        return c



def test_matrix_matrix_multiplication():
    # 4 x 2
    a = [
        [1, 2],
        [3, 4],
    ]
    
    # 2 x 3
    b = [
        [1, 2],
        [3, 4]
    ]
    
    print(a)
    print(b)
    
    
    print(len(a))
    print(len(b))

    assert multiply(a, b) == [[7, 10], [15, 22]]





