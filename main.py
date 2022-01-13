import math
import matplotlib.pyplot as plt

# Объявляем переменные
x = []  # Координаты точек по оси X
y = []  # Координаты точек по оси Y
blue_x = []  # Синие точки по оси X
blue_y = []  # Синие точки по оси Y
red_x = []  # Красные точки по оси X
red_y = []  # Красные точки по оси Y


def check(xy, xy2):
    return math.sqrt((xy[0] - xy2[0]) ** 2 + (xy[1] - xy2[1]) ** 2) > 1


def fill_points(xy):
    # Перебираем все точки. Считаем расстояние, и если оно больше, чем around - точка синяя, если нет, то красная
    for i in range(len(x)):
        koord_x = x[i]
        koord_y = y[i]
        # Если синяя точка - суем в список синих, если красная, то в список красных, все логично
        is_blue = check((koord_x, koord_y), (xy[0], xy[1]))
        if is_blue:
            blue_x.append(koord_x)
            blue_y.append(koord_y)
        else:
            red_x.append(koord_x)
            red_y.append(koord_y)


# Подготавливает данные
def prepare():
    k_x = math.sin(math.radians(30))
    k_y = math.sin(math.radians(60))

    x_step = round(1 * k_x, 2)  # Шаг точек по X
    y_step = round(1 * k_y, 2)  # шаг точек по Y

    # нам нужно рисовать точку через одну
    # будем считать какие точки влезают
    o_x = 0
    # Пока у нас o_x меньше, чем ширина графика повторяем цикл
    count = 2  # Если четное - тогда точку нужно добавить
    while o_x < 5:
        o_y = 0
        while o_y < 5:  # Пока у нас o_y меньше, чем высота графика повторяем
            if count % 2 == 0:  # count делится на 2, значит точку добавляем
                x.append(round(o_x, 2))
                y.append(round(o_y, 2))
            count += 1  # При любой итерации обновляем count.
            # Если добавили, значит следующую не нужно добавлять. И наоборот
            o_y += y_step
        count += 1  # Увеличили x, значит обновляем count. Так рисуются точки
        o_x += x_step


# Объявляем координаты нашей зеленной точки
x_main = 1
y_main = 1

prepare()
fill_points((x_main, y_main))

print(blue_x, blue_y, red_y, red_y)
plt.plot(blue_x, blue_y, 'bo')  # Синие
plt.plot(red_x, red_y, 'ro')  # Красные
plt.plot([x_main], [y_main], 'go--')  # Наша зеленая точка
plt.axis([0, 5, 0, 5])  # Ставит график
plt.grid(True)  # Ставит сетку на графику
plt.show()  # вызов метода показывает все
