"""Generate random samples of datasets."""

from pathlib import Path
import pandas as pd

# %% Set parameters.

datasample_seed = 1984

root_path = Path(__file__).parent.parent

dataset_path = root_path.joinpath('datasets')
datasample_path = root_path.joinpath('datasamples')

dataset_files = {
    'train': 'train.csv',
    'test': 'test.csv'
}

datasample_sizes = {
    '200': 200,
    '02K': 2000,
    '20K': 20000
}

# %% Generate paths.

datasample_files = dict()
for size_key in datasample_sizes:
    files = dict()
    for file_key, file_name in dataset_files.items():
        file_name = file_name.split('.')
        file_name.insert(1, '_' + size_key + '.')
        file_name = ''.join(file_name)
        files[file_key] = file_name
    datasample_files[size_key] = files

dataset_paths = {
    file_key: dataset_path.joinpath(file_name)
    for file_key, file_name in dataset_files.items()
}

datasample_paths = {
    size_key: {
        file_key: datasample_path.joinpath(file_name)
        for file_key, file_name in datasample_files[size_key].items()
    }
    for size_key in datasample_files
}

# %% Read datasets.

datasets = {
    data_key: pd.read_csv(data_path)
    for data_key, data_path in dataset_paths.items()
}

for data_key in datasets:
    print(
        f'{data_key} {datasets[data_key].shape}',
        dataset_paths[data_key],
        sep=' <- '
    )

# %% Generate and save random datasamples.

print(f'seed={datasample_seed}')

for size_key, data_paths in datasample_paths.items():
    data_size = datasample_sizes[size_key]
    for data_key, data_path in data_paths.items():
        data = datasets[data_key].sample(
            data_size,
            random_state=datasample_seed
        )
        data.to_csv(data_path)
        print(
            f'{data_key} {data.shape}',
            data_path,
            sep=' -> '
        )
