from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(name='pyffs',
      version='1.0',
      description='Python implementation of Leveshtein automata',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/antoinewdg/pyffs',
      author='Antoine Wendlinger',
      author_email='antoinewendlinger@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Text Processing :: Linguistic"
      ],
      )
