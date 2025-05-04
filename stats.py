def count_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    words = file_contents.split()
    
    total_words = 0

    for word in words:
        total_words += 1

    print(f"{total_words} words found in the document")