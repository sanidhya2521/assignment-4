text_to_write = input("enter text to write: ")
file1 = open('output.txt', 'w' )
file1.write(text_to_write + "\n")
file1.close()

text_to_append = input("enter text to append: ")
file1 = open('output.txt', 'a')
file1.write(text_to_append)
file1.close()

print("final content of output.txt: ")
file1 = open('output.txt', 'r')
print(file1.read())