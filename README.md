# llm-from-scratch

## PyTorch Starter (CPU oder CUDA 12.4)

### Schnellstart

#### Windows (PowerShell)
```powershell
# CPU
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip
pip install -r requirements-cpu.txt
python torch_test.py

# CUDA 12.4
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip
pip install -r requirements-cuda130.txt
python torch_test.py
```

#### Linux / WSL / macOS (bash)
```bash
# CPU
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements-cpu.txt
python torch_test.py

# CUDA 12.4 (Linux mit NVIDIA)
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements-cuda124.txt
python torch_test.py
```