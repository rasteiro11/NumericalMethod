import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*x

def df(x):
    return 2*x

# gradient descent algorithm - n is the number of iterations
# alpha is the learning rate
def gradient_descent(start, end, n, alpha):
    # we track the results (x and f(x) values as well)
    x_values = []
    y_values = []

    # generate a random starting point (initial location)
    x = np.random.uniform(start, end)

    for i in range(n):
        # this is the gradient descent formula (based on the derivative)
        x = x - alpha*df(x)
        # we store x and f(x) values
        x_values.append(x)
        y_values.append(f(x))
        print(f"#{i} f({f(x)}) = {x}")

    return [x_values, y_values]

if __name__ == "__main__":
   solutions, scores = gradient_descent(-1, 1, 50, 0.1) 

   inputs = np.arange(-1, 1.1, 0.1)

   # create a line plot of input vs result
   plt.plot(inputs, f(inputs))

   # this is how we plot the steps of the algorithm
   plt.plot(solutions, scores, '.-', color='green')
   plt.show()

