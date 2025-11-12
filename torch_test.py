import torch, platform, sys, numpy

print("Python:", sys.version.split()[0], "| Platform:", platform.platform())
print("Torch:", torch.__version__)
print("NumPy:", numpy.__version__)
print("CUDA available:", torch.cuda.is_available())
print("Torch CUDA build:", torch.version.cuda)
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    x = torch.randn((3,3), device="cuda")
    print("Tensor on CUDA OK:", x.device)
else:
    x = torch.randn((3,3))
    print("Tensor on CPU OK:", x.device)
