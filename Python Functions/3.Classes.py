#9.3.5. Class and Instance Variables¶
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
['roll over']
e.tricks
['play dead']
print(d.tricks)
print(e.tricks)
#9.4. Random Remarks
# Function defined outside the class
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
bag = Bag();
bag.add('22');
bag.addtwice("Petar Petrov");
print(bag.data)

#9.5. Inheritance¶
class ImprovedBag(Bag):
   def remove(self,number):
       self.data.remove(number)
premiumBag = ImprovedBag();
premiumBag.add(40);
premiumBag.addtwice(500);
premiumBag.remove(40)
print(premiumBag.data)

