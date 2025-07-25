import socket

HOST = '127.0.0.1'
PORT = 8080
BOUNDARY = 'AaB03x'

payload = (
    f"--{BOUNDARY}\r\n"
    "Content-Disposition: form-data; name=\"file\"; filename=\"test.txt\"\r\n"
    "Content-Type: text/plain\r\n"
    "Content-Length: 100\r\n"
    "\r\n"
    "partial content...\r\n"
    f"--{BOUNDARY}--\r\n"
)

request = (
    f"POST / HTTP/1.1\r\n"
    f"Host: {HOST}:{PORT}\r\n"
    f"Content-Type: multipart/form-data; boundary={BOUNDARY}\r\n"
    f"Content-Length: {len(payload)}\r\n"
    f"Connection: close\r\n"
    f"\r\n"
    f"{payload}"
)

with socket.create_connection((HOST, PORT)) as sock:
    sock.sendall(request.encode())
    try:
        response = sock.recv(1024)
        print("Response:", response.decode())
    except:
        pass
