import socket
import tkinter as tk
import tkinter.messagebox as box
import threading
import time
import pygame

pygame.init()
pygame.mixer.music.load("992600335F7211DC01.mp3")




SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12345

print(socket.gethostbyname(socket.gethostname()))

id_list=["00000","00000","00000","00000","00000","00000","00000",]
text_list=["-----","-----","-----","-----","-----","-----","-----",]





def update_gui():
    for i in range(7):
        id_list_label[i].config(text=id_list[i])
        text_list_label[i].config(text=text_list[i])
        

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
        number_id, message = decoded_data.split(':')
        del id_list[0]
        del text_list[0]        
        id_list.append(number_id)
        text_list.append(message)
        update_gui()
        pygame.mixer.music.play()
        
        
def start_gui():
    window = tk.Tk()
    window.title("당신을 원하고 있습니다!!")
    window.geometry("1000x300+300+100")

    id_label=tk.Label(window, text="아이디", borderwidth=3, relief="groove", width=30, height=2, padx=10, bg="gray")
    id_label.grid(row=0, column=0, sticky="nsew")

    text_label=tk.Label(window, text="내용", borderwidth=3, relief="groove", width=105, height=2, padx=10, bg="gray")
    text_label.grid(row=0, column=1, sticky="nsew")

    global id_list_label, text_list_label

    id_list_label = []
    text_list_label = []

    for i in [0,1,2,3,4,5,6]:
        id_list_label.append(tk.Label(window, text=id_list[i], borderwidth=3, relief="groove", width=30, height=2, padx=10))
        id_list_label[i].grid(row=i+1, column=0, sticky="nsew")
        text_list_label.append(tk.Label(window, text=text_list[i], borderwidth=3, relief="groove", width=30, height=2, padx=10))
        text_list_label[i].grid(row=i+1, column=1, sticky="nsew")

    window.mainloop()




server_thread = threading.Thread(target=start_server)
gui_thread = threading.Thread(target=start_gui)

server_thread.start()
gui_thread.start()