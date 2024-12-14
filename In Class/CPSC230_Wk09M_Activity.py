# Word guessing game
import random
someFish = ["Salmon", "Cod", "Goldfish", "Catfish", "Tuna"]
oneFish = random.randint(0,len(someFish)-1)
oneFish = list(oneFish)
oneFish = random.shuffle(oneFish)
shuffled = list.join(oneFish)
print(shuffled)