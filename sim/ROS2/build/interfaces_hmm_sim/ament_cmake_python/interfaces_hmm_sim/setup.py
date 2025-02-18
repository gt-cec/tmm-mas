from setuptools import find_packages
from setuptools import setup

setup(
    name='interfaces_hmm_sim',
    version='0.0.0',
    packages=find_packages(
        include=('interfaces_hmm_sim', 'interfaces_hmm_sim.*')),
)
