from chap15.die import Die
import pygal

die = Die()

results = []

for roll_num in range(10000):
    result = die.roll()
    results.append(result)

frequences = []
for value in range(1, die.num_slides + 1):
    frequence = results.count(value)
    frequences.append(frequence)

print(frequences)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 10000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"

hist.y_title = "Frequency of Result"
hist.add('D6', frequences)
hist.render_to_file('die_visual.svg')
