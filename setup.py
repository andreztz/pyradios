from setuptools import setup
from setuptools import find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="pyradios",
    version="0.0.2",
    description="A Python wrapper for the http://www.radio-browser.info/webservice",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="pyradios wrapper radios api",
    author="André P. Santos",
    author_email="andreztz@gmail.com",
    url="https://github.com/andreztz/pyradios",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent"],
)
