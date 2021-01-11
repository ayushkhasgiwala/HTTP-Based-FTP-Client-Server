import socket

port=5000
ip="127.0.0.1"
try:
    clientfd=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except:
    print("Socket creation failed")

try:
    clientfd.connect((ip,port))
    print("Connected to ",port)
except:
    print("Connection Failed")

#while(1):
print("\n")
cmd=input("Enter Command : ")
c=cmd.split(" ")
if(c[0]=="GET"):
    command=cmd.encode()
    clientfd.sendall(command)
    d=clientfd.recv(1024*1024*1024,socket.MSG_WAITALL)
    header,data=d.split(b'\n\n',1)
    f=c[1]
    x=f.find('.')
    extension=f[x+1:]
    resultfile=open("result."+extension,"wb")
    resultfile.write(data)
    resultfile.close()
    print("Server : Check File in the location")

else:
    print("The entered command is invalid")

