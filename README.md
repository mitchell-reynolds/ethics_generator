# Ethics Generator


_With Motivation of the [Pioneer.app Tournament](https://pioneer.app/)_

The aim of this project is to recreate various moral philosophers views. 
With the rise of Artificial Intelligence, the impetus to translate human values into a machine-readable format has never been more necessary.
  
The first moral philosopher to be pursued will be Immanuel Kant as I've extensively studied his ethics and 
find his arguments to compelling.

Installation
============

This project is in Python 3 and uses [Gutenberg](https://pypi.python.org/pypi/Gutenberg) to download text data.

    conda env create -f environment.yml
    conda activate ethics

  
Python 3
--------

This package depends on BSD-DB. The bsddb module was removed from the Python
standard library since version 2.7. This means that if we wish to use Gutenberg
on Python 3, you will need to manually install BSD-DB. 
If you're not on a Mac, go directly to the [Gutenberg](https://pypi.org/project/Gutenberg/).

On Mac, you can install BSD-DB using [homebrew](https://homebrew.sh/):

    brew install berkeley-db4
    pip install -r requirements.txt

Downloading Texts of Immanuel Kant
----------------------------------

The raw text data will go into the `texts` folder where it will be cleaned up further. 
After running this, you should have an [`ethics.txt`](http://www.gutenberg.org/ebooks/5684) 
and [`morals.txt`](http://www.gutenberg.org/ebooks/5682) file for his two major works in morality. The initial focus will be on his Morals text.

    python download_kant.py

Cleaning Data
-------------

TODO
