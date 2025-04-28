import io
from setuptools import setup
from setuptools import find_packages


DESCRIPTION = "Python client for the Radio Browser API"


def readme():
    with io.open("README.md", "r", encoding="utf-8") as f:
        return f.read()


def required(sfx=''):
    with open(f"requirements{sfx}.txt") as f:
        return f.read().splitlines()


setup(
    name="pyradios",
    version="2.1.0.dev2",
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="pyradios wrapper radios api",
    author="André P. Santos",
    author_email="andreztz@gmail.com",
    url="https://github.com/andreztz/pyradios",
    license="MIT",
    packages=find_packages(exclude=["test*"]),
    install_requires=required(),
    extras_require={'dev': required('-dev')},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.9",
    project_urls={
        "Source": "https://github.com/andreztz/pyradios/",
        "Upstream": "https://api.radio-browser.info/",
    },
)
