def openFile(givenFile):
    try:
        with open(givenFile,'r') as f:
            contents = f.read()
            print(contents)
    except Exception:
        print(f"{givenFile} is not present.")

openFile('1.txt') 
openFile('2.txt') 
openFile('3.txt') 
openFile('4.txt') 