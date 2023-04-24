# read a number.txt
# number.txt with 20 integers
with open("number.txt", "r") as number_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:
    for line in number_file:
        number_txt_file = int(line)
        if number_txt_file % 2 == 0:
            # extract from number.txt
            # create even.txt if number is even
            even_file.write(str(number_txt_file) + "\n")
        else:
            # extract from number.txt
            # create other odd.txt if number is odd
            odd_file.write(str(number_txt_file) + "\n")
