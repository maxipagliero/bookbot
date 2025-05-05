def book_stats(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()


    letter_dict = {}

    for letter in file_contents.lower():
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    
    items = list(letter_dict.items())

    items.sort(key=lambda item: item[1], reverse=True)

    words = file_contents.split()

    total_words = len(words)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in items:
        print(f"{item[0]}: {item[1]}")
    print("============= END ===============")