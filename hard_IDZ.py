import math
y = float(input("Введите угол между часовой стрелкой и лучом через центр и точку 12 часов (в градусах): "))
h = int(y / 30)
k = y * 12 % 360
m = int(k / 6)
print("Угол для минутной стрелки: {} градусов".format(k))
print("Количество полных часов: {}".format(h))
print("Количество полных минут: {}".format(m))