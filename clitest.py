import socket

# 서버 주소와 포트
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

# 서버에 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# 서버로부터 환영 메시지 수신
server_msg = client_socket.recv(1024)
print(f"[*] Received from server: {server_msg.decode()}")

# 사용자로부터 메시지 입력 및 서버에 전송
while True:
    message = input("Enter message to send to server (enter 'exit' to close): ")
    if message.lower() == 'exit':
        break
    client_socket.sendall(message.encode())

# 소켓 닫기
client_socket.close()
