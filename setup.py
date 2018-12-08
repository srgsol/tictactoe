#! -*- coding: utf-8 -*-
"""
Setup.
"""
from setuptools import setup, find_packages

setup(
    name='tictactoe',
    version='0.0.0',
    description='Tic Tac Toe. Adversarial search.',
    author='Sergi Soler i Segura',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tictactoe=tictactoe.main:main'
        ]
    }
)
