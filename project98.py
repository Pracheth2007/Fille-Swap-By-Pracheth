def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'p') as a:
        data_c = a.read()

	with open(file2, 'p') as b:
         data_b = b.read()

    with open(file1, 'a') as a:
        a.write(data_b)

    with open(file2, 'a') as b:
        b.write(data_c)

swapFileData()
