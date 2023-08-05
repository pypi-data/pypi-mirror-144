###############################################################################
# Copyright (c) 2022, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory
# Written by the Merlin dev team, listed in the CONTRIBUTORS file.
# <merlin@llnl.gov>
#
# LLNL-CODE-797170
# All rights reserved.
# This file is part of merlin-spellbook.
#
# For details, see https://github.com/LLNL/merlin-spellbook and
# https://github.com/LLNL/merlin.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###############################################################################
import numpy as np

import spellbook.ml.surrogates as surrogates


try:
    import cPickle as pickle
except ImportError:
    import pickle


def load_infile(args):
    with np.load(args.infile) as data:
        if args.X is not None:
            X = stack_arrays(data, args.X)  # inputs
        elif "X" in data.keys():
            X = data["X"]
        else:
            X = data[data.files[0]]

        if args.y is not None:
            y = stack_arrays(data, args.y)  # outputs
        elif "y" in data.keys():
            y = data["y"]
        else:
            y = data[data.files[1]]
    return X, y


def make_regressor(args):
    if args.reg_args is None:
        reg_args = {}
    else:
        reg_args = args.reg_args

    regr = surrogates.sklearnRegressors.factory(args.regressor, **reg_args)
    X, y = load_infile(args)

    n_samples_X = X.shape[0]
    n_samples_y = y.shape[0]

    if n_samples_X != n_samples_y:
        raise ValueError("n_samples_X != n_samples_y")

    # single feature or sample reshape as appropriate for sklearn
    if n_samples_y == 1:
        y.reshape((1, -1))
    elif len(y.shape) == 1:
        y.reshape((-1, 1))

    regr.fit(X, y)
    with open(args.outfile, "wb") as f:
        pickle.dump(regr, f)


def stack_arrays(data, delimited_names, delimiter=","):
    stacked = np.vstack([data[name] for name in delimited_names.split(delimiter)])
    return stacked.T
