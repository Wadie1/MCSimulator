import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import montecarlo_simulation as mc


class Lec:

    def __init__(self):
        pass


def index(hist):
    for i in range(len(hist)):
        if hist[i] > 0:
            return i


# LEC plot
def plot_graph(result_losses_list, show_graph=True):
    """Plots the loss exceedance curve from a nparray of Monte Carlo results"""
    # fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    mcs = mc.MonteCarlo_simulation()
    result_array = np.array(result_losses_list)
    hist, edges = np.histogram(result_array, bins=40)
    cumrev = np.cumsum(hist[::-1])[::-1] * 100 / mcs.MC_COUNTER
    #plt.xscale('log')
    if show_graph:
        plt.plot(edges[:-1], cumrev, label='residual')
    else:
        plt.plot(edges[:-1], cumrev, label='inherent')
    plt.grid(which="both")
    plt.ylim(bottom=0, top=100)
    plt.xlim(left=edges[index(hist[1:])])
    #right = edges[-1]
    plt.legend()
    fig = plt.gcf()
    return fig
