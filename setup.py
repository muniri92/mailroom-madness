# _*_ coding utf-8 _*_
from setuptools import setup

setup(
    name="mailroom",
    description="A mailroom application.",
    version=0.1,
    author="Munir Ibrahim",
    author_email="mibrah04@gmail.com",
    license="MIT",
    py_modules=["mailroom"],
    package_dir={'': 'mailroom'},
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
