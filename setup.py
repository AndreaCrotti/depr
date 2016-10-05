from setuptools import setup, find_packages


def get_version():
    import git
    return git.Repo('.').tags[-1].name

package = 'depr'

setup(name=package,
      version=get_version(),
      packages=['depr'],
      description="Deprecation decorator",
      author="Andrea Crotti",
      setup_requires=["GitPython>=2.0"],
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
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy"],
      url='https://github.com/AndreaCrotti/depr')
