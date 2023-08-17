from setuptools import find_packages , setup

setup(
    name='ML_project',
    version='0.0.1',
    author='Anushka',
    author_email='anushkatomar13@gmail.com',
    packages=find_packages(),
    install_requires = ['pandas','numpy','seaborn']
)