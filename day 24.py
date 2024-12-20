Placeholder = "[name]"
with open("day 25_1.txt") as names_file:
    names = names_file.readlines()
    print(names)
with open("day 25_2.txt") as letter_file:
    letter_content =  letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(Placeholder, stripped_name)
        print(new_letter)