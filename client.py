import socket
import tkinter as tk
import tkinter.messagebox as box
import hashlib

SERVER_HOST = '192.168.219.102'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

server_msg = client_socket.recv(1024)
print(f"[*] Received from server: {server_msg.decode()}")


id_and_password={

}

with open(r'C:\Coding\bellproject\databa\회원정보.txt', 'r') as file:
    # 파일의 각 줄에 대해서 반복
        for line in file:
            # 줄을 콜론(:)을 기준으로 분리하여 key와 value로 저장
            key, value = line.strip().split(":")
            
            # 딕셔너리에 key와 value 추가
            id_and_password[key] = value



def check(id_entry, password_entry, text, client_socket):
    id_value=id_entry.get()
    password_value=password_entry.get()
    text_value = text.get()
    if id_value not in id_and_password.keys():
        print("존재하지 않는 학번입니다.")
        box.showinfo(message="존재하지 않는 학번입니다.", title="경고")
    else:
        if  hashlib.sha256(password_value.encode()).hexdigest() == id_and_password[id_value] :
            print(text_value)
            text_id=f"{id_value}:{text_value}"
            client_socket.send(text_id.encode())
            box.showinfo(message="전송되었습니다.", title="알림")
            id_entry.delete(0, len(id_entry.get()))
            password_entry.delete(0, len(password_entry.get()))
            text.delete(0, len(text.get()))

        else:
            box.showinfo(message="아이디와 비밀번호가 일치하지 않습니다.", title="경고")


def register_check(admin_password_entry,register_id_entry,register_password_entry):
    admin_pw = "12345"
    password_value=register_password_entry.get()
    if register_id_entry.get() not in id_and_password:
        if admin_pw ==  admin_password_entry.get():
            hashed_password = hashlib.sha256(password_value.encode()).hexdigest()
            id_and_password[register_id_entry.get()] = hashed_password


            box.showinfo(message="회원가입이 완료되었습니다.", title="알림")

            output_file_path = r'C:\Coding\bellproject\databa\회원정보.txt'
            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                output_file.write(f"{register_id_entry.get()}:{hashed_password}\n")
           
           

            register_id_entry.delete(0, len(register_id_entry.get()))
            register_password_entry.delete(0, len(register_password_entry.get()))
            admin_password_entry.delete(0, len(admin_password_entry.get()))
        else: 
            box.showinfo(message="관리자 비밀번호가 일치하지 않습니다.", title="경고")
            register_id_entry.delete(0, len(register_id_entry.get()))
            register_password_entry.delete(0, len(register_password_entry.get()))
            admin_password_entry.delete(0, len(admin_password_entry.get()))
            
    else:
     box.showinfo(message="이미 등록된 학번입니다.", title="경고")


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

    text_label=tk.Label(page1, text="요구사항(한 줄로 입력해주세요.)")
    text_label.pack()

    text=tk.Entry(page1)
    text.pack()

    button=tk.Button(page1, text="전송", command=lambda: check(id_entry, password_entry, text, client_socket))
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