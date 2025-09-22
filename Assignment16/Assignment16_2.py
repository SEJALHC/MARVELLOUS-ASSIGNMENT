def main():
    filename=open('data.txt',"r")
    data=filename.read()
    print("file daa is:",data)

    filename.close()

if __name__=="__main__":
    main()