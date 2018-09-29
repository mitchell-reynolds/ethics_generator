import sys
import os.path

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

def main(filename, gb_num):
    """
    Saves the Gutenberg work found from the website using the `gutenberg` Python library

    Website: http://www.gutenberg.org/

    :parameter
    filename : the txt file that is specified by the user
    gb_num : the Gutenberg Number found from the Website listed above


    :return
    Saves the raw Gutenberg book into the texts/raw folder to be further processed
    """

    print("Downloading " + filename)
    contents = strip_headers(load_etext(gb_num)).strip()

    name_and_folder = os.path.join("./texts/raw/", filename)

    fh = open(name_and_folder, 'w')
    fh.write(contents)
    fh.close()


gutenberg_dict = {"ethics.txt": 5684,
                  "morals.txt": 5682,
                  "reason.txt": 4280,
                  "prolegomena.txt": 52821,
                  "books.txt": 46060
                  }

if __name__ == '__main__':
    for txt, num in gutenberg_dict.items():
        main(txt, num)
