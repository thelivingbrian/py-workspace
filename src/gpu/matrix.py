import numpy as np
import cupy as cp
import time

# Matrix size
N = 25000

# CPU Benchmark with NumPy
a_cpu = np.random.rand(N, N).astype(np.float32)
b_cpu = np.random.rand(N, N).astype(np.float32)

start_cpu = time.time()
result_cpu = np.dot(a_cpu, b_cpu)
end_cpu = time.time()

print(f"CPU (NumPy) Time: {end_cpu - start_cpu:.4f} seconds")

# GPU Benchmark with CuPy
a_gpu = cp.asarray(a_cpu)
b_gpu = cp.asarray(b_cpu)

cp.cuda.Stream.null.synchronize()  # Ensure GPU is ready
start_gpu = time.time()
result_gpu = cp.dot(a_gpu, b_gpu)
cp.cuda.Stream.null.synchronize()  # Wait for GPU to finish
end_gpu = time.time()

print(f"GPU (CuPy) Time: {end_gpu - start_gpu:.4f} seconds")
