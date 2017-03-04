import matplotlib.pylab as _plt
from matplotlib import rc

import numpy as np
import pandas as pd
import sympy as sp
import statsmodels.api as sm
import math

# Plot size
_plt.rcParams['figure.figsize'] = (16, 9)

# LaTeX
rc('text.latex', preamble=r"\usepackage[utf8]{inputenc}")
rc('text.latex', preamble=r"\usepackage[russian]{babel}")
rc('text.latex', preamble=r"\usepackage{lmodern}")
rc('text.latex', preamble=r"\usepackage[T2A]{fontenc}")
rc('text.latex', unicode=True)

# Options
params = {'text.usetex' : True,
      'font.size' : 20,
      'font.family' : 'lmodern',
      'text.latex.unicode': True,
      }

_plt.rcParams.update(params)

# Get fig, ax
_fig, _ax = _plt.subplots()
_res = _plt.gcf()
_row = 0


def addplot(input="data.csv", units="", label=None, labelx = 0.05, labely = 0.9, xerr=None, yerr=None, number=1):
    global _row

    if number > 1:
        for count in range(number):
            addplot(input=input, xerr=xerr, yerr=yerr, number=0)
        _row = 0
        return

# Load data
    data = pd.read_csv(input, engine='python', header=None)

# Exract arrays
    x = np.array(data[_row])
    _row += 1
    y = np.array(data[_row])
    _row += 1

    t = sm.add_constant(x, prepend=False)

    if xerr:
        xerr = np.array(data[row])
        _row +=1
    if yerr:
        yerr = np.array(data[row])
        _row +=1
        
# Fitting
    model = sm.OLS(y, t)
    result = model.fit()

# Saving parameters
    s_err, i_err = result.bse
    s, i = result.params


# Showing result
    from IPython.display import display
    display(result.summary().tables[1])

# Caclculate ranges
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
    
    if number > 0:
        _row = 0


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
    

