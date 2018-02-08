from chap15.die import  Die
import pygal

die1 = Die()
die2 = Die()

results = []
for i in range(10000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequences = []
for value in range(2, die1.num_slides + die2.num_slides + 1):
    frequent = results.count(value)
    frequences.append(frequent)

print(frequences)

hist = pygal.Bar()
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'

hist.y_title = 'Frequency of Result'
hist.add('D6 + D6', frequences)
hist.render_to_file('dice_visual.svg')