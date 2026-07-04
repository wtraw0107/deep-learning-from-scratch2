import cupy as cp

print(cp.__version__)
cp.show_config()
print(cp.cuda.runtime.getDeviceCount())