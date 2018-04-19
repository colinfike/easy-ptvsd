"""Setup.py file for easy_ptvsd."""
from setuptools import setup

setup(
    name="easy_ptvsd",
    version="0.1.1",
    description="A convenience package for PTVSD.",
    long_description=(
        "EasyPtvsd is a convenience library that makes it a bit easy to remote"
        + " debug with ptvsd without having to remember the function calls and all"
        + " that. It currently provides a decorator that can be used to setup the ptvsd"
        + " server, wait for attachment, then immediately break into the debugger."
    ),
    url="https://github.com/colinfike/easy-ptvsd",
    author="Colin Fike",
    author_email="colin.fike@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3",
    ],
    keywords="ptvsd easy python remote debugging",
    install_requires=["ptvsd==3.0.0"],
    python_requires=">=3",
    py_modules=["easy_ptvsd"],
    packages=[],
)
