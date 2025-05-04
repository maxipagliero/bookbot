def count_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    words = file_contents.split()

    total_words = len(words)

    print(f"{total_words} words found in the document")

def character_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    letter_dict = {}

    for letter in file_contents.lower():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    
    print(letter_dict)