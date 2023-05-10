from setuptools import setup, find_packages

setup(
    name='py_calculator',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pycal = py_calculator.__main__:main'
        ]
    },
    install_requires=[
        'fractions',
    ],
    description='A simple calculator program.',
)