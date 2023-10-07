# Classes are like blue-prints, example for creating objects

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')

print(my_car.make)
print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

# Inheritance - Create classes that depend on the above class

# Overwrites the moves method from Vehicle class


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along..')
        print(f"I am a {self.make} {self.model} {self.faa_id}")

# Overwrites the moves method from Vehicle class


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')

# Inherits fully the method passed in Vehicle class


class Golf_cart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-1223345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = Golf_cart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


print('\n\n')

# Polymorphism - Ability to behave differently in response to the same input messages

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
