import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return y

# this is the initial condition y(0)=1

def euler_method(x=0, y=1, h=0.1):
    x_values = []
    y_values = []

    while x < 10:
        x_values.append(x)
        y_values.append(y)
        y = y + h * f(x, y)
        x = x + h

    plt.plot(x_values, y_values)
    plt.show()

if __name__ == "__main__":
    euler_method()
