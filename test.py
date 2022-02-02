import tkinter
from tkinter import *
from tkinter import messagebox, ttk, scrolledtext
from kafka import KafkaProducer, KafkaConsumer
import threading


class Login(tkinter.Tk):
    def __init__(self):
        # Text Variables
        super().__init__()
        self.username_input = StringVar()
        self.password_input = StringVar()
        self.geometry('600x450')
        self.title("Chat")

        # set window background color
        self['bg'] = "#8db1ab"

        # set resizeable false
        self.resizable(False, False)
        login_frame = Frame(self, bg="#cee397", pady=30)
        login_frame.place(x=90, y=30, w=400, h=400)

        # Login Title
        login_title = Label(login_frame, text="Bienvenue", bg="#cee397", fg="#587792",
                            font=("Cooper Black", 28, "bold"))
        login_title.pack()

        # Username Label
        username_label = Label(login_frame, text="Identifiant:", bg="#cee397", fg="#587792",
                               font=("Courier", 18, "bold"),
                               anchor="w")
        username_label.pack(fill=X, pady=(20, 0), padx=35)

        # Style TEntry
        ttk.Style().configure("TEntry", padding="4 4 0 4", forground="#000")
        self.username = ttk.Entry(login_frame, font=("Courier", 20, "bold"), textvariable=self.username_input)
        self.username.pack()
        # set autofoucus on username input
        self.username.focus()

        # Password Label and input
        password_label = Label(login_frame, text="Mot de passe:", bg="#cee397", fg="#587792",
                               font=("Courier", 18, "bold"),
                               anchor="w")
        password_label.pack(fill=X, pady=(20, 0), padx=35)
        password = ttk.Entry(login_frame, font=("Courier", 20, "bold"), textvariable=self.password_input, show="*")
        password.pack()

        # Login Button
        login_btn = Button(login_frame, text="Se connecter", bg="#587792", activebackground="#587792", fg="#cee397",
                           activeforeground="#cee397", bd=0, font=("Courier", 18, "bold"), cursor="hand2",
                           command=self.login)
        login_btn.pack(fill=X, padx=38, pady=25)

        signin_btn = Button(login_frame, text="S'inscrire", bg="#587792", activebackground="#587792", fg="#cee397",
                            activeforeground="#cee397", bd=0, font=("Courier", 18, "bold"), cursor="hand2",
                            command=self.inscription)
        signin_btn.pack(fill=X, padx=38, pady=1)

    def login(self):

        if self.username_input.get() == "" :
            messagebox.showerror("erreur", "le champs id doit etre remplis!")
            self.username.focus()

        else:

            self.destroy()
            chat1 = Chat(self.username_input.get())
            con = Lecture(chat1)
            con.start()
            chat1.mainloop()
            con.stopthread()

    def inscription(self):
        self.destroy()
        register = Register()
        register.mainloop()


class Register(tkinter.Tk):
    def __init__(self):
        super().__init__()
        # Text Variables
        self.userid_input = StringVar()
        self.name_input = StringVar()
        self.password_input = StringVar()
        self.geometry('600x450')
        self.title("S'inscrire à Chat ")

        # set window background color
        self['bg'] = "#8db1ab"

        # set resizeable false
        self.resizable(False, False)

        # Login Frame

        self.login_frame = Frame(self, bg="#cee397", pady=30)
        self.login_frame.place(x=90, y=30, w=400, h=400)

        # Username Label
        self.username_label = Label(self.login_frame, text="identifiant:", bg="#cee397", fg="#587792",
                                    font=("Courier", 18, "bold"),
                                    anchor="w")
        self.username_label.pack(fill=X, pady=(20, 0), padx=35)

        # Style TEntry
        ttk.Style().configure("TEntry", padding="4 4 0 4", forground="#000")
        self.username = ttk.Entry(self.login_frame, font=("Courier", 20, "bold"), textvariable=self.userid_input)
        self.username.pack()
        # set autofoucus on username input
        self.username.focus()
        self.name_label = Label(self.login_frame, text="Nom:", bg="#cee397", fg="#587792", font=("Courier", 18, "bold"),
                                anchor="w")
        self.name_label.pack(fill=X, pady=(20, 0), padx=35)
        self.password = ttk.Entry(self.login_frame, font=("Courier", 20, "bold"), textvariable=self.name_input)
        self.password.pack()
        # Password Label and input
        self.password_label = Label(self.login_frame, text="Mot de passe:", bg="#cee397", fg="#587792",
                                    font=("Courier", 18, "bold"),
                                    anchor="w")
        self.password_label.pack(fill=X, pady=(20, 0), padx=35)
        self.password = ttk.Entry(self.login_frame, font=("Courier", 20, "bold"), textvariable=self.password_input,
                                  show="*")
        self.password.pack()

        # Login Button
        self.register_btn = Button(self.login_frame, text="S'inscrire", bg="#587792", activebackground="#587792",
                                   fg="#cee397",
                                   activeforeground="#cee397", bd=0, font=("Courier", 18, "bold"), cursor="hand2",
                                   command=self.register)
        self.register_btn.pack(fill=X, padx=38, pady=25)

    def register(self):
        if self.userid_input.get() == "":
            messagebox.showerror("erreur", "le champs id doit etre remplis!")
            self.username.focus()

        else:

            self.destroy()
            chat = Chat(self.userid_input.get())
            con = Lecture(chat)
            con.start()
            chat.mainloop()
            con.stopthread()


class Chat(tkinter.Tk):
    def __init__(self, n):
        super().__init__()
        self.nom = n
        self.title('Chat')
        self.config(bg="lightgray")

        self.chat_label = tkinter.Label(self, text="Discussion : " + self.nom, bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self, text="Message", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self, text="Send", command=self.kafka_prod)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

    def kafka_prod(self):
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        if self.input_area.get("1.0", "end-1c"):
            message = "PYTHON : " + self.nom + ":::" + self.input_area.get("1.0", "end-1c")
            self.input_area.delete("1.0", "end")
            producer.send("chat", message.encode('utf-8'))
            producer.flush()


class Lecture(threading.Thread):
    def __init__(self, ch):
        threading.Thread.__init__(self)
        self.c = False
        self.text = ch

    def run(self):
        consumer = KafkaConsumer("chat", bootstrap_servers='localhost:9092')
        for message in consumer:
            if self.c:
                break
            self.text.text_area.config(state='normal')
            self.text.text_area.insert("end", message.value.decode('utf-8') + "\n")
            self.text.text_area.config(state='disabled')

    def stopthread(self):
        self.c = True
        message = "Deconnexion de " + self.text.nom
        KafkaProducer(bootstrap_servers=['localhost:9092']).send("chat", message.encode('utf-8'))
        KafkaProducer(bootstrap_servers=['localhost:9092']).flush()


# run window
login = Login()
login.mainloop()
