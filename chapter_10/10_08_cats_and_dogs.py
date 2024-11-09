# Cats and Dogs

from pathlib import Path

def cats_and_dogs(*file_paths):
   for file_name in file_paths:
        path = Path(file_name)
        try:
            contents = path.read_text(encoding='utf-8')
        except FileNotFoundError:
            print(f"Sorry, the file {file_name} does not exist.")
        else:
            print(f"Contents of {file_name}:")
            print(contents)
            print()
cats_and_dogs('cats.txt', 'dogs.txt')

# Tricky exercise, got it running after testing for errors using chat. 