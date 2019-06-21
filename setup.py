# -*- coding: UTF-8 -*-
from os.path import dirname, realpath, join as path_join
from setuptools import setup, find_packages

package = 'marsh_schema_piapia'


def valid_requirement(line):
    if not line:
        return False
    else:
        ch = line[0]
        return ch not in ('#', '-')


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    root = dirname(realpath(__file__))
    line_iter = (line.strip() for line in open(path_join(root, filename)))
    return [line for line in line_iter if valid_requirement(line)]


setup(
    name=package,
    version='0.0.1',
    description='marsh_schema_piapia',
    url='',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
)
