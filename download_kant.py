from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

print("Downloading Morals")
morals = strip_headers(load_etext(5682)).strip()
print("Downloading Ethics")
ethics = strip_headers(load_etext(5684)).strip()