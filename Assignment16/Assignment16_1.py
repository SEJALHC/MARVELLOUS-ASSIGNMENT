def main():
    filename=open('student.txt',"w")
    filename.write("name of five students:"+"\n")
    filename.write("sejal"+"\n")
    filename.write("sujal"+"\n")
    filename.write("sajal"+"\n")
    filename.write("sanajna"+"\n")
    filename.write("seema"+"\n")

    filename.close()

    if __name__=="__main__":
        main()
    
