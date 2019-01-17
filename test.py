from neuralfingerprint import load_data

traindata, valdata, testdata = load_data(
    [
        "/home/xiaozhi/datasets/drugs/17p_v1_splited/train/train_p0.csv",
        "/home/xiaozhi/datasets/drugs/17p_v1_splited/val/val_p0.csv",
        "/home/xiaozhi/datasets/drugs/17p_v1_splited/test/test_p0.csv"
    ],
    input_name='smile',
    target_name='p0')
# print(traindata)
# print(valdata)
print(testdata)
