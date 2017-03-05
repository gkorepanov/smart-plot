import matplotlib.pylab as plt
from   matplotlib import rc

import pandas as pd
import numpy as np
import statsmodels.api as sm

import warnings
from   IPython.display import display
import pickle


class Profile:
    """
    input = 'data.csv'

    Matplotlib inherited parameters
    scatter  =  dict(marker='o', color='r', markersize=7)
    linear   =  dict(linestyle='--', linewidth=0.5, color='k')
    grid     =  dict(linestyle='--', linewidth=0.2, color='#e2e2e2')

    Label
    label = {
        label: TODO,
        x: 0.05,
        y: 0.95,
        transform: TODO,
        bbox: TODO
    }


    Options
    rcParams = {
        'text.usetex': True,
        'text.latex.unicode': True,
        'text.latex.preamble': r"\usepackage[T2A]{fontenc}",
        'font.family': 'lmodern'
        'font.size': 20,
        'figure.figsize': (16, 9)
    }
    """

    __standard = ['gk']

    def __init__(self, preset='gk', bare=False):
        if not bare:
            self.load(preset)

    def load(self, preset):
        with open(preset + '.profile', 'rb') as file:
            self.__dict__.update(pickle.load(file))

    def save(self, filename, force=False):
        """filename of preset to be created or overrided,
        by default standard presets are not overrided"""

        if preset not in __standard or force:
            with open(filename, 'wb') as file:
                pickle.dump(self.__dict__, file)
        else:
            raise ValueError("Trying to override the standard preset")


smp.add(SubPlot(fsffsd))

class SmartPlot:
    class SubPlot:
        def __init__(
                self,
                data=profile.input,
                x=0, y=1,
                xerr=None,
                yerr=None,
                label=None, units='',
                settings=None
        ):
            """
            SubPlot(data='1', 0, 1, marker={'markersize': 3})
            SubPlot(data='2', marker={'marker' : 'x', 'color' : 'b'}, linear={'linewidth'=2})
            """


    def __init__(self):
        self.apply(Profile())
        self.__subplots = []

    def __getitem__(self, index):
        return __subplots[index]

    def apply(self, profile):
        self.profile = profile
        plt.rcParams.update(profile.rcParams)

    def add(self, *args, **kwargs):
        self.__subplots.append(self.SubPlot(*args, **kwargs))



























        if isinstance(data, str):
            self.data.append(pd.read_csv(data, engine='python', header=None))
        elif isinstance(data, pd.DataFrame) or isinstance(data, np.ndarray):
            self.data.append(data)
        else:
            raise NotImplementedError(type(data) + \
                                      " is not supported by smartplot")


        elif ()

        addplot._axes = _plt.subplots()[1]

        for count in range(number):
            addplot(input=input, xerr=xerr, yerr=yerr, number=None)

        # Destroy 'em'
        del addplot._row, addplot._data, addplot._axes
        return

    # Load data & calculate ranges
    x = np.array(addplot._data[  addplot._row  ])
    y = np.array(addplot._data[addplot._row + 1])

    xmin, xmax = min(addplot._data[  addplot._row  ]), max(addplot._data[  addplot._row  ])
    ymin, ymax = min(addplot._data[addplot._row + 1]), max(addplot._data[addplot._row + 1])

    addplot._row += 2

    if xerr:
        xerr  = np.array(addplot._data[addplot._row])
        addplot._row += 1
    if yerr:
        yerr  = np.array(addplot._data[addplot._row])
        addplot._row += 1

    # Fit
    t = sm.add_constant(x, prepend=False)
    model  = sm.OLS(y, t)
    result = model.fit()
    s,     i     = result.params
    s_err, i_err = result.bse

    # Show result
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        display(result.summary().tables[1])

    # Heuristics, starting from (0, 0) when not too much empty space
    def need_0(l, r):
        return True if (r > 0 and l > 0 and l/r < 0.2) else False

    if need_0(xmin, xmax) and need_0(ymin, ymax):
        xmin, ymin = 0, 0

    # Plot
    _plt.plot(x, y, linestyle='None', marker='o', color='r', markersize = 7)
    _plt.plot(np.linspace(xmin, xmax), np.linspace(xmin, xmax)*s + i, 'k--', linewidth=0.5)
    if xerr or yerr:
        _plt.errorbar(x, y, xerr=xerr, yerr=yerr)



    # Grid
    addplot._axes.grid(color='#e5e5e5', linestyle='--', linewidth=0.2)


def axes(xlabel=None, ylabel=None):
    _plt.xlabel(xlabel)
    _plt.ylabel(ylabel)


def show(output="graph.png", dpi=300, save=False):
    if save:
        _plt.savefig(
            output,
            dpi = dpi,
            bbox_inches = 'tight'  # Plot occupies maximum of available space
        )
    _plt.show()


def clear():
    _plt.cla()
    _plt.clf()
