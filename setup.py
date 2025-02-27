from setuptools import setup, find_packages

setup(
    name="new-python-package",  # Nom de ton package
    version="0.1.0",            # Version du package
    packages=find_packages(),
    install_requires=[          # Liste des dépendances
        "flake8",
        "pytest",
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
