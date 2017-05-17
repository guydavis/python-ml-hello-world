#!/usr/bin/env python3
"""Basic SciPY Hello-World to verify a successful installation."""
import argparse
import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt

def main():
    """ Compute the maximum of a Bessel function and plot it. """
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("--order", type=int, default=3, help="order of Bessel function")
    args = parser.parse_args()
    f = lambda x: -special.jv(args.order, x)
    sol = optimize.minimize(f, 1.0)
    x = np.linspace(0, 10, 5000)
    plt.plot(x, special.jv(args.order, x), '-', sol.x, -sol.fun, 'o')
    plt.show() # Displays the image in matplotlib window

if __name__ == "__main__":
    main()
