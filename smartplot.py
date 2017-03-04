import matplotlib.pylab as _plt
from   matplotlib import rc
import pandas as pd
import numpy as np
import statsmodels.api as sm
import warnings
from   IPython.display import display


# Options
params = {
    'text.usetex'         : True,
    'text.latex.unicode'  : True,
    'text.latex.preamble' : r"\usepackage[T2A]{fontenc}",
    'font.size'           : 20,
    'font.family'         : 'lmodern',
    'figure.figsize'      : (16, 9),
    }

_plt.rcParams.update(params)

# Get fig, ax
_fig, _ax = _plt.subplots()
_res = _plt.gcf()


def addplot(
        input  = "data.csv",
        units  = "",
        label  = None,
        labelx = 0.05,
        labely = 0.9,
        xerr   = None,
        yerr   = None,
        number = 1
        ):

    # Set attribute (static)
    try:
        addplot._row
    except AttributeError:
        addplot._row = 0

    # Recursive wrapper
    if number:
        for count in range(number):
            addplot(input=input, xerr=xerr, yerr=yerr, number=None)
        addplot._row = 0
        return

    # Load data
    data = pd.read_csv(input, engine='python', header=None)

    # Extract arrays
    x = np.array(data[  addplot._row  ])
    y = np.array(data[addplot._row + 1])
    addplot._row += 2

    if xerr:
        xerr  = np.array(data[addplot._row])
        addplot._row += 1
    if yerr:
        yerr  = np.array(data[addplot._row])
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

    # Calculate ranges
    xmin = min(data[0])
    xmax = max(data[0])
    ymin = min(data[1])
    ymax = max(data[1])

    # Heuristics, starting from 0 is more beautiful when
    # there is not too much empty space
    def need_0(l, r):
        return True if (r > 0 and l > 0 and l/r < 0.2) else False

    if need_0(xmin, xmax):
        xmin = 0

    if need_0(ymin, ymax):
        ymin = 0

    # Plot
    _plt.plot(x, y, linestyle='None', marker='o', color='r', markersize = 7)
    _plt.plot(np.linspace(xmin, xmax), np.linspace(xmin, xmax)*s + i,'k--', linewidth=0.5)
    if xerr or yerr:
        _plt.errorbar(x, y, xerr=xerr, yerr=yerr)

    # Label text
    if label:
        label = r"$K=(" + "{:.3f}".format(s) + r"\pm" + "{:.3f}".format(s_err) + ")$ " + units
        _ax.text(labelx, labely, label, transform=_ax.transAxes, bbox={'facecolor':'white', 'edgecolor':'black', 'pad':10})

    # Grid
    _ax.grid(color='#e5e5e5', linestyle='--', linewidth=0.2)


def axes(xlabel=None, ylabel=None):
    _plt.xlabel(xlabel)
    _plt.ylabel(ylabel)


def show(save=False, output="graph.png"):
# Save file
    _plt.savefig(output,
                dpi=1000,
                # Plot will be occupy a maximum of available space
                bbox_inches='tight',
                )

# ### View and Save:
    _plt.show()
    _plt.cla()
    _plt.clf()
