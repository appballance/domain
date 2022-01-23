from setuptools import setup
import os

DIRECTORY = os.path.dirname(__file__)

REQUIREMENTS = open(os.path.join(DIRECTORY, "requirements.txt")).read().split()
EXTRAS = {
    "async": ["aiohttp"],
    "fast_async": ["aiohttp", "cchardet", "aiodns"]
}
VERSION = subprocess.run(["git", "describe", "--tags"],  stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
# READ_ME = open(os.path.join(DIRECTORY, "README.rst")).read()

setup(
    name="balance_domain",
    version=VERSION,
    author="Calenzo",
    author_email="henriquecalenzo2018@gmail.com",
    license="MIT License",
    description="An API wrapper for the online game, Akinator, written in Python",
    long_description="Readme description",
    long_description_content_type="text/x-rst",
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
