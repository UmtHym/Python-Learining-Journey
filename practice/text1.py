colors = ['blue', 'yellow', 'brown', 'blue']
random_items = [2, 'rainbow', [2,4,5], False]
nested = [1,2,[3,4,5],[6,7,8]]

numbers = [1,2,3,4,5]

# print('From 0th index', numbers[0], numbers[int(round(len(numbers) - 1)/2)], numbers[-1])
# print(3 in numbers)

animals = ['gorilla', 'monkey', 'zebra']

animals.insert(0,'snake')
animals.append('rhino')
animals.extend(['giraffe', 'tomato'])
animals.remove('tomato')

print(animals)