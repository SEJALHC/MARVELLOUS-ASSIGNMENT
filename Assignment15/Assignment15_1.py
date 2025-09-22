import os 
def FileExist(filename):
    check=os.path.exists(filename)

    if(check==True):
        print("thefile is existing in current directory")

    else:
        print("the file does not exists in currenct directory")


    def main():
        print("enter your file name:")
        filename=input()

        FileExist(filename)


    if __name__=="__main__":
        main()