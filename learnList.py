bicycles = ["trek", "lam" , "samuels", "hero"]
message = f"Hey, My first bicycle was {bicycles[3].title()}"
print(message)
bicycles[0] = "Ferrari"
bicycles.append("BTS")
print(bicycles)

cars = []
cars.append('Land Rover')
cars.append('Jaguar')
cars.append('Jeep')
cars.append('Mustang')
cars.insert(2, 'Ford')
cars_pop = cars.pop()
print (cars_pop)
print(cars)