from die import Die

import  pygal

#创建两个D6
die_1 = Die()
die_2 = Die()

#掷骰子，结果存储列表
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequence = results.count(value)
    frequencies.append(frequence)
print(frequencies)

#结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')