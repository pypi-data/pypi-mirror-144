# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pymsm', 'pymsm.datasets', 'pymsm.examples']

package_data = \
{'': ['*'], 'pymsm': ['archive/*']}

install_requires = \
['joblib>=1.1.0,<2.0.0',
 'lifelines>=0.26.4,<0.27.0',
 'matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.22.2,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'tabulate>=0.8.9,<0.9.0',
 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'pymsm',
    'version': '0.1.7',
    'description': 'Multstate modeling in Python',
    'long_description': '[![pypi version](https://img.shields.io/pypi/v/pymsm)](https://pypi.org/project/pymsm/)\n[![Tests](https://github.com/hrossman/pymsm/workflows/Tests/badge.svg)](https://github.com/hrossman/pymsm/actions?workflow=Tests)\n[![codecov](https://codecov.io/gh/hrossman/pymsm/branch/main/graph/badge.svg?token=FG434UHSQ2)](https://codecov.io/gh/hrossman/pymsm)\n[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://hrossman.github.io/pymsm)\n[![DOI](https://zenodo.org/badge/443028256.svg)](https://zenodo.org/badge/latestdoi/443028256)\n\n![PyMSM](https://github.com/hrossman/pymsm/blob/main/docs/pymsm_icon.svg)  \n\nMultistate competing risk models in Python  \n  \n[Read the Docs](https://hrossman.github.io/pymsm/)  \n  \n[Hagai Rossman](https://hrossman.github.io/), [Ayya Keshet](https://github.com/ayya-keshet), [Malka Gorfine](https://www.tau.ac.il/~gorfinem/) 2022\n\n\n`PyMSM` is a Python package for fitting competing risks and multistate models, with a simple API which allows user-defined model, predictions at a single or population sample level, statistical summaries and figures.  \n\nFeatures include:\n\n- Fit a Competing risks Multistate model based on survival analysis (time-to-event) models.\n- Deals with right censoring, competing events, recurrent events, left truncation, and time-dependent covariates.\n- Run Monte-carlo simulations for paths emitted by the trained model and extract various summary statistics and plots.\n- Load or configure a pre-defined model and run path simulations.\n- Modularity and compatibility for different time-to-event models such as Survival Forests and other custom models.\n\n\n## Installation\n\n```console\npip install pymsm\n```\n\nRequires Python >=3.8\n\n## Quick example\n\n```py linenums="1"\n# Load data (See Rotterdam example for full details)\nfrom pymsm.datasets import prep_rotterdam\ndataset, states_labels = prep_rotterdam()\n\n# Define terminal states\nterminal_states = [3]\n\n#Init MultistateModel\nfrom pymsm.multi_state_competing_risks_model import MultiStateModel\nmulti_state_model = MultiStateModel(dataset,terminal_states)\n\n# Fit model to data\nmulti_state_model.fit()\n\n# Run Monte-Carlo simulation and sample paths\nmcs = multi_state_model.run_monte_carlo_simulation(\n              sample_covariates = dataset[0].covariates.values,\n              origin_state = 1,\n              current_time = 0,\n              max_transitions = 2,\n              n_random_samples = 10,\n              print_paths=True)\n```\n\n```mermaid\n    stateDiagram-v2\n    s1 : (1) Primary surgery\n    s2 : (2) Disease recurrence\n    s3 : (3) Death\n    s1 --> s2: 1518 \n    s1 --> s3: 195 \n    s2 --> s3: 1077 \n```  \n\n\n## Full examples\n1. [Rotterdam Illness-death example](https://github.com/hrossman/pymsm/blob/main/src/pymsm/examples/Rotterdam_example.ipynb)\n2. [EBMT multistate example](https://github.com/hrossman/pymsm/blob/main/src/pymsm/examples/ebmt.ipynb)\n3. [COVID hospitalizations multistate example](https://github.com/hrossman/pymsm/blob/main/src/pymsm/examples/COVID_hospitalization_example.ipynb)\n\n  \n## Citation\n\nIf you found this library useful in academic research, please cite:\n\n```bibtex\n@software{Rossman_PyMSM_Multistate_modeling_2022,\n    author = {Rossman, Hagai and Keshet, Ayya and Gorfine, Malka},\n    doi = {https://doi.org/10.5281/zenodo.6300873},\n    license = {MIT},\n    month = {2},\n    title = {{PyMSM, Multistate modeling in Python}},\n    url = {https://github.com/hrossman/pymsm},\n    year = {2022}\n}\n```\n\nAlso consider starring the project [on GitHub](https://github.com/hrossman/pymsm)\n\nThis project is based on methods first introduced by the authors of [Roimi et. al. 2021](https://academic.oup.com/jamia/article/28/6/1188/6105188).  \n Original R code by Jonathan Somer, Asaf Ben Arie, Rom Gutman, Uri Shalit & Malka Gorfine available [here](https://github.com/JonathanSomer/covid-19-multi-state-model).\n Also see [Rossman & Meir et. al. 2021](https://www.nature.com/articles/s41467-021-22214-z) for an application of this model on COVID-19 hospitalizations data.\n',
    'author': 'Hagai Rossman, Ayya Keshet, Malka Gorfine',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://hrossman.github.io/pymsm/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
