def multiply(a, b):
    c = 0

    for i in range(len(a)):
        c += a[i] * b[i]

    return c

def test_inner_product():
    assert multiply([1, 2], [2, 2]) == 6
