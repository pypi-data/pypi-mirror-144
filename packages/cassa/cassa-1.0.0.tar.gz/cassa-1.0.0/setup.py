# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cassa']

package_data = \
{'': ['*']}

install_requires = \
['dask>=2022.2.1,<2023.0.0',
 'numpy>=1.22.3,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'sklearn>=0.0,<0.1']

setup_kwargs = {
    'name': 'cassa',
    'version': '1.0.0',
    'description': 'Python package to perform unsupervised and semi-supervised machine learning (ML) classification algorithms on generic tensors of pre-processed data',
    'long_description': None,
    'author': 'Karl Nordstrom',
    'author_email': 'karl.am.nordstrom@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
