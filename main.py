from tkinter import *
import tkinter.scrolledtext
from kafka import KafkaProducer, KafkaConsumer
import threading


def kafka_prod():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    if input_area.get("1.0", "end-1c"):
        message = input_area.get("1.0", "end-1c")
        input_area.delete("1.0", "end")
        producer.send("chat", message.encode('utf-8'))
        producer.flush()


class Lecture(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.c = False

    def run(self):
        consumer = KafkaConsumer("chat", bootstrap_servers='localhost:9092')
        for message in consumer:
            if self.c:
                break
            text_area.config(state='normal')
            text_area.insert("end", message.value.decode('utf-8') + "\n")
            text_area.config(state='disabled')

    def stopthread(self):
        self.c = True
        message = "Deconnexion"
        KafkaProducer(bootstrap_servers=['localhost:9092']).send("chat", message.encode('utf-8'))
        KafkaProducer(bootstrap_servers=['localhost:9092']).flush()


fenetre = Tk()
fenetre.config(bg="lightgray")
fenetre.title("Chat")

chat_label = tkinter.Label(fenetre, text="Chat", bg="lightgray")
chat_label.config(font=("Arial", 12))
chat_label.pack(padx=20, pady=5)

text_area = tkinter.scrolledtext.ScrolledText(fenetre)
text_area.pack(padx=20, pady=5)

msg_label = tkinter.Label(fenetre, text="Message", bg="lightgray")
msg_label.config(font=("Arial", 12))
msg_label.pack(padx=20, pady=5)

input_area = tkinter.Text(fenetre, height=3)
input_area.pack(padx=20, pady=5)

send_button = tkinter.Button(fenetre, text="Send", command=kafka_prod)
send_button.config(font=("Arial", 12))
send_button.pack(padx=20, pady=5)
con = Lecture()
con.start()
fenetre.mainloop()
con.stopthread()
