class cars:
       def __init__(self,name,brand,colour,hp):
         self.name=name
         self.brand= brand
         self.colour=colour
         self.hp=hp

       def myfunc(self):
         print(f"the name is {self.name} the brand is {self.brand} the colour is {self.colour} and the hp is{self.hp}")

       def __str__(self):
         return "Name:" +self.name + ", brand: "+self.brand +", colour:"+self.colour +",hp:"+str(self.hp)

p1= cars("harrier","tata","black",str(746))
p1.myfunc()
print(p1)


