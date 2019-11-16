import numpy as np
import matplotlib.pyplot as plt


def populate_data():
    for i in range(0, 30):
        my_samples.append(i)
        my_linear.append(i)
        my_quadratic.append(i ** 2)
        my_cubic.append(i ** 3)
        my_exponential.append(1.5 ** i)


def plots():
    plt.figure('lin')
    plt.xlabel('sample points')
    plt.ylabel('linear function')
    plt.ylim(0, 1000)
    plt.plot(my_samples, my_linear)
    plt.figure('quad')
    plt.plot(my_samples, my_quadratic)
    plt.figure('cube')
    plt.title('Cubic')
    plt.plot(my_samples, my_cubic)
    plt.figure('expo')
    plt.title('Exponential')
    plt.plot(my_samples, my_exponential)
    plt.figure('quad')
    plt.ylabel('quadratic function')

    plt.figure('lin')
    plt.title('Linear')
    plt.figure('quad')
    plt.clf()  # clears any existing formatting
    plt.title('Quadratic')
    plt.plot(my_samples, my_quadratic)
    plt.ylim(0, 1000)
    plt.show()


def compare_graphs():
    plt.figure('lin quad')
    plt.clf()
    plt.plot(my_samples, my_linear, label='linear')
    plt.plot(my_samples, my_quadratic, label='quadratic')
    plt.title('Linear vs. Quadratic')
    plt.legend(loc='upper left')

    plt.figure('cube exp')
    plt.clf()
    plt.plot(my_samples, my_cubic)
    plt.plot(my_samples, my_exponential)
    plt.title('Cubic vs. Exponential')
    plt.show()


def plot_data_display():
    plt.figure('lin quad')
    plt.clf()
    plt.plot(my_samples, my_linear, 'b-', label='linear', linewidth=2.0)
    plt.plot(my_samples, my_quadratic, 'ro', label='quadratic', linewidth=3.0)
    plt.title('Linear vs. Quadratic')
    plt.legend(loc='upper left')

    plt.figure('cube exp')
    plt.clf()
    plt.plot(my_samples, my_cubic, 'g^', label='cubic', linewidth=4.0)
    plt.plot(my_samples, my_exponential, 'r--', label='exponential', linewidth=5.0)
    plt.legend()
    plt.title('Cubic vs. Exponential')
    plt.show()


def sub_plots():
    plt.figure('lin quad')
    plt.clf()
    plt.subplot(211)  # rows & columns 2 rows , 1 column, 1 which location to use
    plt.ylim(0, 900)
    plt.plot(my_samples, my_linear, 'b-', label='linear', linewidth=2.0)
    plt.subplot(212)
    plt.ylim(0, 900)
    plt.plot(my_samples, my_quadratic, 'r', label='quadratic', linewidth=3.0)
    plt.legend(loc= 'upper left')
    plt.title('Linear vs. Quadratic')

    plt.figure('cube exp')
    plt.clf()
    plt.subplot(121) # 1 row, 2 columns, 1 which location to use
    plt.ylim(0, 140000)
    plt.plot(my_samples, my_cubic, 'g--', label='cubic', linewidth=4.0)
    plt.subplot(122)
    plt.ylim(0, 140000)
    plt.plot(my_samples, my_exponential, 'r', label='exponential', linewidth=5.0)
    plt.legend()
    plt.title('Cubic vs. Exponential')

    plt.show()


def changing_scales():
    plt.figure('cube exp log')
    plt.clf()
    plt.plot(my_samples, my_cubic, 'g--', label='cubic', linewidth=2.0)
    plt.plot(my_samples, my_exponential, 'r', label='exponential', linewidth=4.0)
    plt.yscale('log')
    plt.legend()
    plt.title('Cubic vs. Exponential')

    plt.show()


if __name__ == '__main__':
    my_samples = []
    my_linear = []
    my_quadratic = []
    my_cubic = []
    my_exponential = []

    populate_data()

    # Plotting orders of growth

    # plots()
    # compare_graphs()
    # plot_data_display()
    # sub_plots()
    changing_scales()


