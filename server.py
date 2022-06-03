import socket
import os
import random
ip = "127.0.0.1"
port = 8888
format = "utf-8"
size = 1024

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen()

    app_list = ["(1) - Calculator", "(2) - File Editor", "(3) - Random code generator", "(quit) - Quit program"]
    program1_list = ["(1) - Sum", "(2) - Sub", "(3) - Mul", "(4) - Div", "(5) - Back"]
    program2_list = ["(1) - Write to file (overwrite) (extension: .txt)", "(2) - Append to file (must exist)", "(3) - Clear file (must exist)", "(4) - Read file (must exist)", "(5) - Back"]
    program3_list = ["(1) - Only letters", "(2) - Only numbers", "(3) - Only characters", "(4) - Everything", "(5) - Back"]
    while True:
        conn, addr = server.accept()
        print("Client connected!")

        while True:
            #client connection
            conn.send(str(app_list).encode(format))

            #program selection
            res = conn.recv(size).decode(format)
            if res == "1":
                while True:
                    conn.send(str(program1_list).encode(format))
                    res = conn.recv(size).decode(format)
                    if res == "1":
                        sum = 0
                        nr1 = conn.recv(size).decode(format)
                        nr2 = conn.recv(size).decode(format)
                        sum = int(nr1) + int(nr2)
                        conn.send(str(sum).encode(format))
                        break
                    elif res == "2":
                        sub = 0
                        nr1 = conn.recv(size).decode(format)
                        nr2 = conn.recv(size).decode(format)
                        sub = int(nr1) - int(nr2)
                        conn.send(str(sub).encode(format))
                        break
                    elif res == "3":
                        mul = 0
                        nr1 = conn.recv(size).decode(format)
                        nr2 = conn.recv(size).decode(format)
                        mul = int(nr1) * int(nr2)
                        conn.send(str(mul).encode(format))
                        break
                    elif res == "4":
                        div = 0
                        nr1 = conn.recv(size).decode(format)
                        nr2 = conn.recv(size).decode(format)
                        div = int(nr1) / int(nr2)
                        conn.send(str(div).encode(format))
                        break
                    elif res == "5":
                        break
                    else:
                        break
            elif res == "2":
                while True:
                    path = r"C:\Users\Cristi\Desktop\pythonProjectRetele"
                    text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
                    conn.send(str(text_files).encode(format))
                    conn.send(str(program2_list).encode(format))
                    res = conn.recv(size).decode(format)
                    if res == "1":
                        file_name = conn.recv(size).decode(format)
                        text = conn.recv(size).decode(format)
                        f = open(file_name, "w")
                        f.write(text)
                        f.close()
                        break
                    elif res == "2":
                        file_name = conn.recv(size).decode(format)
                        text = conn.recv(size).decode(format)
                        f = open(file_name, "a")
                        f.write(text)
                        f.close()
                        break
                    elif res == "3":
                        file_name = conn.recv(size).decode(format)
                        f = open(file_name, "w")
                        f.write("")
                        f.close()
                        break
                    elif res == "4":
                        file_name = conn.recv(size).decode(format)
                        f = open(file_name, "r")
                        text = f.read()
                        if text == "":
                            text = "Fisierul este gol!"
                        conn.send(text.encode(format))
                        f.close()
                        break
                    elif res == "5":
                        break
                    else:
                        break
            elif res == "3":
                while True:
                    conn.send(str(program3_list).encode(format))
                    res = conn.recv(size).decode(format)
                    if res == "1":
                        length = conn.recv(size).decode(format)
                        result = ''.join(
                            (random.choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")) for x in
                            range(int(length)))
                        conn.send(result.encode(format))
                        break
                    elif res == "2":
                        length = conn.recv(size).decode(format)
                        result = ''.join(
                            (random.choice("1234567890")) for x in
                            range(int(length)))
                        conn.send(result.encode(format))
                        break
                    elif res == "3":
                        length = conn.recv(size).decode(format)
                        result = ''.join(
                            (random.choice("`!@#$%^&*()-=_+[]{};'\:|,./<>?")) for x in
                            range(int(length)))
                        conn.send(result.encode(format))
                        break
                    elif res == "4":
                        length = conn.recv(size).decode(format)
                        result = ''.join(
                            (random.choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890`!@#$%^&*()-=_+[]{};'\:|,./<>?")) for x in
                            range(int(length)))
                        conn.send(result.encode(format))
                        break
                    elif res == "5":
                        break
                    else:
                        break
            if res == "quit":
                break
        conn.close()