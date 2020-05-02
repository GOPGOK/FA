import numpy as np
import random
#Белые - это синие
#Черные - это красные

#TODO 1.	Поочередно осуществляется ввод расположение шашек на доске, в этот момент пользователь должен выбрать цвет своих шашек (количество шашек ограничено 6 для каждого цвета);
class UtilClass:
    """Класс со всякой фигней"""
    @staticmethod
    def xint2char(xint):
        """Конвертирование числа в букву"""
        d = {0:"A",1:"B", 2:"C", 3:"D", 4:"E", 5: "F", 6: "G", 7: "H"}
        
        if xint in d:
            return d[xint]
        else:
            raise ValueError("Нет ключа для полученного xint {}".format(xint))
     
    @staticmethod
    def char2xint(char):
        """Конвертирование буквы в число"""
        d = {"A" : 0, "B" : 1, "C" : 2, "D": 3, "E":4, "F":5, "G":6 , "H":7}
        if char in d:
            return d[char]
        else:
            raise ValueError("Нет ключа для полученного char {}".format(char))
     
class FieldClass:
    """
    Класс 1 клетки доски
    Поля:
    - Координата X
    - Координата Y
    - Занята или нет, если занята то кем?
    - Цвет клетки
    - Ссылка на объект фигуры, которая стоит на клетке
    
    Методы:
    - Занятие/резервация клетки фигурой
    - Освобождение клетки фигурой
    """
    def __init__(self, coord_x, coord_y, figure_obj=None):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.figure_obj = figure_obj
        self.color_generator()
    
    def color_generator(self):
        """Генератор цвета ячейки на основе ее координат"""
        x = UtilClass.char2xint(self.coord_x)
        y = self.coord_y

        if (x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
            color = "white"
        else:
            color = "black"
        
        self.color = color
    
    def isfree(self):
        """Проверяет, свободна ли текущая ячейка"""
        if self.figure_obj == None:
            return True
        return False

    def field_reserve(self, figure_obj):
        """
        Занятие клетки фигурой
        """
        self.figure_obj = figure_obj

    def field_free(self):
        """
        Освобождение клетки фигурой
        """
        self.figure_obj = None

    def __str__(self):
        """Вывод ячейки на экран"""
        board_color2print_dict = {"black" : "⬛️", "white": "⬜️"}
        figure_color2print_dict = {"black" : "🔴", "white": "🔵"}
        #Если ячейка свободная -> выводим просто ее цвет на экран
        if self.isfree():
            return board_color2print_dict[self.color]
        #Если ячейка занята -> выводим цвет шашки, которую она занимает
        return figure_color2print_dict[self.figure_obj.color]

class FigureClass:
    """
    Класс фигуры (шашки)
    Поля:
    - Координата X
    - Координата Y
    - Цвет (черный/белый) генерится автоматически
    """
    def __init__(self, color, coord_x, coord_y):
        self.color = color
        self.coord_x = coord_x
        self.coord_y = coord_x

    def movement(self, oldfield_obj, newfield_obj):
        """
        Осуществление перемещения фигуры
        - Удаление привязки в ячейке
        - Изменение координат фигуры
        - Привязка к новой ячейке
        """
        oldfield_obj.figure_obj = None
        self.coord_x = newfield_obj.coord_x
        self.coord_x = newfield_obj.coord_y
        newfield_obj.figure_obj = self

class BoardClass:
    """Класс игровой доски"""
    def __init__(self):
        self.board = None
        self.board_generator()
        print(self)
        self.figure_generator()

    def board_generator(self):
        """Создание чистого игрового поля без фигур"""

        board = np.array([])
        for x in np.arange(8):
            for y in np.arange(8):
                field_obj = FieldClass(UtilClass.xint2char(x), y) 
                board = np.append(field_obj, board)
        
        self.board = np.array(board.reshape(8,8))

    def figure_generator(self):
        """Расстановка фигур по полю и их генерация"""
        board = self.board
        for x in np.arange(8):
            for y in np.arange(8):
                if x < 3 and not((x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1)):
                    board[x][y].field_reserve(FigureClass("black", x, y))
                elif x > 4 and not((x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1)):
                    board[x][y].field_reserve(FigureClass("white", x, y))
        
        self.board = board

    def __str__(self):
        """Вывод игровой доски не экран"""
        board = self.board
        for i in np.arange(board.shape[0]):
            for j in np.arange(board.shape[1]):
                print('{}'.format(board[i][j]), end="")
            print("")
        return ""

        
class MainClass():
    """Управляющий класс с логикой игры"""
    def __init__(self):
        self.stopgame_flag = False
        #Создаем доску
        board = BoardClass()
        print(board)
        self.gameprocess()

    def gameprocess(self):
        """Управляющая логика работы игры"""
        while not self.stopgame_flag:
            command_input = input("Введите команду -> ")
            
    def computer_game(self):
        """Осуществление хода компьютером"""
        pass

if __name__ == "__main__":
    MainClass()