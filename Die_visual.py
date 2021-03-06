from Die import Die
import pygal

#创建一个D6
die_1 = Die()
die_2 = Die()

#掷骰子并保存在列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max = die_2.num_side + die_1.num_side
for value in range(1,max+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Results of rolling two D6 1000 times.'
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6+D6', frequencies)

hist.render_to_file('die_visual.svg')