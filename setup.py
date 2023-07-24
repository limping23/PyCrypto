from setuptools import setup, find_packages
import re


with open("README.rst", "r") as f:
    long_description = f.read()


with open("PyCrypto/__init__.py") as f:
    version = re.search(r"""^__version__\s*=\s*['"]([^\'"]*)['"]""", f.read(), re.MULTILINE).group(1)


setup(
    name="PyCrypto",
    version=version,
    author="limping",
    author_email="matvey.nemudrov@mail.ru",
    description="Get CryptoCurrencies info, prices, volume using Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/limping23/PyCrypto",
    download_url="https://github.com/limping23/PyCrypto/tarball/v" + version,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=None,
    python_requires='>=3.6',
)
