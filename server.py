import socket
import tkinter as tk
import tkinter.messagebox as box


def Main():
    host = "localhost"
    port = 5000

    print (socket.gethostname())

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        data = str(data)
        print (data)

    conn.close()

def add_waiting():
    print(123)

if __name__ == '__main__':
    Main()


waiting_list={
    "30913":"안녕하세요",
    "12345":"ㅠㅠㅠㅠ",
    "11111":"-----",
    "22222":"-----",
    "33333":"-----",
    "44444":"444444",
    "55555":"555555",
}
id_list=list(waiting_list.keys())
text_list=list(waiting_list.values())

window = tk.Tk()
window.title("당신을 원하고 있습니다!!")
window.geometry("1000x300+300+100")

id_label=tk.Label(window, text="아이디", borderwidth=3, relief="groove", width=30, height=2, padx=10, bg="gray")
id_label.grid(row=0, column=0, sticky="nsew")

text_label=tk.Label(window, text="내용", borderwidth=3, relief="groove", width=105, height=2, padx=10, bg="gray")
text_label.grid(row=0, column=1, sticky="nsew")

for i in [0,1,2,3,4,5,6]:
    id_list_label=tk.Label(window, text=id_list[i], borderwidth=3, relief="groove", width=30, height=2, padx=10)
    id_list_label.grid(row=i+1, column=0, sticky="nsew")
    text_list_label=tk.Label(window, text=text_list[i], borderwidth=3, relief="groove", width=30, height=2, padx=10)
    text_list_label.grid(row=i+1, column=1, sticky="nsew")

window.mainloop()