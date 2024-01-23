import cv2
import socket
import struct
import pickle
from io import BytesIO
from PIL import Image,ImageDraw
import numpy as np
import serial
import time



path = "/dev/ttyS0"
baud = 9600

dev = serial.Serial(
                    port = path,
                    baudrate = baud,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    bytesize = serial.EIGHTBITS
                    )


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.109',8485))
cam = cv2.VideoCapture(0)

def find_coeffs(pa,pb):
    matrix = []
    for p1,p2 in zip(pa,pb):
        matrix.append([p1[0],p1[1],1,0,0,0,-p2[0]*p1[0],-p2[0]*p1[1]])
        matrix.append([0,0,0,p1[0],p1[1],1,-p2[1]*p1[0],-p2[1]*p1[1]])
    A = np.matrix(matrix,dtype=np.float)
    B = np.array(pb).reshape(8)
    res = np.dot(np.linalg.inv(A.T*A)*A.T,B)
    return np.array(res).reshape(8)

coeffs = find_coeffs([(100,-600),(540,-600),(540,480),(100,480)],[(150,250),(490,250),(540,420),(100,420)])


A = np.ones(640)
B = np.ones(480)
A1 = np.zeros(640)
for i in range(640):
    A1[i] = A1[i]+i
B1 = np.zeros(480)
for i in range(480):
    B1[i] = B1[i]+i
def centroid(image):

    M00 = np.dot(np.dot(image,A),B)
    M10 = np.dot(np.dot(image,A1),B)
    M01 = np.dot(np.dot(image.T,B1),A)
    if M00 == 0:
        M00 =1
    Cx = int(M10/M00)
    Cy = int(M01/M00)
    return Cx, Cy


if __name__ == "__main__":
    
    while True:

        ret, frame = cam.read()
        cv2.imshow('frame',frame)
        
        img_bytes = BytesIO()
        width = frame.shape[1]
        height = frame.shape[0]
        frame1 = Image.fromarray(frame)
        
        perspective = frame1.transform((width,height),Image.PERSPECTIVE, coeffs, Image.BICUBIC)
        
        gray = perspective.convert('L')    
        threshold = 127
        fn2 = lambda x : 255 if x < threshold else 0
        thresh = gray.point(fn2)

        #cx,cy = centroid(width,height,thresh)
        cx,cy=centroid(np.array(thresh))

        im = ImageDraw.Draw(thresh)
        im.ellipse([(cx-5,cy-5),(cx+5,cy+5)], fill='red', outline=None)
        
        
        thresh.save(img_bytes, format = 'PNG')
        img_bytes = img_bytes.getvalue()
        data = pickle.dumps(img_bytes)
        size = len(data)
        client_socket.sendall(struct.pack(">L",size) + data )
        
        if cx >380:
            time.sleep(0.3)
            dev.write(b'right')
        elif cx < 260:
            time.sleep(0.3)
            dev.write(b'left')
        else:
            time.sleep(0.3)
            dev.write(b'forward')
       

            

    client_socket.close()
    cam.release()
    cam.destroyAllWindow()

        
