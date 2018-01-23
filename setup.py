#!/usr/bin/env python
from setuptools import setup, find_packages
import os


data_files = [(d, [os.path.join(d, f) for f in files])
              for d, folders, files in os.walk(os.path.join('src', 'config'))]

setup(name='fiery-snap',
      version='1.0',
      description='messaging for fiery-snap',
      author='Adam Pridgen',
      author_email='adpridge@cisco.com',
      install_requires=['toml', 'kombu', 'redis', 'validators',
                        'web.py', 'regex', 'python-twitter',
                        'bs4', 'pymongo', 'requests'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
)
