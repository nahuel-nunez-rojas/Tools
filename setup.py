from setuptools import setup, find_packages

setup(
    name = "eda",
    version = "0.1",
    description = "Exploratory Data Analysis",
    author = "Nahuel Nuñez Rojas",
    packages = find_packages(),
    install_requires = [
        "pandas",
    ]
)