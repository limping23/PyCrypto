from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas==2.0.3", "pycoingecko==3.1.0"]

setup(
    name="limping",
    version="1.0.0",
    author="limping",
    description="A package to work with Cryptocurrency",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/limping23/PyCrypto/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: MIT License ::",
    ],
)