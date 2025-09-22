def mark():
    fobj = open("mark.txt",'r')

    for i in fobj.readlines():
        data= i.split()
        if int(data[1])>75:
            print(data)

def main():
    mark()

if __name__=="__main__":
    main()