import os
def FileExists(filename):
    check = os.path.exists(filename)
    
    if(check == True):
        print("The file is exists in current directory")
    else:
        print("The file is not exists in current directory")        
    
def main():
    print("Enter your File Name :")
    filename = input()
    
    FileExists (filename)

if __name__ == "__main__":
    main()