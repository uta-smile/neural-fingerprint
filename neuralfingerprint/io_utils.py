import os
import csv
import numpy as np
import itertools as it


def read_csv(filename, input_name, target_name):
    data = ([], [])
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[0].append(row[input_name])
            data[1].append(float(row[target_name]))
    return list(map(np.array, data))


def load_data(filename, input_name, target_name):
    if len(filename) == 3:
        return load_data_slices_islist(filename, input_name, target_name)
    else:
        raise Exception("Please make sure the filename contains three ones.")

    


def load_data_slices_islist(filename, input_name, target_name):
    train_file = filename[0]
    val_file = filename[1]
    test_file = filename[2]
    train_data = read_csv(train_file, input_name, target_name)
    val_data = read_csv(val_file, input_name, target_name)
    test_data = read_csv(test_file, input_name, target_name)
    return [(train_data[0], train_data[1]), (val_data[0], val_data[1]), (test_data[0], test_data[1])]

def load_data_slices_nolist(filename, slices, input_name, target_name):	
    stops = [s.stop for s in slices]	
    if not all(stops):	
        raise Exception("Slices can't be open-ended")	


    data = read_csv(filename, max(stops), input_name, target_name)	
    return [(data[0][s], data[1][s]) for s in slices]

def list_concat(lists):
    return list(it.chain(*lists))


def load_data_slices(filename, slice_lists, input_name, target_name):
    stops = [s.stop for s in list_concat(slice_lists)]
    if not all(stops):
        raise Exception("Slices can't be open-ended")

    data = read_csv(filename, max(stops), input_name, target_name)

    return [(np.concatenate([data[0][s] for s in slices], axis=0),
             np.concatenate([data[1][s] for s in slices], axis=0))
            for slices in slice_lists]


def get_output_file(rel_path):
    return os.path.join(output_dir(), rel_path)


def get_data_file(rel_path):
    return os.path.join(data_dir(), rel_path)


def output_dir():
    return os.path.expanduser(safe_get("OUTPUT_DIR"))


def data_dir():
    return os.path.expanduser(safe_get("DATA_DIR"))


def safe_get(varname):
    if varname in os.environ:
        return os.environ[varname]
    else:
        raise Exception("%s environment variable not set" % varname)
