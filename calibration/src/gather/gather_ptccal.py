import h5py
import numpy as np
import os
import sys
import time
import glob

from gather_base import GatherBase

class Gather(GatherBase):
    def __init__(self,
                 in_fname,
                 out_fname,
                 runs):
        super().__init__(in_fname, out_fname, runs)
