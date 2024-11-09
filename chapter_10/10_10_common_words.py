# Common Words

from pathlib import Path

def count_common_words(file_path, word):
    
    path = Path(file_path)
    
    try:
        
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {file_path} does not exist.")
        return 0
    else:
        
        word_count = contents.count(word)
        print(f"The word '{word}' appears {word_count} times in {file_path}.")
        return word_count


count_common_words('/Users/noelito/CSC_141/where_the_west_beggins.txt', 'taken')

# I was able to do this exercise following the answers from github. 