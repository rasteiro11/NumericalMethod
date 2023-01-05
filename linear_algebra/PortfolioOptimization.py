import numpy as np
from GaussianElimination import gaussian_elimination;

if __name__ == "__main__":
    print(gaussian_elimination(
        np.array([[1., 1.], [0.035, 0.05]]),
                                        np.array([24000.0, 930.])))
