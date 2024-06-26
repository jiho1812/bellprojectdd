import socket
import tkinter as tk
import tkinter.messagebox as box
import threading
import time
import pygame

pygame.init()
pygame.mixer.init()

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12345

print(socket.gethostbyname(socket.gethostname()))

id_list=["00000","00000","00000","00000","00000","00000","00000",]
text_list=["-----","-----","-----","-----","-----","-----","-----",]
teacher_list=["---","---","---","---","---","---","---"]


teacher_sound={"이재선 선생님":1, "김수환 선생님":1, "손병만 선생님":1, "유병산 선생님":1, "김진영 선생님":1, "전선영 선생님":1, "오원진 선생님":1, "김기태 선생님":1, "박영선 선생님":1, "김영훈 선생님":1}

def play_music(track):
    pygame.mixer.music.load(teacher_sound[track])


def update_gui():
    for i in range(7):
        id_list_label[i].config(text=id_list[i])
        text_list_label[i].config(text=text_list[i])
        teacher_list_label[i].config(text=teacher_list[i])
        

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
    client_socket.sendall("Hello, client!".encode())

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"[*] Received: {data.decode()}")
        decoded_data=data.decode()
        number_id, message, teacher = decoded_data.split(':')
        del id_list[0]
        del text_list[0]   
        del teacher_list[0]     
        id_list.append(number_id)
        text_list.append(message)
        teacher_list.append(teacher)
        update_gui()
        play_music(teacher)

        
        
        
def start_gui():
    window = tk.Tk()
    window.title("당신을 원하고 있습니다!!")
    window.geometry("1000x300+300+100")

    id_label=tk.Label(window, text="아이디", borderwidth=3, relief="groove", width=30, height=2, padx=10, bg="gray")
    id_label.grid(row=0, column=0, sticky="nsew")

    teacher_label=tk.Label(window, text="선생님",borderwidth=3, relief="groove", width=30, height=2, padx=10, bg="gray")
    teacher_label.grid(row=0, column=1, sticky="nsew")

    text_label=tk.Label(window, text="내용", borderwidth=3, relief="groove", width=105, height=2, padx=10, bg="gray")
    text_label.grid(row=0, column=2, sticky="nsew")

    global id_list_label, text_list_label, teacher_list_label

    id_list_label = []
    text_list_label = []
    teacher_list_label=[]

    for i in [0,1,2,3,4,5,6]:
        id_list_label.append(tk.Label(window, text=id_list[i], borderwidth=3, relief="groove", width=30, height=2, padx=10))
        id_list_label[i].grid(row=i+1, column=0, sticky="nsew")
        teacher_list_label.append(tk.Label(window, text=teacher_list[i], borderwidth=3, relief="groove", width=30, height=2, padx=10))
        teacher_list_label[i].grid(row=i+1, column=1, sticky="nsew")
        text_list_label.append(tk.Label(window, text=text_list[i], borderwidth=3, relief="groove", width=30, height=2, padx=10))
        text_list_label[i].grid(row=i+1, column=2, sticky="nsew")

    window.mainloop()




server_thread = threading.Thread(target=start_server)
gui_thread = threading.Thread(target=start_gui)

server_thread.start()
gui_thread.start()