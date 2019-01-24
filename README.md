Neural Graph Fingerprints
=============

<img src="https://github.com/HIPS/DeepMolecules/blob/master/paper/figures/3d-nets/net1.png" width="300">

This software package implements convolutional nets which can take molecular graphs of arbitrary size as input.
These are useful for predicting the properties of novel molecules, and are designed to be a drop-in replacement for Morgan or ECFP fingerprints.

The paper describing the algorithm used is:

[Convolutional Networks on Graphs for Learning Molecular Fingerprints](http://arxiv.org/pdf/1509.09292.pdf)

by

David Duvenaud, Dougal Maclaurin, Jorge Aguilera-Iparraguirre, Rafael Gómez-Bombarelli, Timothy Hirzel, Alán Aspuru-Guzik, and Ryan P. Adams.

## How to install

This package requires:
* Scipy version >= 0.15.0  (For Anaconda users, use `conda install scipy` instead of `pip install scipy` to upgrade your version.)
* [RDkit](http://www.rdkit.org/docs/Install.html)
* [Autograd](http:github.com/HIPS/autograd) (Just run `pip install autograd`)
* [Smile](https://github.com/uta-smile/smile-python) (Just run `pip install smile`)

## How to run
* `python regression.py data_path='/smile/nfs/hm/17properties_datasets/17p_v1/single_property_xiaozhi/clean_17p_v1_splited' i=0`
* data_path: Make sure there are three subfolders under the target data_path named train, val and test. if you mounted the nfs, please try this data_path: `/smile/nfs/hm/17properties_datasets/17p_v1/single_property_xiaozhi/clean_17p_v1_splited`
* i: in this case, i is the number of 17 properties (pgp, solub, logp, 2c9, 2d6, 2c19, rlm, mmp, ames, pldc, heptox, 3a4, pampac, pampar, herg, 1a2, vd), from 0 to 16

## Examples

This package includes a [regression example](examples/regression.py) and a [visualization example](examples/visualization.py) in the examples directory.

## Authors

This software was primarily written by [David Duvenaud](https://www.cs.toronto.edu/~duvenaud/), [Dougal Maclaurin](https://dougalmaclaurin.com/), and [Ryan P. Adams](http://www.seas.harvard.edu/directory/~rpa).
Please feel free to submit any bugs or feature requests.
We'd also love to hear about your experiences with this package in general.
Drop us an email!

We want to thank Jennifer Wei for helpful contributions and advice, and Analog Devices International and Samsung Advanced Institute of Technology for their generous support.

## TensorFlow and Theano implementations

A Tensorflow implementation of a closely-related algorithm can be found at [https://github.com/momeara/DeepSEA](https://github.com/momeara/DeepSEA)

and a Theano implementation can be found at [https://github.com/debbiemarkslab/neural-fingerprint-theano](https://github.com/debbiemarkslab/neural-fingerprint-theano)

