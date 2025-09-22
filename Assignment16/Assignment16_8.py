def blank():
    fobj1=open("Demo.txt",'r')

    fobj2=open("Demo1.txt",'w')

    for line in fobj1.readlines():
        line_copy=line
        line=line.replace("","")
        line=line.replace("\n","")
        if(line==""):
            continue
        else:
            fobj2.write(line_copy)

        fobj1.close()
        fobj2.close()

def main():
    blank()

if __name__=="__main__":
    main()