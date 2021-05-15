# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:01:57 2021

@author: Gp
"""

from pqdict import pqdict #pqdict, saf Python'da dikte benzeri bir sınıf olarak 
#uygulanan dizinlenmiş bir öncelikli kuyruk veri yapısı sağlar.
import turtle #içerisinde yer alan çizim fonksiyonları ile çizimler yapabiliriz

def dijkstra(G,basla,bitis):
    # nihai uzakliklarin sozlugu
    D = {}  
    # ebeveyn dugumlerin sozlugu
    P = {}  
    # dugumlerin baslangica olan tahmini uzakliginin kuyrugu
    Q = pqdict() 

    Q[basla] = 0

    while len(Q)>0:
       (v,vv) = Q.popitem()
       D[v] = vv
       for w in G[v]:
          vwLength = D[v] + G[v][w]
          if w in D:
              if vwLength < D[w]:
                  raise ValueError("sonuca giden daha iyi yol bulundu")
          elif w not in Q or vwLength < Q[w]:
              Q[w] = vwLength
              P[w] = v
              print(v)
    #oluşturulacak yolu atacağımız dizi oluşturduk
    path = []
    #dizi oluşturulması
    while 1:
       path.append(bitis)
       print(path)
       if bitis == basla: break
       bitis = P[bitis]
    path.reverse()
    return path
#Kullanılcak şehir kütüphanesinin oluşturulması
graph = { 'siv' : {'kay' :195 , 'yoz' :224},
         'yoz' :{'kay': 175, 'nev' :190, 'kır' : 112, 'krk' : 141},
         'kay' :{'yoz': 175, 'nev' :81, 'nig' :128},
         'nig' :{'aks' :123, 'kay': 128, 'nev' :82, 'kon' : 242, 'kar' : 175},
         'nev' :{'aks' :75, 'kay': 81, 'kır' :91, 'yoz' : 190, 'nig' : 82},
         'kır' :{'aks' :110, 'nev': 91, 'krk' :113, 'yoz' : 112, 'ank' : 184},
         'krk' :{'kır' :113, 'yoz': 141, 'ank' :75, 'can' :105},
         'ank' :{'aks' :225, 'kır': 184, 'krk' :75, 'can' : 131, 'kon' : 258, 'esk' :233},
         'can' : {'ank' :131 , 'krk' :105},
         'esk' : {'ank' :233 , 'kon' :338},
         'kon' :{'aks' :148, 'nig': 242, 'kar' :119, 'esk' : 238, 'ank' : 258},
         'kar' : {'kon' :119 , 'nig' :175},
         'aks' :{'kon' :148, 'nig': 123, 'nev' :75, 'kır' : 110, 'ank' : 258},}

#hangi mesafeler arası algoritma uygulanacak
a = dijkstra(graph,'siv','esk')

#yol güzergahının yazdırılması
print(a)

#toplam yolun kaç km olduğunun bulunması
toplam_km = 0
for i in range(len(a)-1):
    x = graph.get(a[i])
    y = x.get(a[i+1])
    toplam_km += y


#Çizim
turtle.title("SG LOJİSTİK SİMÜLASYONU") 
turtle.setup(1500,700)
board = turtle.Turtle()
turtle.bgpic("harita.png")
#çizim işlemi için kontrollerin yapılması
for i in range(len(a)):
    #başlangıç konumunun belirlenmesi
    if(i == 0):
         if(a[i] == "kay"):
             board.up()
             board.goto(138,-51)
             board.down()
             
         elif(a[i] == "yoz"):
             turtle.up()
             board.goto(85,82)
             board.down()
             
         elif(a[i] == "can"):
             board.up()
             board.goto(-108,255)
             board.down()
             
         elif(a[i] == "nev"):
             board.up()
             board.goto(5,45)
             board.down()
             
         elif(a[i] == "nig"):
             board.up()
             board.goto(5,-158)
             board.down()
             
         elif(a[i] == "siv"):
             board.up()
             board.setpos(300,62)
             board.down()
             
         elif(a[i] == "esk"):
             board.up()
             board.goto(-380,132)
             board.down()
             
         elif(a[i] == "ank"):
             board.up()
             board.goto(-215,120)
             board.down()
             
         elif(a[i] == "krk"):
             board.up()
             board.goto(-90,125)
             board.down()
             
         elif(a[i] == "kon"):
             board.up()
             board.goto(-243,-127)
             board.down()
             
         elif(a[i] == "aks"):
             board.up()
             board.goto(-85,-87)
             board.down()
             
         elif(a[i] == "kar"):
             board.up()
             board.goto(-155,-268)
             board.down()
             
         elif(a[i] == "kır"):
             board.up()
             board.goto(-48,48)
             board.down()
             
         else:
            print("girdiğiniz başlangıç noktası bölgede bulunmamaktadır.")

    board.speed(1)
    board.shape("turtle")
    
    #adımların kontrolü
    if(a[i] == "kay"):
        #kayseri
        board.pendown()
        board.setpos(138,-51)
        board.circle(25)        

    elif(a[i] == "yoz"):
        #yozgat
        board.pendown()
        board.setpos(85,82)
        board.circle(25)
        
    elif(a[i] == "can"):
        #çankırı
        board.pendown()
        board.setpos(-108,255)
        board.circle(25)

    elif(a[i] == "nev"):
        #nevşehir
        board.pendown()
        board.setpos(5,-45)
        board.circle(25)
     
    elif(a[i] == "nig"):
        #niğde
        board.pendown()
        board.setpos(5,-158)
        board.circle(25)
     
    elif(a[i] =="siv"):
        #sivas
        board.pendown()
        board.setpos(300,62)
        board.circle(25)
         
    elif(a[i] == "esk"):
        #eskişehir
        board.pendown()
        board.setpos(-380,122)
        board.circle(25)

    elif(a[i] == "ank"):
        #Ankara
        board.pendown()
        board.setpos(-215,130)
        board.circle(25)
                
    elif(a[i] == "krk"):
        #kırıkkale
        board.pendown()
        board.setpos(-90,125)
        board.circle(25)
      
    elif(a[i] == "kon"):
        #konya
        board.pendown()
        board.setpos(-243,-127)
        board.circle(25)
     
    elif(a[i] == "kar"):
        #karaman
        board.pendown()
        board.setpos(-155,-268)
        board.circle(25)
       
    elif(a[i] == "aks"):
        #aksaray
        board.pendown()
        board.setpos(-85,-87)
        board.circle(25)
     
    elif(a[i] == "kır"):
        #kırşehir
        board.pendown()
        board.setpos(-48,48)
        board.circle(25)
     
    else:
        print("sistesel bir arıza oluştu. Lütfen tekrar deneyiniz")

turtle.write(toplam_km)
turtle.done()
