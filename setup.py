from setuptools import setup, find_packages

package = 'depr'
version = '0.1.5'

setup(name=package,
      version=version,
      packages=['depr'],
      description="Deprecation decorator",
      author="Andrea Crotti",
      author_email="andrea.crotti.0@gmail.com",
      license='MIT',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy"],
      url='https://github.com/AndreaCrotti/depr')
