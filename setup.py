try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sintervals

metadata = dict(name='sintervals',
                maintainer='Nick Kypreos',
                maintainer_email='nickkypreos@gmail.com',
                description='',
                license='',
                url='',
                version=sintervals.__version__,
                download_url='',
                long_description='',
                py_modules=['sintervals'])

setup(**metadata)
