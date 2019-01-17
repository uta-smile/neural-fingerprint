from __future__ import print_function

import os


# def main():
#     data_path = "/smile/nfs/shengwang/drug/logp"
#     train_data = os.path.join(data_path, "train_logp_data.smi")
#     train_label = os.path.join(data_path, "train_logp_label.smi")
#     valid_data = os.path.join(data_path, "val_logp_data.smi")
#     valid_label = os.path.join(data_path, "val_logp_label.smi")
#     test_data = os.path.join(data_path, "test_logp_data.smi")
#     test_label = os.path.join(data_path, "test_logp_label.smi")
#     head, target = "smile", "logp"
#     target_file = os.path.join(data_path, "logp.csv")

#     smiles = []
#     labels = []
#     with open(train_data, "r") as f:
#         lines = [x.strip() for x in f.readlines() if x.strip()]
#         smiles += lines
#         print("Train data: ", len(lines))
#     with open(valid_data, "r") as f:
#         lines = [x.strip() for x in f.readlines() if x.strip()]
#         smiles += lines
#         print("Valid data: ", len(lines))
#     with open(test_data, "r") as f:
#         lines = [x.strip() for x in f.readlines() if x.strip()]
#         smiles += lines
#         print("Test data: ", len(lines))

#     with open(train_label, "r") as f:
#         lines = [x.strip() for x in f.readlines() if x.strip()]
#         labels += lines
#         print("Train data: ", len(lines))
#     with open(valid_label, "r") as f:
#         lines = [x.strip() for x in f.readlines() if x.strip()]
#         labels += lines
#         print("Valid data: ", len(lines))
#     with open(test_label, "r") as f:
#         lines = [x.strip() for x in f.readlines() if x.strip()]
#         labels += lines
#         print("Test data: ", len(lines))

#     assert len(smiles) == len(labels), "smiles labels are not of same number"

#     with open(target_file, "w") as f:
#         f.write("%s,%s\n" % (head, target))
#         for x, y in zip(smiles, labels):
#             f.write("%s,%s\n" % (x, y))


def main():
    data_path = "/smile/nfs/shengwang/drug/solub"
    train_data = os.path.join(data_path, "train_solub_data.smi")
    train_label = os.path.join(data_path, "train_solub_label.smi")
    valid_data = os.path.join(data_path, "val_solub_data.smi")
    valid_label = os.path.join(data_path, "val_solub_label.smi")
    test_data = os.path.join(data_path, "test_solub_data.smi")
    test_label = os.path.join(data_path, "test_solub_label.smi")
    head, target = "smile", "solub"
    target_file = os.path.join(data_path, "solub.csv")

    smiles = []
    labels = []
    with open(train_data, "r") as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
        smiles += lines
        print("Train data: ", len(lines))
    with open(valid_data, "r") as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
        smiles += lines
        print("Valid data: ", len(lines))
    with open(test_data, "r") as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
        smiles += lines
        print("Test data: ", len(lines))

    with open(train_label, "r") as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
        labels += lines
        print("Train data: ", len(lines))
    with open(valid_label, "r") as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
        labels += lines
        print("Valid data: ", len(lines))
    with open(test_label, "r") as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
        labels += lines
        print("Test data: ", len(lines))

    assert len(smiles) == len(labels), "smiles labels are not of same number"

    with open(target_file, "w") as f:
        f.write("%s,%s\n" % (head, target))
        for x, y in zip(smiles, labels):
            f.write("%s,%s\n" % (x, y))


if __name__ == "__main__":
    main()
