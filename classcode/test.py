import matplotlib.pylab as plt
import numpy as np
import scipy.optimize as opt
from matplotlib.colors import LogNorm

#from astroML.datasets import fetch_sdss_spectrum
#from scipy.interpolate import interp1d
#from scipy.integrate import simps

from setup import image_home_dir
#from fetch_sdss_image import fetch_sdss_image
from PIL import Image

#from setup import setup 
import os
from itertools import product
from numpy import random as rnd

def plot_pretty(dpi=175,fontsize=9):
    # import pyplot and set some parameters to make plots prettier
    import matplotlib.pyplot as plt

    plt.rc("savefig", dpi=dpi)
    plt.rc('text', usetex=True)
    plt.rc('font', size=fontsize)
    plt.rc('xtick', direction='in') 
    plt.rc('ytick', direction='in')
    plt.rc('xtick.major', pad=5) 
    plt.rc('xtick.minor', pad=5)
    plt.rc('ytick.major', pad=5) 
    plt.rc('ytick.minor', pad=5)
    plt.rc('lines', dotted_pattern = [0.5, 1.1])

    return
