#!/usr/bin/env python3

import os
import sys
import platform
from setuptools import setup, find_packages

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = []
setup(
  name = "pymoji",
  version = "1.0",
  packages = ["pymoji"],
  scripts = [],
  install_requires = requirements,

  author = "Felix \"KoffeinFlummi\" Wiegand",
  author_email = "koffeinflummi@gmail.com",
  description = "emoji-cheat-sheet converter",
  long_description = read("README.md"),
  license = "MIT",
  keywords = "emoji emoticons unicode emoji-cheat-sheet",
  url = "https://github.com/KoffeinFlummi/pymoji",
  classifiers=[]
)
