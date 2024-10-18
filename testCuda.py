import numpy as np
import torch

print("NumPy version:", np.__version__)
print("PyTorch version:", torch.__version__)
a = np.array([1, 2, 3])
b = torch.tensor(a)
print("Tensor:", b)


print(torch.__version__)            # Check PyTorch version
print(torch.version.cuda)           # Check CUDA version used by PyTorch
print(torch.cuda.is_available())    # Should return True if CUDA is available
