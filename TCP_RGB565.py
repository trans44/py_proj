import cv2
import socket
from datetime import datetime
LCD_WIDTH = 240
LCD_LENGTH = 280
server = ('192.168.101.97',3333)

def socket_cilent(ip):
    global client
    #实例化socket
    # #TCP
    # client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #UDP
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # #连接客户端地址 ip=(port,host)
    # if(client.connect_ex(ip) == 0):
    #     print("connect to server",ip)


def resize_img(image,width,length):
    if(width > LCD_WIDTH or length > LCD_LENGTH):
        if(width <= length):#横
            image = cv2.resize(image,(280,int(width*(280/length))))
    return image
    # if(image_width > image_length):#竖
    #     cv2.resize(image,())

def toarray_rgb565(img_arr):
    img_arr = cv2.cvtColor(img_arr,cv2.COLOR_BGR2BGR565)
    img_arr = img_arr[:,:,(1,0)]
    return img_arr

if __name__=="__main__":
    socket_cilent(server)
    image = cv2.imread('rtt.jpg')
    image_width = image.shape[0]
    image_length = image.shape[1]
    image_dimension = image.shape[2]

    image = resize_img(image,image_width,image_length)
    image_565 = toarray_rgb565(image)

    #转字节传输
    img_bytestream= image_565.tobytes()
    print(type(img_bytestream),len(img_bytestream),"B")
    #print(img_bytestream.hex())

    #TCP
    #client.send(img_bytestream,server)
    #UDP
    client.sendto(b"2312",server)

    # cv2.imshow("im",image)
    # cv2.waitKey()