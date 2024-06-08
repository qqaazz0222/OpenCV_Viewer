
import socket
import numpy
import cv2

UDP_IP = "192.168.196.100"
UDP_PORT = 9505

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

s = b''

while True:
    data, addr = sock.recvfrom(46080)
    s += data

    if len(s) == (46080 * 20):
        frame = numpy.fromstring(s, dtype=numpy.uint8)
        frame = frame.reshape(480, 640, 3)
        cv2.imshow("frame", frame)
        s = b''

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break