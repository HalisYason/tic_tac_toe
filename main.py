
import tkinter as tk

class app(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("300x360")
        self.title("tic tac toe")


        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Dosya menüsü oluştur
        dosya_menu = tk.Menu(menubar)
        menubar.add_cascade(label="hakkında", menu=dosya_menu)

        # Yeni Pencere seçeneğini ekle
        dosya_menu.add_command(label="hakkında", command=self.yeni_pencere)

        self.sıra = 0
        self.x_durum = []
        self.o_durum = []

        self.e1  = tk.Label(text=" ___ ")
        self.e1.grid(row=1,column=1)

        self.e2  = tk.Label(text=" ___ ")
        self.e2.grid(row=1,column=2)


        self.e3  = tk.Label(text=" ___ ")
        self.e3.grid(row=1,column=3)

        self.e4  = tk.Label(text=" ___ ")
        self.e4.grid(row=2,column=1)

        self.e5  = tk.Label(text=" ___ ")
        self.e5.grid(row=2,column=2)

        self.e6  = tk.Label(text=" ___ ")
        self.e6.grid(row=2,column=3)

        self.e7  = tk.Label(text=" ___ ")
        self.e7.grid(row=3,column=1)

        self.e8  = tk.Label(text=" ___ ")
        self.e8.grid(row=3,column=2)

        self.e9  = tk.Label(text=" ___ ")
        self.e9.grid(row=3,column=3)

        self.sıra_e = tk.Label(text="sıra: ",bg="grey",fg="white")
        self.sıra_e.grid(row=1,column=4) 

        self.sıra_k = tk.Label(text="O",bg="grey",fg="orange")
        self.sıra_k.grid(row=1,column=5) 

        
        # butonlar

        self.koy = tk.Button(text="KOY",command=self.ekrana_koy)
        self.koy.grid(row=7,column=1)

        self.kapat = tk.Button(text="PES",command=self.kapatt)
        self.kapat.grid(row=7,column=2)


        self.tekrar = tk.Button(text = "TEKRAR",command=self.tekrar_buton)
        self.tekrar.grid(row=7,column=3)

        # entry

        self.neresi = tk.Entry()
        self.neresi.grid(row=6,column=2)


        ####

        self.uyarı1 = tk.Label(text="",fg="red")
        self.uyarı1.grid(row=9,column=2)

        self.uyarı2 = tk.Label(text="",fg="red")
        self.uyarı2.grid(row=11,column=2)

    
    def kapatt(self):
        print(self.sıra_k)
        self.kapat["state"] = "disabled"
        self.uyarı1["fg"] = "red"
        self.uyarı2["fg"] = "green"

        self.uyarı1["text"] = "OYUN SONLANDI"
        self.uyarı2["text"] = "KAZANAN YOK"


        self.after(4200, self.destroy)



    def ekrana_koy(self):
        self.uyarı1["text"] = ""
        self.uyarı2["text"] =""
        n = self.neresi.get()
        x,y = n.split("-")
        self.tahta(x,y)
        self.kazanma_olcutleri()
        

    # tahtaya yazdırma ve bir dizi işlem daha
    def tahta(self, x, y):
        try:
            x = int(x) - 1
            y = int(y) - 1

            durum = [x,y]

            if x < 0 or x > 2 or y < 0 or y > 2:
                self.uyarı1["text"] = "Tahta dışına çıkılamaz."
                self.neresi.delete(0, tk.END)  
        except ValueError:
            self.uyarı2["text"] = "Geçersiz girdi: x ve y tam sayı olmalıdır."
            self.neresi.delete(0, tk.END)
            return
        except IndexError as e:
            self.uyarı2["text"] = e
            return

        oyun_tahtası = [[self.e1, self.e2, self.e3],
                        [self.e4, self.e5, self.e6],
                        [self.e7, self.e8, self.e9]]
        
        if oyun_tahtası[x][y]["text"] == " ___ ":
            sıra_bu = self.sıra_kimde()

            if sıra_bu == "X":
                self.sıra_k["text"] = "O"
                self.x_durum.append(durum)
                oyun_tahtası[x][y]["text"] = "X"
            if sıra_bu == "O":
                self.sıra_k["text"] = "X"
                self.o_durum.append(durum)
                oyun_tahtası[x][y]["text"] = "O"

            self.neresi.delete(0, tk.END)
        else:
            self.uyarı2["text"] = "ORASI DOLU\n BAŞKA YERE KOYUN"


    # sıra devretme işlemi
    def sıra_kimde(self):
        self.sıra += 1
        if self.sıra % 2 == 0:
            return "X"
        else:
            return "O"
        

    def kazanan(self,k):
        self.uyarı2["fg"] = "green"
        if k == "O":
            self.uyarı2["text"] = "KAZANAN\n O"
        if k == "X":
            self.uyarı2["text"] = "KAZANAN\n X"

        self.koy["state"] = "disabled"
        self.kapat["state"] = "disabled"



    def kazanma_olcutleri(self):
        # kazanma ölçütlerini yani kazanma durumlarını listeledik
        kazanma_ölçütleri = [
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
        ]


        for i in kazanma_ölçütleri:
            o = [z for z in i if z in self.o_durum]
            x = [z for z in i if z in self.x_durum]
            if len(o) == len(i):
                self.kazanan("O")
            if len(x) == len(i):
                self.kazanan("X")


    # tekrar oynama
    def tekrar_buton(self):
        self.neresi.delete(0,tk.END)

        self.uyarı1["text"] = ""
        self.uyarı2["text"] = ""

        self.sıra_k["text"] = "O"
        self.koy["state"] = "active"
        self.kapat["state"]  ="active"

        self.sıra = 0
        self.x_durum = []
        self.o_durum = []

        oyun_tahtası = [[self.e1, self.e2, self.e3],
                        [self.e4, self.e5, self.e6],
                        [self.e7, self.e8, self.e9]]
        
        for satır in oyun_tahtası:
            for eleman in satır:
                eleman["text"] = " ___ "

        self.after(1100)

    
    # hakkında penceresi
    def yeni_pencere(self):
        # Yeni pencere oluştur
        yeni_pencere = tk.Toplevel(self.master)
        yeni_pencere.title("Hakkında")

        # Yeni pencere içeriğini ekle
        etiket = tk.Label(yeni_pencere, text="developer: halis göller\ne-posta: gollerhls@gmail.com")
        etiket.pack(padx=20, pady=20)

        
      

if __name__=="__main__":

    a1 = app()
    a1.mainloop()



# TİC TAC TOE
