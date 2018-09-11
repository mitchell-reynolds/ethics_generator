import os.path

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

print("Downloading Morals")
morals = strip_headers(load_etext(5682)).strip()
print("Downloading Ethics")
ethics = strip_headers(load_etext(5684)).strip()


def save(filename, contents):

    name_and_folder = os.path.join("./texts/raw", filename)

    fh = open(name_and_folder, 'w')
    fh.write(contents)
    fh.close()

save("morals.txt", morals)
save("ethics.txt", ethics)