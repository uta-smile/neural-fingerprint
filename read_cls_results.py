from __future__ import print_function

import pickle

import numpy as np

results = pickle.load(open("solub.pickle"))

predict = results["predict"]
target = results["target"]
print(predict.shape)
print(target.shape)

print(type(predict))
print(type(target))

print(predict[0])
print(target[0])

predict = (predict > 0.5).astype(np.int8)
target = target.astype(np.int8)

print((predict == target).sum())
print((predict == target).sum() * 1.0 / predict.shape[0])
