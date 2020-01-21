from __future__ import division, print_function
import sys, os, matplotlib
import numpy as np

matplotlib.rcParams['text.usetex'] = True
matplotlib.rc('font', family='serif')
if 'noshow' in sys.argv:
        matplotlib.use('Agg')
import matplotlib.pyplot as plt
import colors
import readnew

plt.figure(figsize=(5, 4))

fname = '../square-well/data/samc-1e4-50-s1-reference-lndos.dat'
e, lndos = readnew.e_lndos(fname)

emax = -8
emin = -276
Tmin = 0.333333
eminimportant = -265
eminimportant = -248
eSmax = -120
Smin = -377.174
Sminimportant = -255
Sminimportant = -197.9025045
#plt.plot(e, (e - eminimportant)/.2 + Sminimportant - Smin, 'r:')


ei = np.arange(eminimportant, eSmax, 0.1)
B = 1/(2*Tmin*(eSmax - eminimportant))
Stop = Sminimportant + B*(eSmax - eminimportant)**2
plt.fill_between(ei,
                 Stop - B*(ei - eSmax)**2 - Smin,
                 ei*0 + Sminimportant - Smin,
                 color='tab:blue', alpha=0.25,
                label=r'quadratic $\Delta S_{\textrm{tot}}$')

interesting = (e > eminimportant)*(e < eSmax)
plt.rcParams['hatch.color'] = 'tab:green'
plt.rcParams['hatch.linewidth'] = 3
plt.fill_between(e[interesting],
                 lndos[interesting] - Smin,
                 e[interesting]*0 + Sminimportant - Smin,
                 #color='tab:green',
                hatch='\\\\\\', label=r'actual $\Delta S_{\textrm{tot}}$',
                facecolor='none', edgecolor='tab:green', linewidth=0)


plt.plot(e, lndos - Smin, color='tab:green', label='$S$')
plt.axvline(eminimportant, linestyle=':', color='tab:gray')
plt.axvline(eSmax, linestyle=':', color='tab:gray')
plt.ylabel('$S/k_B$')
plt.ylim(0, (Stop-Smin)*1.05)
plt.xlim(emin, emax)
plt.xlabel('$E$')
plt.legend(loc='lower right')
plt.tight_layout()

plt.savefig('N50-lndos-comparison.pdf')
#plt.show()
