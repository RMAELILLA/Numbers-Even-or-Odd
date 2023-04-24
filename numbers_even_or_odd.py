# read a number.txt
# number.txt with 20 integers
with open("number.txt", "r") as number_file:
    for line in number_file:
        number_txt_file = int(line)
        # create even.txt if number is even
        if number_txt_file % 2 == 0:
            even_file = number_txt_file
            even_file = open("even.txt", "w")
            even_file.write(str(number_txt_file) + "\n")
        else:
            print()
# extract from number.txt
# create other odd.txt if number is odd
# extract from number.txt