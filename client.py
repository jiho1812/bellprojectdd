import socket
import tkinter as tk
import tkinter.messagebox as box
import hashlib

mySocket = socket.socket()

def Main():
        host = "DESKTOP-2NOGS03"
        port = 5000

        
        mySocket.connect((host,port))

        message = input(" -> ")

        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()

                print ('Received from server: ' + data)

                message = input(" -> ")

        mySocket.close()

if __name__ == '__main__':
    Main()



id_and_password={
    "id":"password",
    "30913" : "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
    "30826" : "fe2592b42a727e977f055947385b709cc82b16b9a87f88c6abf3900d65d0cdc3",
}


def check(id_entry, password_entry, text, mySocket):
    id_value=id_entry.get()
    password_value=password_entry.get()
    text_value = text.get("1.0", tk.END)
    if id_value not in id_and_password.keys():
        print("존재하지 않는 학번입니다.")
        box.showinfo(message="존재하지 않는 학번입니다.", title="경고")
    else:
        if  hashlib.sha256(password_value.encode()).hexdigest() == id_and_password[id_value] :
            print(text_value)
            mySocket.send(text_value.encode())
        else:
            box.showinfo(message="아이디와 비밀번호가 일치하지 않습니다.", title="경고")


def register_check(admin_password_entry,register_id_entry,register_password_entry):
    admin_pw = "12345"
    password_value=register_password_entry.get()
    if admin_pw ==  admin_password_entry.get():
        id_and_password[register_id_entry.get()]=hashlib.sha256(password_value.encode()).hexdigest()
        box.showinfo(message="회원가입이 완료되었습니다.", title="알림")
    else: 
        box.showinfo(message="관리자 비밀번호가 일치하지 않습니다.", title="경고")
        

def show_page(page):
    page.tkraise()

def create_page1(container):     
    page1 = tk.Frame(container)

    id_label=tk.Label(page1, text="학번")
    id_label.pack()

    id_entry=tk.Entry(page1)
    id_entry.pack()

    password_label=tk.Label(page1, text="비밀번호")
    password_label.pack()

    password_entry=tk.Entry(page1, show="*")
    password_entry.pack()

    text_label=tk.Label(page1, text="요구사항")
    text_label.pack()

    text=tk.Text(page1)
    text.pack()

    button=tk.Button(page1, text="전송", command=lambda: check(id_entry, password_entry, text, mySocket))
    button.pack()

    button1 = tk.Button(page1, text="회원가입", command=lambda: show_page(page2))
    button1.pack()

    return page1

def create_page2(container):
    page2 = tk.Frame(container)
    
    register_label = tk.Label(page2, text="계정 만들기")
    register_label.pack()
    register_label.config(pady=50)
    
    register_id_label=tk.Label(page2, text="학번")
    register_id_label.pack()

    register_id_entry=tk.Entry(page2)
    register_id_entry.pack()

    register_password_label=tk.Label(page2, text="비밀번호")
    register_password_label.pack()

    register_password_entry=tk.Entry(page2, show="*")
    register_password_entry.pack()

    button_success=tk.Button(page2, text="완료", command=lambda:register_check(admin_password_entry,register_id_entry,register_password_entry))
    button_page1=tk.Button(page2, text="로그인 페이지로 돌아가기", command=lambda: show_page(page1))
    button_success.pack()
    button_page1.pack()




    admin_password_label=tk.Label(page2, text="관리자용")
    admin_password_label.pack()
    admin_password_label.config(pady=20)

    admin_password_entry=tk.Entry(page2, show="*")
    admin_password_entry.pack()

   

    
    

    return page2

window = tk.Tk()
window.title("선생님을 부르세요!")

container = tk.Frame(window)
container.pack(side="top", fill="both", expand=True)

page1 = create_page1(container)
page2 = create_page2(container)

window.geometry("500x500+500+150")

page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")

show_page(page1)

window.mainloop()