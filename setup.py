from setuptools import *
setup(
name="quaternionmath",
version="1.0.0",
description=("A simple Python library featuring a"
"\"Quaternion\" class, for dealing with Quaternion arithmetic."),
long_description="""
Quaternionmath consists of a "Quaternion" class, which defines the Quaternion
(four-dimensional) numbers. The class provides addition, subtraction,
multiplication, and division logic, as well as string and representation
information.
""",
author="Toby Govin-Fowler",
author_email="ttoobbyyninja@gmail.com",
url="https://github.com/tobygf/quaternionmath",
license="MIT",
classifiers=["Development Status :: 5 - Production/Stable",

               "Intended Audience :: Education",
               "Topic :: Scientific/Engineering :: Mathematics",

               "License :: OSI Approved :: MIT License",

               "Programming Language :: Python",
               "Programming Language :: Python :: 2",
               "Programming Language :: Python :: 3",
],
keywords="math quaternion",
packages=find_packages(),
)
