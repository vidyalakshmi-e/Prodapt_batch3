# file=open('example.txt','r')
# data=file.read()
# print(data)
# file.close()

def read_file(filename):
    try:
        file=open(filename,'r')
        data=file.read()
        print(data)
    except FileNotFoundError:
        print(f"Error: the file '{filename} was not found")
    except IOError:
        print(f"Error: An I/O error occurred while reading the file")
    except Exception as e:
        print(f"Erro: '{e}")
    finally :
        if 'file' in locals():
            file.close()
readfilename=input("enter the filename to read")
read_file(readfilename)