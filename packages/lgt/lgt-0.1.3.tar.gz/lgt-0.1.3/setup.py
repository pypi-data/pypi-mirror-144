# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['lgt',
 'lgt.group',
 'lgt.lattice',
 'lgt.lattice.su3.numpy',
 'lgt.lattice.su3.pytorch',
 'lgt.lattice.su3.tensorflow',
 'lgt.lattice.sun',
 'lgt.lattice.u1',
 'lgt.lattice.u1.numpy',
 'lgt.lattice.u1.pytorch',
 'lgt.lattice.u1.tensorflow']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=8.2.0,<9.0.0',
 'itermplot>=0.331,<0.332',
 'numpy>=1.22.3,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'tensorflow>=2.8.0,<3.0.0',
 'torch>=1.11.0,<2.0.0']

setup_kwargs = {
    'name': 'lgt',
    'version': '0.1.3',
    'description': 'Python library for Lattice Gauge Theory',
    'long_description': None,
    'author': 'Sam Foreman',
    'author_email': 'saforem2@gmail.com',
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
