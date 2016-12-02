import socketserver

s = socketserver.MySocket()

s.connect(s.gethostname(), 8081)


data = s.myreceive()

print (data)
input()
