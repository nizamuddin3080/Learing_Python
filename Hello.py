'''
with open("loremipsam.txt", mode="r") as s_file:
    word_all = []
    for line in s_file.readlines():
        word = line.strip().split()
        word_all += word
        # stripped_string = line.strip()
        # print(stripped_string.split(" "))
        unique_word = set(word_all)
        print(len(word_all))
        print(len(unique_word))

        # print(len(line))

        with open("unique_word.txt", mode="w") as write_file:
            for item in sorted(unique_word):
                write_file.write(item)
                write_file.write("\n")

print("finished")
'''

# debugging mode
#
# username = input("Your Name: ")
#
# value = 1
#
# new_string: int = value+username
#
# print(new_string)