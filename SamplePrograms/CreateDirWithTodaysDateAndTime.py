from datetime import datetime
import os

def create_directory():
    try:
        today = datetime.now()
        print("Today's Date :",today)
        filename = today.strftime('%Y-%m-%d_%H%M%S')
        print("File Name: ", filename)
        os.mkdir(filename)
        print("File created")
    except:
        os.error("Unable to Create Directory")

def delete_directory(file_name):
    try:
        os.rmdir(file_name)
    except:
        os.error("Unable to Delete the file")

#delete_directory("C:\\Users\\shan1260\\PycharmProjects\\Practice\\SamplePrograms\\2020-06-29_0113")
if __name__ == "__main__":
    print ("__name__ :", __name__)
    create_directory()