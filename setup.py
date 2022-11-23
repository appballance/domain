from setuptools import setup, find_packages
import subprocess
import os

DIRECTORY = os.path.dirname(__file__)

REQUIREMENTS = open(os.path.join(DIRECTORY, "requirements.txt")).read().split()

VERSION = subprocess.run(['git', 'describe', '--tags'],  stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in VERSION

READ_ME = open(os.path.join(DIRECTORY, "README.rst")).read()

setup(
    name="balance_domain",
    version=VERSION,
    author="Calenzo",
    author_email="calenzodevs@gmail.com",
    license="MIT License",
    description=READ_ME,
    long_description="Readme description",
    long_description_content_type="text/x-rst",
    install_requires=REQUIREMENTS,
    url="https://pypi.org/project/balance-domain",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
