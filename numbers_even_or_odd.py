# read a number.txt
# number.txt with 20 integers
with open("number.txt", "r") as number_file:
    for line in number_file:
        number_txt_file = int(line)
        if number_txt_file % 2 == 0:
            open("even.txt", "w")
        else:
            print()
# create even.txt if number is even
# extract from number.txt
# create other odd.txt if number is odd
# extract from number.txt