import time
import cv2
import cupy as cp
from cupyx.scipy.ndimage import gaussian_filter

img = cv2.imread("your_image_4k.jpg")
#img = cv2.resize(img, (1920, 1080))

# CPU (OpenCV)
t0 = time.perf_counter()
cpu_blur = cv2.GaussianBlur(img, (15, 15), 0)   # sigma auto
t1 = time.perf_counter()

# GPU (CuPy)
gpu = cp.asarray(img)
# Match OpenCV's sigma for ksize=15 (sigma ≈ 2.6)
t2 = time.perf_counter()
gpu_blur = gaussian_filter(gpu, sigma=(2.6, 2.6, 0.0))
cp.cuda.Stream.null.synchronize()  # ensure kernel finished
t3 = time.perf_counter()
gpu_blur_host = cp.asnumpy(gpu_blur)

print(f"CPU: {(t1 - t0):.4f}s, CuPy GPU: {(t3 - t2):.4f}s")
cv2.imwrite("blur_cupy.jpg", gpu_blur_host)
