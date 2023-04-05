class Person:
     def __int__(self,name,sqesi,asaki,xelfasi):
         self.name = name
         self.sqesi = sqesi
         self.asaki = asaki
         self.xelfasi = xelfasi

     def __str__(self):
         return f" saxelia {self.name}, sqesia {self.sqesi},asakia {self.asaki},xelfasia {self.xelfasi}"
     def funqcia(self,sapensio):
        sashemosavlo = (self.xelfasi) / 5
        self.sapensio = self.xelfasi /  100
        jami = sashemosavlo + sapensio
        print(jami)
     def sapensiodanazogi(self ):
         if self.sqesi == "women":
            danazogi = (self.xelfasi / 100) * 30 * 12
            return danazogi
        elif:
           danazogi = sapensio * 35 * 12
           return  danazogi
    def pensia(self):
        if self.sqesi == "women":
         pensiaa = 60 - self.asaki
        elif:
         pensiaa = 60 - self.asaki

x = Person("mari","women",20,100)
print(x)




