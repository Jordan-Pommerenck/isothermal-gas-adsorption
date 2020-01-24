#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

parser = argparse.ArgumentParser(description =
    """
        This script functions by reading in energy and entropy data given
        the number 'N' forming the LJ cluster. The heat capacity is computed
        and compared to a benchmark (which is also read in).  A heat capacity
        error .TXT file is saved in the appropriate data directory.
    """)

parser.add_argument('--N', metavar='cluster_size', type=int, default=1,
                    help='The number of atoms in the LJ cluster -- Default = 1')
parser.add_argument('--benchmark', required=True,
                    help='Each file is compared to the benchmark reference -- Required')
parser.add_argument('--need_wide_cv', action='store_true',
                    help='A boolean that determines whether we plot a narrow range --Default = False')
args = parser.parse_args()
print(args)

N=args.N
need_wide_cv = args.need_wide_cv
benchmark = args.benchmark # This is bench below!

datadir = '../lj-cluster/data/lj%i/' % N
os.makedirs(datadir, exist_ok=True)

"""


    (4) I will put this in lj-cluster/data
    (5) I will automatically loop through data in given directory
    (6) I will need four argparse arguments!
    (7) possibly
"""

T = np.arange(0.01, 0.05000001, 0.0005)
wideT = np.arange(0.01, 0.4000001, 0.001)

CV = None
need_wide_cv = True

def heat_capacity(T, E, S):
    C = np.zeros_like(T)
    for i in range(len(T)):
        boltz_arg = S - E/T[i]
        P = np.exp(boltz_arg - boltz_arg.max())
        P = P/P.sum()
        U = (E*P).sum()
        C[i] = ((E-U)**2*P).sum()/T[i]**2
    return C + 31*1.5


# old_cvs = []
#
# fnames = [
#     '/home/droundy/src/sad-monte-carlo/tiny-lj-benchmark',
#     '/home/jordan/sad-monte-carlo/lj-31-benchmark',
#
#     '/home/jordan/sad-monte-carlo/lj-sad-31-bin001',
#     '/home/jordan/sad-monte-carlo/lj-sad-31-bin01',
#     '/home/jordan/sad-monte-carlo/lj-sad-31-bin002',
#     # '/home/jordan/sad-monte-carlo/lj-sad-31-bin0005',
#     '/home/droundy/src/sad-monte-carlo/lj-sad-31-bin0001',
#
#     '/home/jordan/sad-monte-carlo/lj-wl-31-bin01',
#     '/home/jordan/sad-monte-carlo/lj-wl-31-bin001',
#     '/home/jordan/sad-monte-carlo/lj-wl-31-bin002',
#     '/home/jordan/sad-monte-carlo/lj-wl-31-bin0005',
#     '/home/jordan/sad-monte-carlo/lj-wl-31-bin0001',
#
#     '/home/jordan/sad-monte-carlo/lj-inv-t-wl-31-bin01',
#     '/home/jordan/sad-monte-carlo/lj-inv-t-wl-31-bin001',
#     '/home/jordan/sad-monte-carlo/lj-inv-t-wl-31-bin001-58',
#     '/home/jordan/sad-monte-carlo/lj-inv-t-wl-31-bin001-54',
#     '/home/jordan/sad-monte-carlo/lj-inv-t-wl-31-bin001-52',
#     '/home/jordan/sad-monte-carlo/lj-inv-t-wl-31-bin002',
#     '/home/jordan/sad-monte-carlo/lj-inv-t-wl-31-bin0005',
#     '/home/jordan/sad-monte-carlo/lj-inv-t-wl-31-bin0001',
#
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e5-bin01',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e5-bin001',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e5-bin002',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e5-bin0005',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e5-bin0001',
#
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e6-bin01',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e6-bin001',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e6-bin002',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e6-bin0005',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e6-bin0001',
#
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e7-bin01',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e7-bin001',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e7-bin002',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e7-bin0005',
#     '/home/jordan/sad-monte-carlo/lj-samc-31-1e7-bin0001',
# ]
#
# for fname in fnames:
#     print(fname)
#     time = np.loadtxt(fname+'.time')
#     my_energy = np.loadtxt(fname+'.energy')
#     my_entropy = np.loadtxt(fname+'.entropy')
#
#     if CV is None:
#         Ebest = my_energy;
#         Sbest = my_entropy[-1,:]
#         CV = heat_capacity(T, Ebest, Sbest)
#         np.savetxt(datadir+'bench-cv.txt',
#                    np.array([T, CV]).transpose(),
#                    fmt='%.4g', # good enough for our plot
#         );
#     elif need_wide_cv:
#         wideCV = heat_capacity(wideT, my_energy, my_entropy[-1,:])
#         np.savetxt(datadir+'wide-cv.txt',
#                    np.array([wideT, wideCV]).transpose(),
#                    fmt='%.4g', # good enough for our plot
#         );
#         need_wide_cv = False
#
#     cv_error = []
#     cv_max_error = []
#     myt = []
#     for t in range(len(my_entropy[:, 0])):
#         if time[t] < 1e7:
#             continue
#         myt.append(time[t])
#         mycv = heat_capacity(T, my_energy, my_entropy[t,:])
#         plt.clf()
#         for i in range(len(old_cvs)):
#             plt.plot(T, old_cvs[i], label=fnames[i])
#         plt.plot(T, mycv, label=fname+' '+str(time[t]))
#         plt.legend(loc='best')
#         plt.xlim(T[0], T[-1])
#         plt.ylim(80, 130)
#         plt.pause(0.01)
#
#         err = 0
#         norm = 0
#         for j in range(1, len(mycv)):
#             err += abs(CV[j]-mycv[j])
#             norm += 1.0
#         cv_error.append(err/norm)
#         cv_max_error.append(abs(CV-mycv).max())
#         if time[t] == 1e12:
#             np.savetxt(datadir+os.path.basename(fname)+'-cv.txt',
#                        np.array([T, mycv]).transpose(),
#                        fmt='%.4g', # good enough for our plot
#             );
#             np.savetxt(datadir+os.path.basename(fname)+'-wide-cv.txt',
#                        np.array([wideT, heat_capacity(wideT, my_energy, my_entropy[t,:])]).transpose(),
#                        fmt='%.4g', # good enough for our plot
#             );
#
#     old_cvs.append(mycv)
#
#     np.savetxt(datadir+os.path.basename(fname)+'-cv-error.txt',
#                np.array([myt, cv_error, cv_max_error]).transpose(),
#                fmt='%.3g', # low resolution is good enough for error data.
#     );
