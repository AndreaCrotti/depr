from setuptools import setup, find_packages

from depr import __version__

def _get_version():
    with open('VERSION', 'r') as f:
        return f.read().strip(' \n\rv')

package = 'depr'

setup(name=package,
      version=_get_version(),
      packages=['depr'],
      description="Deprecation decorator",
      author="Andrea Crotti",
      author_email="andrea.crotti.0@gmail.com",
      license='MIT',
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy"],
      url='https://github.com/AndreaCrotti/depr')
