## -----------------------------------------------------------------------------
## This is a Makefile to facilitate building a complete Python environment for
## the development of a Python package
## -----------------------------------------------------------------------------

help: ## Show this help.
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "};  \
	{printf "%-15s %s\n", $$1, $$2}'

miniconda:	## Downloads and install latest Miniconda3 x86_64 for Linux
	# TODO: this tag is yet to be tested
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash Miniconda3-latest-Linux-x86_64.sh -p $HOME/miniconda
	rm Miniconda3-latest-Linux-x86_64.sh
	conda init
	conda config --set auto_activate_base true

env-create:	## Creates a conda environment named "sample" with Python 3.9
	conda create -n sample python=3.9 --yes

env-remove:	## Removes the "sample" environment
	conda env remove -n sample

# must run `conda activate sample` before executing this
env-setup:  ## Sets up the environment for development
	# Install repository as an editable package
	pip install --editable .

	# Installs pre-commit hooks
	pip install pre-commit~=2.8.2
	pre-commit install

	# Install jupyter to remove notebooks output
	pip install jupyter

	# Installs Sphinx documentation related packages
	pip install sphinx sphinx_rtd_theme

autodoc:    ## Build sphinx auto documentation
	cd docs; sphinx-apidoc --force --maxdepth 2 --private --module-first \
	--ext-autodoc --ext-viewcode --ext-todo \
	-o source/module ../sample
