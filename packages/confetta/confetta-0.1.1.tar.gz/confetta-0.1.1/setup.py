from setuptools import find_packages, setup


def find_required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


def find_dev_required():
    with open("requirements-dev.txt") as f:
        return f.read().splitlines()


setup(
    name="confetta",
    version="0.1.1",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="2GIS Test Labs",
    author_email="test-labs@2gis.ru",
    python_requires=">=3.7",
    url="https://github.com/2gis-test-labs/confetta",
    license="Apache-2.0",
    packages=find_packages(exclude=("tests",)),
    package_data={"confetta": ["py.typed"]},
    install_requires=find_required(),
    tests_require=find_dev_required(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
