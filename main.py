import tkinter as tk
import tkinter.messagebox as box
import hashlib


id_and_password={
    "id":"password",
    "30913" : "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
    "30826" : "fe2592b42a727e977f055947385b709cc82b16b9a87f88c6abf3900d65d0cdc3",
}



def check():
    id_value=id_entry.get()
    password_value=password_entry.get()
    text_value = text.get("1.0", tk.END)
    if id_value not in id_and_password.keys():
        print("존재하지 않는 학번입니다.")
        box.showinfo(message="존재하지 않는 학번입니다.", title="경고")
    else:
        if  hashlib.sha256(password_value.encode()).hexdigest() == id_and_password[id_value] :
            print(text_value)
        else:
            box.showinfo(message="아이디와 비밀번호가 일치하지 않습니다.", title="경고")
        


window = tk.Tk()

window.title("띵동띵동")
window.geometry("500x500+500+150")
window.resizable(False,False)

id_label=tk.Label(window, text="학번")
id_label.pack()

id_entry=tk.Entry(window)
id_entry.pack()

password_label=tk.Label(window, text="비밀번호")
password_label.pack()

password_entry=tk.Entry(window, show="*")
password_entry.pack()

text_label=tk.Label(window, text="요구사항")
text_label.pack()

text=tk.Text(window)
text.pack()

button=tk.Button(window, text="전송", command=check)
button.pack()

window.mainloop()