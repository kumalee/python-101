from car import car

class dc_car(car):
    def __init__(self, brand, color, types, dc):
        car.__init__(self, brand, color, types)
        self.dc = dc

    def charge(self, dc=10):
        self.dc += 10

    def get_dc(self):
        print 'The {color} {brand} {types}\'s dc is {dc}'.format(color=self.color, brand=self.brand,
		types=self.types, dc=self.dc)

my_car = dc_car('benz','red','electric car',dc=0)
my_car.status()
my_car.get_dc()
my_car.charge(20)
my_car.get_dc()
