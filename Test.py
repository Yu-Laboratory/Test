"""
Script: generate_npy_files.py

Description:
    Generates multiple NumPy (.npy) files filled with random floating-point data within a specified range.

Configuration:
    total_size   (int): Total target size of all files combined, in bytes (default: 50 GiB).
    file_size    (int): Size per individual file, in bytes (default: 49 MiB).
    dtype        (np.dtype): Data type of the array elements (default: np.float32).
    output_dir   (str): Directory where output .npy files will be saved.
    value_range  (tuple): Tuple of two floats (min_value, max_value) defining the range of random values.

Behavior:
    1. Compute the number of files to generate (rounding up).
    2. Create the output directory if it does not exist.
    3. For each file index:
        a. Calculate the number of elements per file based on file_size and dtype.itemsize.
        b. Generate an array of random floats uniformly distributed in [min_value, max_value).
        c. Save the array to an .npy file named 'file_XXX.npy'.
    4. Print progress and final summary of generated files.

Usage:
    python generate_npy_files.py

Requirements:
    - Python 3.x
    - NumPy library

Notes:
    - Adjust `total_size`, `file_size`, and `dtype` for different data volume or precision.

"""
import os
import numpy as np

# —— 配置区 —— #
total_size = 2 * 1024**3    # 50 GiB
file_size  = 49 * 1024**2    # 49 MiB
dtype      = np.float32      # 每个元素 4 字节，浮点

# 计算需要生成的文件数（向上取整）
num_files = (total_size + file_size - 1) // file_size

# 输出目录
output_dir = 'output_npy_files'
os.makedirs(output_dir, exist_ok=True)

# 每个文件元素个数（自动根据 dtype 大小调整）
elements_per_file = file_size // np.dtype(dtype).itemsize
a = -1000
b = 1000
# —— 开始生成 —— #
for i in range(42, num_files + 1 + 42):
    # 生成随机浮点数据，均匀分布在 [0, 1)
    arr = (b - a) * np.random.rand(elements_per_file).astype(dtype) + a
    path = os.path.join(output_dir, f'file_{i:03d}.npy')
    np.save(path, arr)
    print(f'✔ 已生成 {path} （约 {arr.nbytes / (1024**2):.2f} MiB 随机浮点数据）')

print(f'\n共生成 {num_files} 个文件，总约 {(num_files * file_size) / (1024**3):.2f} GiB。')
