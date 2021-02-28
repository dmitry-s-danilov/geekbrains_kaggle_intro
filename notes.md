### Python virtual environment creation

```bash
# Create virtual environment.
python -m venv .venv

# Activate virtual environment.
source .venv/bin/activate

which python

# Upgrade package manager.
python -m pip install --upgrade pip

# Install ipykernel module
# which provides the IPython kernel for Jupyter.
pip install ipykernel

# List installed packages
pip list

# Output installed packages in requirements format.
pip freeze > requirements.txt

cat requirements.txt

# Add virtual environment to Jupyter by typing.
python -m ipykernel install --user --name=kaggle_intro

# List installed kernel specifications.
jupyter kernelspec list

# Remove Jupyter kernelspec by name.
jupyter kernelspec uninstall kaggle_intro

cat ~/.local/share/jupyter/kernels/kaggle_intro/kernel.json

# Deactivate virtual environment.
deactivate
```
