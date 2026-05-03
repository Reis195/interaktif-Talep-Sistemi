from tkinter import *
pencere = Tk()
pencere.geometry("500x350")
pencere.title("ITS")
pencere.configure(background="gray12")

kategoriler = {}
hata_labeli = Label(pencere,text="Lütfen Fiyat Kısmına Sayı Giriniz",bg="gray12",fg="white")

giris = Label(pencere,text="İNTERAKTİF TALEP SİSTEMİ",font=("Times",24,"bold"),bg="gray12",fg="white")

def kaydetme():
    tur = tur_entrysi.get().strip().capitalize()
    isim = isim_entrysi.get().strip()
    fiyat = fiyat_entrysi.get().strip()
    fiyat2 = fiyat.replace(",","",1)
    if not fiyat2.isdigit():
        hata_labeli.pack()
        return
    hata_labeli.destroy()
    if tur and isim and fiyat:
        #programın hatalı ve boş veri kaydetmesini engelleyen kod
        if tur not in kategoriler:
            kategoriler[tur] = []

        kategoriler[tur].append(f"{isim} ---> {fiyat}TL")

        print(f"eklendi {tur} --> {isim} > {fiyat}TL")

    else:
        print("Lütfen bir şeyler ekleyin, ekranı boş bırakmayın")

def menu_gosterme():
    yeni_pencere = Toplevel()
    yeni_pencere.geometry("500x800")
    yeni_pencere.configure(bg="#E6DAB8")
    baslik = Label(yeni_pencere,text="MENÜ",bg="#E6DAB8",foreground="black",font=("Times",24,"bold"))
    baslik.pack()
    for tur,isim in kategoriler.items():
        Label(yeni_pencere,text=f"--{tur}--",bg="#E6DAB8",fg="Black",font="Arial 20").pack(pady=10)
        for urun in isim:
            Label(yeni_pencere,text=f"<<< {urun} >>>",bg= "#E6DAB8",fg = "Black").pack()
    pencere.mainloop()

def silme():
    kategoriler.clear()
    tur_entrysi.delete(0,END)
    isim_entrysi.delete(0,END)
    fiyat_entrysi.delete(0,END)


tur_entrysi = Entry(pencere)
tur_entrysi.pack(pady=10)

tur_labeli = Label(pencere,text="Ürünün Kategorisini giriniz:",bg="gray12",fg="white")
tur_labeli.place(x=10,y=10)

isim_entrysi = Entry(pencere)
isim_entrysi.pack(pady=10)

isim_labeli = Label(pencere,text="Ürünün İsmini Giriniz:",bg="gray12",fg="white")
isim_labeli.place(x=10,y=45)

fiyat_entrysi = Entry(pencere)
fiyat_entrysi.pack(pady=10)

fiyat_labeli = Label(pencere,text="Ürünün Fiyatını Giriniz:",bg="gray12",fg="white")
fiyat_labeli.place(x=10,y=85)

kaydetme_butonu = Button(pencere,text="Kaydet",command=kaydetme,width=12,height=2)
kaydetme_butonu.place(x=50,y=180)

menu_gosterme_butonu = Button(pencere,text="Menü Gösterme",command=menu_gosterme,width=12,height=2)
menu_gosterme_butonu.place(x=200,y=180)

silme_butonu= Button(pencere,text="Sil",command=silme,width=12,height=2)
silme_butonu.place(x=350,y=180)

giris.place(x=20,y=270)

pencere.mainloop()