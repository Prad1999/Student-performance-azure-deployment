from setuptools import find_packages, setup

setup(
    name='mlproject',
    version='0.0.1',
    author='Pradurshan',
    author_email='prad10@hotmail.co.uk',
    package=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
