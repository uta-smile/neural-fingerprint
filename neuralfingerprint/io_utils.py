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
    # slices = []
    # start = 0
    # for size in sizes:
    #     stop = start + size
    #     slices.append(slice(start, stop))
    #     start = stop
    return load_data_slices_nolist(filename, input_name, target_name)


def load_data_slices_nolist(filename, input_name, target_name):
    # stops = [s.stop for s in slices]
    # if not all(stops):
    #     raise Exception("Slices can't be open-ended")
    train_file = filename[0]
    val_file = filename[1]
    test_file = filename[2]
    data0 = read_csv(train_file, input_name, target_name)
    data1 = read_csv(val_file, input_name, target_name)
    data2 = read_csv(test_file, input_name, target_name)
    return [(data0[0], data0[1]), (data1[0], data1[1]), (data2[0], data2[1])]


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
