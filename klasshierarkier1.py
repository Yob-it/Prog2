class Djur:
    def __init__(self, name):
        self.name = name
       
        

class Haj(Djur):
    def __init__(self, name,  eat_amount, can_swim):
        super().__init__(name)
        self.eat_amount = eat_amount
        self.can_swim = can_swim

class Fisk(Djur):
    def __init__(self, name, can_swim):
        super().__init__(name)
        self.can_swim = can_swim
    


haj = Haj("Apex predator", 5.5, True)
lax = Fisk("Lax", True)

#Hajen
print("_______________________")
print("Shark:")
print(f"Sharks eat {haj.eat_amount}  kilo fish per day")
if haj.can_swim:
    print("The shark can swim!!!!!1!")
else:
    print("The shark sunk...")

print("===========================")
#Laxen
print("Laxen")
print(f"{lax.name} can swim: {lax.can_swim}") 
print("________________________")