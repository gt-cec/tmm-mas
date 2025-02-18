from setuptools import find_packages
from setuptools import setup

setup(
    name='ltl_automaton_msgs',
    version='0.1.0',
    packages=find_packages(
        include=('ltl_automaton_msgs', 'ltl_automaton_msgs.*')),
)
