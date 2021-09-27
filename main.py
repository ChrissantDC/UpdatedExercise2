# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# list_dir [path] [ouput_filename]
# list_dir d:\downloads my_output.csv
#
# Develop an application with the following requirements:
#
# Take the path of a directory and list the files (recursively)
# Output the files in a CSV (comma separated value) file.
# Here are the columns of the CSV: parent path, filename, filesize, sha1, md5
# Here's what a row should look like: "D:\Downloads","setup.exe",1048576, sha1-here, md5-here
# The output filename should be set by the user using command line arguments
# Commit your code in GitHub under the project listdir. Post the link to the project here

import sys

#  Sample output in cmd: python PycharmProjects\Exercise2\main.py  C:\Users\delac\PycharmProjects\Exercise2 E.csv
from configparser import ConfigParser

print(f"The name of the script is: {sys.argv[0]}")
folder_path = (r"" + sys.argv[1])

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

import glob
import hashlib
import pathlib
import os

file_path = []
txt_files = []
files_size = []
sha1 = []
md5 = []


# STEP 1: Get files and store them to array
# STEP 2: Get path of each file from the array
# STEP 3: Get file name
# STEP 4: Get Sha1
# STEP 5: Get md5
# STEP 6: Follow the format and save to csv

def get_file():
    # This function will list down the file names in an array

    for text_file in glob.glob(folder_path + "\*.txt"):
        # For some reason, if I make this *.*, a problem with hashing occurs. I will ask for help regarding this
        txt_files.append(text_file)
        print(txt_files)
    print(folder_path+"*.txt")

# print(txt_files)


def print_path(path):
    # This function will collect the paths of the file
    file_path.append(str(pathlib.Path(path).parent.resolve()))


def hash_file(filename):
    # This function returns the SHA-1 hash
    # of the file passed into it

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as hashfile:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = hashfile.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    sha1.append(h.hexdigest())
    return h.hexdigest()


def file_size(filename):
    file_name = os.path.getsize(filename)
    files_size.append(file_name)
    return file_name


def get_md5(filename):
    with open(filename, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    md5.append(file_hash.hexdigest())  # to get a printable str instead of bytes


get_file()
for file in txt_files:
    print_path(file)
    file_size(file)
    hash_file(file)
    get_md5(file)

# text = input("prompt ")
# print("you entered " + text)
# with open(input("Enter Desired File Name: "), "w") as Test_Write:
completeName = os.path.join(folder_path, sys.argv[2])
print('name is: ' + completeName)

with open(completeName, "w") as Test_Write:
    first_column = "Parent path \t filename \t filesize \t sha1 \t md5"
    row = ""
    i = 0
    print(len(txt_files))
    for i in range(len(txt_files)):
        row += file_path[i] + ",\t" + txt_files[i] + ",\t" + str(files_size[i]) + ",\t" + sha1[i] + ",\t" + md5[
            i] + "\n"
    Test_Write.write(row)


def config_parser():
    # FOR READING:
    # f = 'config.ini'
    # config = ConfigParser()
    # config.read(f)
    #
    # print(config.sections())
    # print(config['account'])
    # print(list(config['account']))
    # print(config['account']['pin'])

    # FOR WRITING:
    conf_path = os.path.join(folder_path, sys.argv[3])
    config = ConfigParser()
    config.add_section('Parent path')
    config.add_section('File Names')
    config.add_section('File Sizes')
    config.add_section('sha1')
    config.add_section('md5')
    j = 0
    for j in range(len(txt_files)):
        config.set('Parent path', txt_files[j], file_path[j])
        config.set('File Names', txt_files[j], txt_files[j])
        config.set('File Sizes', txt_files[j], str(files_size[j]))
        config.set('sha1', txt_files[j], sha1[j])
        config.set('md5', txt_files[j], str(md5[j]))
        print(len(txt_files))

        with open(conf_path, 'w') as configfile:
            config.write(configfile)


config_parser()


# print("you entered " + sys.argv[1])
# print(str(txt_files))
# print(file_path)
# print(sha1)
# for files in txt_files:
#     fs = file_size("A.txt")
# print("File Size is :", fs, "bytes")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
