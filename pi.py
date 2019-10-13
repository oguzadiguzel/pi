import random
import matplotlib.pyplot as plt


#Birim çember içine/dışına düşen atışların x/y ekseni koordinatları
x_icerde = []   
y_icerde = []   
x_disarda = []  
y_disarda = []  

def pi_sayisi(atis):
    icerde = 0
    for i in range (atis):
        #-1 ve 1 aralığında rastgele atışlar
        x = random.uniform(-1,1) 
        y = random.uniform(-1,1)
        if x**2 + y**2 <= 1:  #Atışların çember içine düşüp düşmediğinin kontrolü
            icerde += 1
            x_icerde.append(x)
            y_icerde.append(y)
        else:
            x_disarda.append(x)
            y_disarda.append(y)
            
    f = 4*(icerde/atis) #Çember içine ve dışına düşen atışların oranından yaklaşık pi sayısı değeri 
    return f


pi = pi_sayisi (1000) #atış sayısı

print("Yaklaşık pi sayısı değeri:", pi)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.scatter(x_icerde, y_icerde, color='g')
ax.scatter(x_disarda, y_disarda, color='r')
fig.show()