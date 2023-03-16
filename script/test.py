import uproot
import awkward
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplhep as hep

# Load the file
tree = uproot.open("../python/TnPTree_data.root:tnpEleIDs/fitter_tree")

# show the branches including pass/fail
key = [x for x in tree.keys() if "passing" in x]
print(key)

# load the branches
df = tree.arrays(['passingHEEPV71'], library="np")
print(df)