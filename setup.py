from setuptools import setup
from setuptools import find_packages
from setuptools.command.develop import develop
from setuptools.command.develop import develop as DevelopCommand
from setuptools.command.test import test as TestCommand



DESCRIPTION = (
    "A Python wrapper for the http://www.radio-browser.info/webservice"
)


def readme():
    with open("README.md") as f:
        return f.read()


def required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


# import pip
# dev_requirements = []


# class CustomDevelopCommand(DevelopCommand):
#     def run(self):
#         super().run()
#         pip.main(["install"] + dev_requirements)


class CustomTestCommand(TestCommand):
    # https://pytest.readthedocs.io/en/2.7.3/goodpractises.html#integrating-with-distutils-python-setup-py-test
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

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
    tests_require=['pytest'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    cmdclass={"test": CustomTestCommand},
)
