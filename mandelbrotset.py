import numpy as np
import matplotlib.pyplot as plt


def mandel_function_check(c, threshold):
    """

    :param c: Initial position in the complex plane
    :param threshold: The number of times z = z^2 + c needs to be executed in order to ensure the value doesn't diverge
    :return: The function's non-diverging limit
    """
    z = complex(0,0)
    for num in range(threshold):
        z = (z**2) + c
        if abs(z) > 2:
            break

    return num



def generate_mandelbrot_set(threshold,map_density):
    """
    Displays the mandelbrot set
    :param threshold: The number of times z = z^2 + c needs to be executed in order to ensure the value doesn't diverge
    :param map_density: Spread of Real and Complex plane
    :return:
    """

    real_num_plane = np.linspace(-2.25, 0.75, map_density)
    imag_num_plane = np.linspace(-1.5, 1.5, map_density)

    # Mandelmap represented as a 2D array [Length of Real number set x Length of imaginary number set]
    mandel_map = np.empty((len(real_num_plane),len(imag_num_plane)))

    for real_index,real_num in enumerate(real_num_plane):
        for imag_index,imag_num in enumerate(imag_num_plane):

            complex_num = complex(real_num,imag_num)
            mandel_map[real_index,imag_index] = mandel_function_check(complex_num,threshold)


    mandel_map = mandel_map.T
    plt.imshow(mandel_map, interpolation="nearest")
    plt.show()

generate_mandelbrot_set(120,1000)



