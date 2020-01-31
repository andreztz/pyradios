from setuptools import setup
from setuptools import find_packages
from setuptools.command.develop import develop
from setuptools.command.develop import develop as DevelopCommand
import pip


DESCRIPTION = (
    "A Python wrapper for the http://www.radio-browser.info/webservice"
)


def readme():
    with open("README.md") as f:
        return f.read()


def required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


dev_requirements = ["pytest"]


class CustomDevelopCommand(DevelopCommand):
    def run(self):
        super().run()
        pip.main(["install"] + dev_requirements)


setup(
    name="pyradios",
    version="0.0.18",
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="pyradios wrapper radios api",
    author="André P. Santos",
    author_email="andreztz@gmail.com",
    url="https://github.com/andreztz/pyradios",
    license="MIT",
    packages=find_packages(),
    install_requires=required(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    cmdclass={"develop": CustomDevelopCommand},
)
