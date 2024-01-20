import socket
import time
import json

HOST = "0.0.0.0" # 0.0.0.0 defaults to using the device's IP address.
PORT = 80 # 80 is default HTTP port, so you could call ONLY the device's IP address to access... BUT, it requires sudo/root permissions

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Binding to host '" + HOST + "' and port '" + str(PORT) + "'...")
s.bind((HOST, PORT))
print("Beginning to listen...")
s.listen(1)
while True:
    print("Now waiting for connection...")
    conn, addr = s.accept()
    print("Connection from " + str(addr) + "!")


    # get all data
    conn.settimeout(0.5)
    all_data:bytearray = bytearray()
    while True:
        try:
            data:bytes = conn.recv(1024)
            for b in data:
                all_data.append(b)
        except: # there are no more bytes incoming in the stream and the timeout triggered
            break
    print(str(len(all_data)) + " bytes received!")

    # print the content
    print("Content received: " + str(data))

    # assemble JSON payload (body of response)
    payload = {"time": time.time()}

    # assemble response body
    response:str = "HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n" + json.dumps(payload)

    # send 200 OK
    conn.send(response.encode("utf-8"))
    conn.close()

