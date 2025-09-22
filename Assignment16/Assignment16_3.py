def counter(file1):
    counter=0
    filename=open(file1,"r")
    line_count=0
    word_count=0
    for line in filename.readlines():
        line_count+=1
        for word in line.split():
            word_count+=1
            for c in word:
                counter+=1

    print("word count:",word_count)
    print("line count:",line_count)
    print("chsr count:",counter)

    filename.close()