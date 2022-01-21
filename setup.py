from setuptools import setup
import os

DIRECTORY = os.path.dirname(__file__)

REQUIREMENTS = open(os.path.join(DIRECTORY, "REQUIREMENTS.txt")).read().split()
EXTRAS = {
    "async": ["aiohttp"],
    "fast_async": ["aiohttp", "cchardet", "aiodns"]
}
VERSION = open(os.path.join(DIRECTORY, "akinator", "VERSION.txt")).read()
READ_ME = open(os.path.join(DIRECTORY, "README.rst")).read()

setup(
    name="akinator.py",
    version=VERSION,
    author="NinjaSnail1080",
    author_email="innuganti.ashwin@gmail.com",
    packages=["akinator", "akinator.async_aki"],
    package_data={
        "akinator": ["VERSION.txt"]
    },
    url="https://github.com/NinjaSnail1080/akinator.py",
    project_urls={
        "Documentation": "https://github.com/NinjaSnail1080/akinator.py/blob/master/README.rst",
        "Source": "https://github.com/NinjaSnail1080/akinator.py",
        "Tracker": "https://github.com/NinjaSnail1080/akinator.py/issues",
        "Say Thanks!": "https://saythanks.io/to/innuganti.ashwin%40gmail.com"
    },
    license="MIT License",
    description="An API wrapper for the online game, Akinator, written in Python",
    long_description=READ_ME,
    long_description_content_type="text/x-rst",
    keywords="akinator api",
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS,
    python_requires=">=3.5.3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Topic :: Utilities"
    ]
)