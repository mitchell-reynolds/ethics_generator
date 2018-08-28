****************
Ethics Generator
****************

With Motivation of the Pioneer.app Project

The aim of this project is to recreate various moral philosophers views. 
With the rise of Artificial Intelligence, the impetus to translate human values into a machine-readable format has never been more necessary.
  
The first moral philosopher to be pursued will be Immanuel Kant as I've extensively studied his ethics and find his arguments to compelling.

Installation
============

This project uses `PyPI <https://pypi.python.org/pypi/Gutenberg>`_, so I'd
recommend that you just install everything from there using your favourite
Python package manager.

.. sourcecode :: sh

    pip install gutenberg
  
  
Python 3
--------

This package depends on BSD-DB. The bsddb module was removed from the Python
standard library since version 2.7. This means that if you wish to use gutenberg
on Python 3, you will need to manually install BSD-DB.

  
MacOS
*****

On Mac, you can install BSD-DB using `homebrew <https://homebrew.sh/>`_:

.. sourcecode :: sh

    brew install berkeley-db4
    pip install -r requirements-py3.pip
