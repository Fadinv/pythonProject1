import math
import matplotlib.pyplot
import matplotlib.patches

circle = matplotlib.patches.Circle


class Pos(object):
    def __init__(self):
        self.__x = []
        self.__y = []
        self.__blue_x = []
        self.__blue_y = []
        self.__red_x = []
        self.__red_y = []

    @staticmethod
    def distance(xy: tuple[float, float], xy2: tuple[float, float]):
        return math.sqrt((xy[0] - xy2[0]) ** 2 + (xy[1] - xy2[1]) ** 2)

    def add(self, num_x: float, num_y: float):
        self.add_x(round(num_x, 2))
        self.add_y(round(num_y, 2))

    def add_x(self, num: float):
        self.__x.append(num)

    def add_y(self, num: float):
        self.__y.append(num)

    def fill_points(self, xy: tuple[float, float], around: int):
        self.__blue_x = []
        self.__blue_y = []
        self.__red_x = []
        self.__red_y = []
        for i in range(len(self.__x)):
            x = self.__x[i]
            y = self.__y[i]
            is_blue = self.distance((x, y), (xy[0], xy[1])) > around
            if is_blue:
                self.__blue_x.append(x)
                self.__blue_y.append(y)
            else:
                self.__red_x.append(x)
                self.__red_y.append(y)

    def get_blue_x(self):
        return self.__blue_x

    def get_blue_y(self):
        return self.__blue_y

    def get_red_x(self):
        return self.__red_x

    def get_red_y(self):
        return self.__red_y


class Scheme(object):
    # size - Размер схемы
    # step - Расстояние до точек
    # around - Расстояние от активной точки, до точек, которые нужно подсветить
    def __init__(self, plt: matplotlib.pyplot, size: float, step: float, around: int):
        self.plt = plt
        self.size = size
        self.step = step
        self.around = around
        self.points = Pos()
        self.fill()

    def fill(self):
        k_x = math.sin(math.radians(30))
        k_y = math.sin(math.radians(60))
        # python почему-то считает синус 30° как 0.49999999999999994
        x_step = round(self.step * k_x, 2)
        y_step = round(self.step * k_y, 2)
        # нам нужно рисовать точку через одну
        # будем считать какие точки влезают
        o_x = 0
        count_x = 1
        while o_x < self.size:
            o_y = 0
            count_y = 1
            while o_y < self.size:
                if (count_x + count_y) % 2 == 0:
                    self.points.add(o_x, o_y)
                count_y += 1
                o_y += y_step
            count_x += 1
            o_x += x_step

    def show(self, x, y):
        self.points.fill_points((x, y), self.around)
        self.plt.plot(self.points.get_blue_x(), self.points.get_blue_y(), 'bo')
        self.plt.plot(self.points.get_red_x(), self.points.get_red_y(), 'ro')
        self.plt.axis([0, self.size, 0, self.size])
        self.plt.grid(True)
        self.plt.plot([x], [y], 'go--')
        self.plt.show()


scheme = Scheme(matplotlib.pyplot, 10, 1, 1)
scheme.show(1, 1)
