#Chapter 16 Notes

#Open a file:
#f = open('users.txt'); f
#users = f.readlines()
#users

#Close a file
#f.close; f

#f.readline -> reads one line
#Once out of readlines, Python returns an empty string

#Writing data to files:
#send 'r+w', read and write through open to open a file without erasing its contents
#Ex:
#f = open('users.txt', 'r+w')
#f.write('test')
#f.close()
#f = open('users.txt')
#lines = f.readlines()
#for line in lines:
    #print lines

#Opening a file in write mode:
#Ex:
#f = open('users.txt', 'w')

#Other functions of file streams:
#writelines() -> writes each of them in the list to the file

#Appending data to files:
#f = open('users.txt', 'a')

#Creating Files:
#f = open('tmp.txt', 'w+')
#f.write("this is a new file")
#f.closes()

#Lists of Files
#import os
#os.getcwd()

#import os
#os.listdir('.')

#Making new directories
#makedir
