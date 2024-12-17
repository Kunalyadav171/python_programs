# st = "hey i'am yash "

# f = open("python /my_file.txt","w")
# contant = f.write(st)
# f.close()

with open("python /my_file.txt") as f:
    print(f.read())