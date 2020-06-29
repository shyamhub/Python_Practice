import os

def create_file():
    print("****In Create File Method")
    print("The Current path is:" ,os.getcwd()+'\Shyam.txt')
    f = open("demofile.txt",'w+')
    #f.write()


def write_file():
    print("****In Write File Method")
    f=open("demofile.txt",'a')
    f.write("This is a new File")

def read_file():
    print("****In Read File Method")
    f = open("demofile.txt", 'r')
    for line in f:
        print(line)

def delete_file():
    print("****In Delete File Method")
    os.remove("demofile.txt")



create_file()
write_file()
read_file()
#delete_file()