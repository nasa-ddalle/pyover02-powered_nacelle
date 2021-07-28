#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard library modules
import os
import shutil


# This folder
fdir = os.path.dirname(os.path.realpath(__file__))
# Name of working folder
fwork = os.path.join(fdir, "work")

# Files list
fnames = [
    "flowthrough.json",
    "powered.json",
    "bcpower.json",
    "tools/nacelle.py",
    "tools/bcnacelle.py",
    "inputs/matrix/flowthrough.csv",
    "inputs/matrix/powered.csv",
    "inputs/matrix/bcpower.csv",
    "inputs/flowthrough-mach.lay",
    "inputs/flowthrough-mach-mesh.lay",
    "inputs/powered-cp.lay",
    "inputs/powered-mach.lay",
    "inputs/powered-mach-mesh.lay",
    "common_flowthrough/overflow.inp",
    "common_flowthrough/grid.in",
    "common_flowthrough/xrays.in",
    "common_flowthrough/Config.xml",
    "common_flowthrough/fomo/grid.ib",
    "common_flowthrough/fomo/grid.ibi",
    "common_flowthrough/fomo/grid.i.tri",
    "common_flowthrough/fomo/grid.map",
    "common_flowthrough/fomo/grid.nsf",
    "common_flowthrough/fomo/mixsur.fmp",
    "common_flowthrough/fomo/mixsur.inp",
    "common_powered/overflow_test01.inp",
    "common_powered/overflow_test02.inp",
    "common_powered/overflow_test03.inp",
    "common_powered/grid.in",
    "common_powered/xrays.in",
    "common_powered/Config.xml",
    "common_powered/fomo/grid.bnd",
    "common_powered/fomo/grid.ib",
    "common_powered/fomo/grid.ibi",
    "common_powered/fomo/grid.i.tri",
    "common_powered/fomo/grid.map",
    "common_powered/fomo/grid.nsf",
    "common_powered/fomo/grid.ptv",
    "common_powered/fomo/mixsur.fmp",
    "common_powered/fomo/mixsur.inp"
]

# Check if working folder exists
if not os.path.isdir(fwork):
    # Create it
    os.mkdir(fwork)

# Loop through files
for fname in fnames:
    # System independence
    f1 = fname.replace("/", os.sep)
    # Source file
    fsrc = os.path.join(fdir, f1)
    # Destination file
    fdest = os.path.join(fwork, f1)
    # Check if output file already exists
    if os.path.isfile(fdest):
        # Skip
        continue
    # Break out folder names (if any)
    fparts = fname.split("/")[:-1]
    # Create cumulative subfolder name
    fsub = fwork
    # Loop through subfolder names
    for fpart in fparts:
        # Add to subfolder name
        fsub = os.path.join(fsub, fpart)
        # Check if folder exists
        if os.path.isdir(fsub):
            continue
        # Create folder
        os.mkdir(fsub)
    # Copy file
    shutil.copy(fsrc, fdest)

