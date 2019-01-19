# Jupyter Notebook on Raspberry Pi

## Usage

### Installation

```bash
pip3 install pipenv
pipenv sync

echo JUPYTER_CONFIG_DIR=`pwd`/.jupyter >> .env
echo IPYTHONDIR=`pwd`/.ipython >> .env
mkdir -p .jupyter
echo "c.NotebookApp.ip = '0.0.0.0'" > .jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.open_browser = False" > .jupyter/jupyter_notebook_config.py
```

## Start jupyter notebook

```bash
pipenv run jupyter notebook
```
