import socket
ip = "127.0.0.1"
port = 8888
format = "utf-8"
size = 1024

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))

    while True:
        #client recieves program list
        res = client.recv(size).decode(format)
        print(res)

        #client selects program
        req = input("Select a program!\n")
        client.send(req.encode(format))

        if str(req) == "1":
            # client recieves info about program operations
            res = client.recv(size).decode(format)
            print(res)

            req = input("Select an operation!\n")
            client.send(req.encode(format))

            if str(req) != "5":
                nr1 = input("Select the first number!\n")
                nr2 = input("Select the second number!\n")
                client.send(nr1.encode(format))
                client.send(nr2.encode(format))
                res = client.recv(size).decode(format)
                print(res)
        elif str(req) == "2":
            # client recieves info about program operations
            print("All files with .txt:")
            res = client.recv(size).decode(format)
            print(res)
            res = client.recv(size).decode(format)
            print(res)

            req = input("Select an operation!\n")
            client.send(req.encode(format))

            if str(req) != "5":
                file_name = input("Select the file name! (+extension)\n")
                client.send(file_name.encode(format))
                if str(req) not in ["3","4"]:
                    text = input("Type what you want to write!\n")
                    client.send(text.encode(format))
                if str(req) == "4":
                    res = client.recv(size).decode(format)
                    print(res)
        elif str(req) == "3":
            res = client.recv(size).decode(format)
            print(res)

            req = input("Select an operation!\n")
            client.send(req.encode(format))

            if str(req) != "5":
                length = input("Select the length of the code!\n")
                client.send(length.encode(format))

                res = client.recv(size).decode(format)
                print(res)
        if req == "quit":
            break