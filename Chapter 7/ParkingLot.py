from datetime import datetime


class ParkingLot:
    def __init__(self, name, capacity):
        self.name = name
        self.vehicles = []
        self.capacity = capacity

    def register_vehicle(self, vehicle):
        if len(self.vehicles) + 1 > self.capacity:
            print('Parking lot is full :(')
        else:
            ticket = Ticket()
            ticket.register()
            vehicle.ticket = ticket
            self.vehicles.append(vehicle)
            vehicle.print()
            print(' was registered...')
            print()

    def vehicle_leave(self, vehicle):
        print()
        self.vehicles.remove(vehicle)
        print(vehicle.license_plate + ' is leaving the Parking lot')
        vehicle.ticket.pay_ticket()

    def print_vehicles_in_parking_lot(self):
        for vehicle in self.vehicles:
            vehicle.print()


class Ticket:
    def __init__(self):
        self.time_in = None
        self.time_out = None

    def register(self):
        print('Ticket was generated ... ')
        self.time_in = datetime.now()

    def print_ticket(self):
        print('Time In: ', self.time_in)

    def pay_ticket(self):
        self.time_out = datetime.now()
        self.print_ticket()
        print('Time Out: ', self.time_out)
        print('Ticket was paid, the vehicle must leave ...')
        print()


class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.ticket = None


class Car(Vehicle):
    def print(self):
        print('Car: ' + self.license_plate, end="")


class Motorcycle(Vehicle):
    def print(self):
        print('Motorcycle: ' + self.license_plate, end="")


class Truck(Vehicle):
    def print(self):
        print('Truck: ' + self.license_plate, end="")


car_one = Car('SH6829')
motorcycle = Motorcycle('PO1233')
car_two = Car('CA0922')
truck = Truck('KL0099')


parking_lot = ParkingLot('My Parking Lot :)', 3)
parking_lot.register_vehicle(car_one)
parking_lot.register_vehicle(motorcycle)
parking_lot.register_vehicle(car_two)
parking_lot.register_vehicle(truck)
parking_lot.vehicle_leave(car_one)
parking_lot.register_vehicle(truck)