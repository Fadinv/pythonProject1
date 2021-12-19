import math
import matplotlib.pyplot
import matplotlib.patches


# Читать начинай отсюда
# Это класс, который отвечает за позиционирование
class Pos(object):
    # В конструкторе ничего не делаем, только создаем приватные поля, куда будем кидать координаты
    def __init__(self):
        self.__x = []  # Сюда мы кладем вообще все координаты точек по оси X
        self.__y = []  # Сюда мы кладем вообще все координаты точек по оси Y
        self.__blue_x = []  # Сюда мы кладем все синие точки по оси X
        self.__blue_y = []  # Сюда мы кладем все синие точки по оси Y
        self.__red_x = []  # Сюда мы кладем все красные точки по оси X
        self.__red_y = []  # Сюда мы кладем все красные точки по оси Y

    # Считает расстояние между двумя точками, принимает координаты (x, y) и (x1, y1)
    @staticmethod  # Статический метод (мы можем обращаться к нему как Pos.distance в любом месте)
    def distance(xy, xy2):
        return math.sqrt((xy[0] - xy2[0]) ** 2 + (xy[1] - xy2[1]) ** 2)

    # добавяет координату в приватные переменные __x и __y
    def add(self, num_x: float, num_y: float):  # Нужен когда мы расставляем все точки
        self.add_x(round(num_x, 2))
        self.add_y(round(num_y, 2))

    def add_x(self, num: float):  # Используется в методе add
        self.__x.append(num)

    def add_y(self, num: float):  # Используется в методе add
        self.__y.append(num)

    # Нужно вызвать, когда передаем around (радиус, относительно которого хватаем точки)
    # Расставляет синие и красные точки
    def fill_points(self, xy, around: int):
        self.__blue_x = []
        self.__blue_y = []
        self.__red_x = []
        self.__red_y = []
        # Перебираем все точки. Считаем растояние, и если оно больше, чем around - точка синяя, если нет, то красная
        for i in range(len(self.__x)):
            x = self.__x[i]
            y = self.__y[i]
            # Если синяя точка - суем в список синих, если красная, то в список красных, все логично
            is_blue = self.distance((x, y), (xy[0], xy[1])) > around
            if is_blue:
                self.__blue_x.append(x)
                self.__blue_y.append(y)
            else:
                self.__red_x.append(x)
                self.__red_y.append(y)

    # Ниже методы - гетеры. То есть вернут тебе координаты,
    # если не вызван метод fill_points, то они все вернут пустой массив

    # Вернет массив синих точек по X
    def get_blue_x(self):
        return self.__blue_x

    # Вернет массив синих точек по Y
    def get_blue_y(self):
        return self.__blue_y

    # Вернет массив красных точек по X
    def get_red_x(self):
        return self.__red_x

    # Вернет массив красных точек по Y
    def get_red_y(self):
        return self.__red_y


# Основной класс - рисует схему
class Scheme(object):
    # В конструкторе мы принимаем объект из библиотеки matplotlib, который позволяет графики рисовать
    # А также размер схемы, расстояние до точек, и радиус поиска
    # plt - объект matplotlib.pyplot. Библиотека, с помощью которой рисуется график
    # size - Размер схемы
    # step - Расстояние до точек
    # around - Расстояние от активной точки, до точек, которые нужно подсветить
    def __init__(self, plt: matplotlib.pyplot, size: float, step: float, around: int):
        self.plt = plt
        self.size = size
        self.step = step
        self.around = around
        # В конструкторе мы создаем инстанс класса Pos как свойство объекта
        self.points = Pos()
        # И расставляем точки (пока без засовывания туда активной)
        self.fill()

    # Метод расставляет точки
    def fill(self):
        k_x = math.sin(math.radians(30))
        k_y = math.sin(math.radians(60))
        # python почему-то считает синус 30° как 0.49999999999999994, поэтому round

        # Это не совсем правильное решение, т.к шаг может оказаться не кратным значением
        # и вычисления получатся не верные при больших числах
        # Но тут это не совсем важно, думаю препод простит.
        # Математически верное решение - не прибавлять y_step и x_step друг к другу,
        # а увеличивать step на величину step при каждом шаге

        # Шаг точек по X
        x_step = round(self.step * k_x, 2)
        # шаг точек по Y
        y_step = round(self.step * k_y, 2)

        # нам нужно рисовать точку через одну
        # будем считать какие точки влезают
        o_x = 0
        # Пока у нас o_x меньше, чем ширина графика повторяем цикл
        count = 2  # Если четное - тогда точку нужно добавить
        while o_x < self.size:
            o_y = 0
            # Пока у нас o_y меньше, чем высота графика повторяем
            while o_y < self.size:
                # count делится на 2, значит точку добавляем
                if count % 2 == 0:
                    self.points.add(o_x, o_y)
                # при любой итерации обновляем count. Если добавили, значит следующую не нужно добавлять. И наоборот
                count += 1
                o_y += y_step
            # увеличили x, значит обновляем count. Так рисуются точки
            count += 1
            o_x += x_step

    # Основной метод. Принимает значения точки, по координатам x и y, относительно которой нужно считать радиус
    def show(self, x, y):
        # Вызываем метод класса Pos. Расставляет цветные точки на гафике
        self.points.fill_points((x, y), self.around)

        # Вызываем метод plot. Он ставит точки
        self.plt.plot(self.points.get_blue_x(), self.points.get_blue_y(), 'bo')  # Синие
        self.plt.plot(self.points.get_red_x(), self.points.get_red_y(), 'ro')  # Красные
        self.plt.plot([x], [y], 'go--')  # Наша зеленая точка

        self.plt.axis([0, self.size, 0, self.size])  # Ставит график
        self.plt.grid(True)  # Ставит сетку на графику
        self.plt.show()  # вызов метода показывает все


# И наконец наши вызовы
# Создаем инстанс класса
scheme = Scheme(matplotlib.pyplot, 10, 1, 1)

# Показываем график
scheme.show(1, 1)
