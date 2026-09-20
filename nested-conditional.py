print("Welcome to ride-picker!")
print("Pick your vehicle\n1 bike \n2 car")
vehicle_choice=input("Enter 1 or 2: ")
if vehicle_choice=='1':
    print("Pick your bike-type\n1 sports bike \n2 desert bike")
    bike_type=input("Enter 1 or 2: ")
    if bike_type=='1':
        print('You picked: sports bike')
        print('Top speed: 140 km/h')
        print('Best for: City roads')
    if bike_type=='2':
        print('You picked: desert bike')
        print('Top speed: 60 km/h')
        print('Best for: Deserts')

if vehicle_choice=='2':
    print("Pick your car-type\n1 SUV \n2 Sedan")
    car_type=input("Enter 1 or 2: ")
    if car_type=='1':
        print('You picked: SUV')
        print('Seats: 7')
        print('Best for: Off road adventures')
    if car_type=='2':
        print('You picked: Sedan')
        print('Seats=5')
        print('Best for: City travel')