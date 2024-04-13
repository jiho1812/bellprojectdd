import socket

# 서버 주소와 포트
SERVER_HOST = '0.0.0.0'  # 외부에서 접근 가능한 모든 네트워크 인터페이스에 바인딩
SERVER_PORT = 12345

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 주소와 포트에 소켓을 바인딩
server_socket.bind((SERVER_HOST, SERVER_PORT))

# 클라이언트의 연결을 기다림
server_socket.listen(1)
print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# 클라이언트의 연결을 수락
client_socket, client_address = server_socket.accept()
print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

# 클라이언트에게 환영 메시지 전송
client_socket.sendall("Hello, client!".encode())

# 클라이언트로부터 메시지 수신 및 출력
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"[*] Received: {data.decode()}")

# 소켓 닫기
client_socket.close()
server_socket.close()
