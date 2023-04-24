# read a number.txt
# number.txt with 20 integers
with open("number.txt", "r") as number_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:
    for line in number_file:
        number_txt_file = int(line)
        # create even.txt if number is even
        if number_txt_file % 2 == 0:
            even_file.write(str(number_txt_file) + "\n")
        # extract from number.txt
        # create other odd.txt if number is odd
        else:
            odd_file.write(str(number_txt_file) + "\n")
        # extract from number.txt