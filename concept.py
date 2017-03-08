import matplotlib.pyplot as plt
import pandas as pd


class Subplot:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def plot(self):
        plt.plot(self.x, self.y)


def plot(output=None, display=True, dpi=300):
    if not (output or display):
        raise UserWarning("All output methods are forbidden")

    for subplot in plot.list:
        subplot.plot()

    if output:
        plt.savefig(output, dpi=dpi, bbox_inches='tight')
    if display:
        plt.show()


def add(input, x=0, y=1):
    data = pd.read_csv(input, header=None)
    plot.list += [Subplot(data[x], data[y])]


def rm(id):
    del plot.list[id]


def clr():
    plot.list.clear()


def __init__(): pass
plot.list = []
