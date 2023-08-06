import setuptools
from distutils.core import  setup

packages = ['LyScript32']

setup(
    name='LyScript32',
    version='1.0.10',
    author='lyshark',
    description='A powerful x64dbg remote debugging module',
    author_email='me@lyshark.com',
    python_requires=">=3.6.0",
    license = "MIT Licence",
    packages=packages,
    include_package_data = True,
    platforms = "any"
    )