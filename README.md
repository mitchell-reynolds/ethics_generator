# Ethics Generator


_With Motivation of the [Pioneer.app Tournament](https://pioneer.app/)_

The aim of this project is to recreate various moral philosophers views. 
With the rise of Artificial Intelligence, the impetus to translate human values into a machine-readable format has never been more necessary.
  
The first moral philosopher to be pursued will be Immanuel Kant as I've extensively studied his ethics and 
find his arguments to compelling.

My initial explorations rely on [Samir Bajaj's work](https://github.com/samirbajaj-zz/cs224n-project) with summarizing
Shakespeare works. 

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
and [`morals.txt`](http://www.gutenberg.org/ebooks/5682) for his two major works in morality. 
The initial focus will be on his Morals text or "Fundamental Principles of the Metaphysic of Morals."

    python download_kant.py

Cleaning Data
=============

The `texts/processed` folder mirrors that of [Bajaj's](https://nlp.stanford.edu/courses/cs224n/2013/reports/bajaj.pdf) 
organization - ie the `processed` text file for morals has
the removal of the preface to only include Kant's words & thoughts. 

Run these commands in this order to create the full ethical `LEXICON` of Immanuel Kant.

`cd texts/processed`  
**lowercase all words**  
```for f in `ls *.txt`; do cat $f | tr '[[:upper:]]' '[[:lower:]]' > ../lowercase/$f; done```  

**Remove punctuation.**  
```cd ../lowercase && for f in `ls *.txt`; do cat $f | sed 's/[:;?!.,-]/ /g' | tr "'" " " > ../remove_punct/$f ; done```  

**Move up in the directory and Remove stop words**  
_If you use these scripts for other works, make sure to go into `remove_stop_words.py` to update the `book` name variable in `main()`_  
```cd ../.. && python remove_stop_words.py```  

**Stem Words**  
```cd texts/remove_stop_words && for f in `ls *.txt`; do python ../../porter.py $f > ../stemmed/$f ; done```  

**Create LEXICON**  
```cd ../.. && cat texts/stemmed/*.txt | tr ' ' '\n' | sed '/^\s+$/d' | sort | uniq -c > LEXICON```

TODO: 
-----
* Make `remove_stop_words.py` a command line utility
* Keep "i.e." as these scripts remove punctuation and the stopword "I", therefore leaving a floating "e"
* Remove numbers found in LEXICON version 1
