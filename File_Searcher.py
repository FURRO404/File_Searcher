#==============FURRO404==============#
#File_Searcher.py
import os
#--------------#
x = 0
drives = ["C:\\", "X:\\"]
#Enter your own drives into the above list

dir_path = os.path.dirname(drives[x]) 
#---------------------------------------------------------#
a = str(input("(1) Keyword Search\n(2) File Type Search\n(3) Keyword and File Type Search\nCommand ~ "))
print("\n\n\n")

if a == "1":
    choice = str(input("Keyword: "))
    
    print("\n\n")
    for i in drives:
         for root, dirs, files in os.walk(dir_path):
             for file in files:
                 if choice in file:
                     print ("\n" + root+'\\'+str(file))
         dir_path = os.path.dirname(drives[x+1])
#---------------------------------------------------------#
elif a == "2":
    ext = str(input("File type: "))
    
    print("\n\n")
    for i in drives:
        for root, dirs, files in os.walk(dir_path): 
            for file in files:  
                if file.endswith(ext): 
                    print ("\n" + root+'\\'+str(file))
        dir_path = os.path.dirname(drives[x+1])
#---------------------------------------------------------#
elif a == "3":
    choice = str(input("Keyword: "))
    ext = str(input("File type: "))

    print("\n\n")
    for i in drives:
        for root, dirs, files in os.walk(dir_path): 
            for file in files:  
                if choice in file and file.endswith(ext): 
                    print ("\n" + root+'\\'+str(file))
        dir_path = os.path.dirname(drives[x+1]) 
#==============FURRO404==============#
