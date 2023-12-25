# Modifying Elements in a List
value = ['honda', 'suzuki', 'ducati', 'toyota']
print(value[1].title())

value[0] = 'ford'
print(value)


# Appending Elements to a List
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)