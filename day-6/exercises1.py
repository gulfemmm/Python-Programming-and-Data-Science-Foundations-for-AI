def  count_words_and_lines(filename):
    try:
        with open (filename,"r") as file:
            lines = file.readlines()
            line_count =len(lines)
            word_count = sum(len(line.split()) for line in lines)
            print(f"Number of lines:{line_count}")
            print(f"number of words:{word_count}")
    except FileNotFoundError:
        print(f"file{filename} not found!")
count_words_and_lines("sample.txt")