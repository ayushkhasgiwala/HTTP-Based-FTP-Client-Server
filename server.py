import socket

port=5000
ip="127.0.0.1"
try:
    serverfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket created successfully")
except: 
    print("Socket creation failed with error")

try:
    print("hey")
    serverfd.bind((ip,port))
    print("Socket binded to ",port)
    serverfd.listen(10)
    print("Socket is listening")
    while(1):
        clientfd,addr=serverfd.accept()
        rdata=clientfd.recv(5000).decode()
        rdata=rdata.split("\n")
        #print(rdata[0])
        url=rdata[0]
        #print(url)
        url=url.split(' ')
        path=url[1]
        #print(path)
        #print(rdata[1])
        h="HTTP/1.1 200 OK\n\n"
        #h+="Content-Type: text/html; charset=utf-8\r\n"
        header=h.encode()
        if(path[0]=='/'):
            p='.'
            p+=path
        else:
            p="./"
            p+=path
        #print(p)
        if(path!="/favicon.ico"):    
            try:
                with open(p,'rb') as f:
                    data=f.read()
                clientfd.sendall(header+data)
            except:
                print("File Does not Exist")
                d="File Does not Exist"
                z="HTTP/1.1 404 NOT FOUND\n\n"
                clientfd.sendall(z.encode()+d.encode())
        else:
            clientfd.sendall("".encode())
        #data+="\r\n"
        #data+="<html><body>Hello World</body></html>\r\n\r\n"
        #clientfd.sendall(header+data)
        clientfd.shutdown(socket.SHUT_WR)

except:
    print("Error")

serverfd.close()