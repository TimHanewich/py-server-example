import socket

HOST = "0.0.0.0" # 0.0.0.0 defaults to using the device's IP address.
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
    print("Now waiting for connection...")
    conn, addr = s.accept()
    print("Connection from " + str(addr) + "!")
    data:bytes = conn.recv(1024)
    print(str(len(data)) + " bytes received!")

    # print the content
    print("Content received: " + str(data))

    # send 200 OK
    conn.send("HTTP/1.0 200 OK\r\n\r\n".encode("utf-8"))
    conn.close()

