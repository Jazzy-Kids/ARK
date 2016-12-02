import socketserver

s = socketserver.MySocket()

s.connect(s.gethostname(), 8081)


data = 1

s.mysend(data)

print (data)
input()
