import numpy as np

def gaussian_elimination(a, b):
    n = len(b)

    for k in range(n-1):
        # values below pivot value
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k:n] = a[i, k:n] - lam * a[k, k:n]
                b[i] = b[i] - lam * b[k]

    # back substitution
    for k in range(n-1, -1, -1):
       b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k+1:n])) / a[k, k]

    return b
    
if __name__ == "__main__":
    print(gaussian_elimination(
        np.array([[1., 1., -1.], [2., -1., 1.], [-1., 2., 2.]]),
                                        np.array([-2., 5., 1.])))
