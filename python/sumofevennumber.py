n = int(input('Enter n : \n'))
counter = 2
sum = 0
while counter <= n:
     if counter % 2 == 0:
          print(counter, end= ' ')
          sum += counter
          print(sum)
     counter = counter + 1