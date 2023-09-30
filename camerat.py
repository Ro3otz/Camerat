import socket
import cv2
import pickle
import struct

ip = 'IP_ADDRESS'
port = 4444

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    data = pickle.dumps(frame)
    message_size = struct.pack("L", len(data))
    client_socket.sendall(message_size + data)

client_socket.close()
cap.release()
