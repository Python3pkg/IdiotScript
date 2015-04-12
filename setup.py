#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="idiotscript",
      version="1.1.1",
      description="An easier, less powerful alternative to regular expressions",
      author="Matthew Gamble",
      author_email="git@matthewgamble.net",
      url="https://github.com/djmattyg007/IdiotScript",
      download_url="https://github.com/djmattyg007/IdiotScript/archive/1.1.1.zip",
      packages=find_packages(),
      scripts=['bin/idiotscript.py'],
      package_data={'idiotscript': ['README.rst']},
      data_files=[('share/doc/python-idiotscript', ['README.txt', 'LICENSE.txt'])],
      license="UNLICENSE",
      install_requires=[]
      )

