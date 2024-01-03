import numpy as np
version = np.__version__
print("Phiên bản Numpy hiện tại:", version)

# Hiển thị cấu hình xây dựng của Numpy
print("Cấu hình xây dựng của Numpy:")
for key, value in np.version.full_version.items():
    print(f"{key}: {value}")
