import matplotlib.pylab as _plt
from matplotlib import rc

# Plot size
_plt.rcParams['figure.figsize'] = (8, 5)

# LaTeX
rc('text.latex', preamble=r"\usepackage[utf8]{inputenc}")
rc('text.latex', preamble=r"\usepackage[russian]{babel}")
rc('text.latex', preamble=r"\usepackage{lmodern}")
rc('text.latex', preamble=r"\usepackage[T2A]{fontenc}")
rc('text.latex', unicode=True)

# Options
params = {'text.usetex' : True,
      'font.size' : 11,
      'font.family' : 'lmodern',
      'text.latex.unicode': True,
      }

_plt.rcParams.update(params)

# Get fig, ax
_fig, _ax = _plt.subplots()
_res = _plt.gcf()




def addplot(input="data.csv", units=None, label=None, labelx = 0.05, labely = 0.9, xerr=None, yerr=None):
    import numpy as np
    import pandas as pd
    import sympy as sp
    import statsmodels.api as sm
    import math

# Load data
    data = pd.read_csv(input, engine='python', header=None)

# Exract arrays
    x = np.array(data[0])
    y = np.array(data[1])
    t = sm.add_constant(x, prepend=False)

    row = 2
    if xerr:
        xerr = np.array(data[row])
        rows += 1
    if yerr:
        yerr = np.array(data[row])
        
# Fitting
    model = sm.OLS(y, t)
    result = model.fit()

# Saving parameters
    s_err, i_err = result.bse
    s, i = result.params


# Showing result
    result.summary().tables[1]


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
    _plt.plot(data[0], data[1],'ro', np.linspace(xmin, xmax), np.linspace(xmin, xmax)*s + i,'k--')
    if xerr or yerr:
        _plt.errorbar(x, y, xerr=xerr, yerr=yerr)
        

# Label text
    if label:
        label = r"$K=(" + "{:.3f}".format(s) + r"\pm" + "{:.3f}".format(s_err) + ")$ " + units
        _ax.text(labelx, labely, label, transform=_ax.transAxes, bbox={'facecolor':'white', 'edgecolor':'black', 'pad':10})

# Grid
    _ax.grid(color='#e5e5e5', linestyle='--', linewidth=0.2)


'''
# Updating axes limits

    def getlim(lim, lval):
        l, r = lim
        return (0, r) if (lval == 0) else (l, r)


    _plt.xlim(getlim(_plt.xlim(), xmin))
    _plt.ylim(getlim(_plt.ylim(), ymin))
'''


def axes(xlabel=None, ylabel=None):
    _plt.xlabel(xlabel)
    _plt.ylabel(ylabel)


def show():
# Save into variable
    _res = _plt.gcf()
# ### View and Save:
    _plt.show()
    


def save(output="graph.pdf"):

# Save file
    _res.savefig(output, 
                dpi=1000, 
                # Plot will be occupy a maximum of available space
                bbox_inches='tight', 
                )

