import numpy as np
import random
#Белые - это синие
#Черные - это красные

#Война - это мир
#Свобода - это рабство
#Незнание - это сила

#TODO 1.	Поочередно осуществляется ввод расположение шашек на доске, в этот момент пользователь должен выбрать цвет своих шашек (количество шашек ограничено 6 для каждого цвета);
#TODO ограничения??

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
        d = {"A" : 0, "B" : 1, "C" : 2, "D": 3, "E":4, "F":5, "G":6 , "H":7,
            "a": 0, "b" : 1, "c" :2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7
        }
        if char in d:
            return d[char]
        else:
            raise ValueError("Нет ключа для полученного char {}".format(char))
    
    @staticmethod
    def checkxy_value(part):
        """Проверка на корректные на координаты xy"""
        if type(part) != str or len(part) != 2:
            return False

        l1 = ["A", "B", "C", "D", "E", "F", "G", "H", "a","b", "c", "d", "e", "f", "g", "h"]
        l2 = list(map(str, range(1,9)))
        if part[0] in l1 and part[1] in l2:
            return True
        return False

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
            color = "black"
        else:
            color = "white"
        
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
        #TODO figure_color2print_dict = {"black" : "🔴", "white": "🔵", "TEST" : "🍺"}
        figure_color2print_dict = {"black" : "👹", "white": "🍺", "TEST" : "💩"}
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

    def detect_element(self, search_x, search_y):
        """
        Определяем, есть ли элемент с такими координатами на доске
        Это необходимо для того, чтоб не выехать за массив
        """
        board = self.board
        for x in np.arange(8):
            for y in np.arange(8):
                if board[x][y].coord_x == search_x and board[x][y].coord_y == search_y:
                    return True
        return False

    def figure_generator(self):
        """Расстановка фигур по полю и их генерация"""
        board = self.board
        for x in np.arange(8):
            for y in np.arange(8):
                if x < 3 and ((x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1)):
                    board[x][y].field_reserve(FigureClass("white", x, y))
                elif x > 4 and ((x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1)):
                    board[x][y].field_reserve(FigureClass("black", x, y))
        
        self.board = board

    def __str__(self):
        """Вывод игровой доски не экран"""
        board = self.board
        for i in np.arange(board.shape[0]-1,-1,-1):
            print("{}".format(i+1), end="")
            for j in np.arange(board.shape[1]):
                print('{}'.format(board[i][j]), end="")
            print("")
        print("  A B C D E F G H")
        return ""

class AnalyserClass:
    """Класс ограничений и выявление некорректного хода"""
    def __init__(self, command_dict, board_obj):
        self.results_list = []
        self.command_dict = command_dict
        self.board_obj = board_obj

        self.backstep_detector()
        self.diagonal_detector()
        self.fieldtype_detector()

        if command_dict["mode"] == "war":
            self.war_detector()
        else:
            self.peace_detector()
        
        print(self.results_list)


    
    def backstep_detector(self):
        """Проверка на перемещение вперед"""
        d = self.command_dict
        print(d)
        if d["from"]["y"] > d["to"]["y"]:
            self.results_list.append(False)
        else:
            self.results_list.append(True)

    def diagonal_detector(self):
        """Проверка на осуществление перехода по диагонали"""
        #Возможные пути, куда может пойти шашка (их всего 4)
        board_obj = self.board_obj
        d = self.command_dict
        target_x = d["from"]["x"]
        target_y = UtilClass.char2xint(d["from"]["y"])
        #self.board_obj.board[target_x][target_y].figure_obj = FigureClass("TEST", target_x, target_y)
        ways_list = [[target_x+1,target_y+1], [target_x+2,target_y+2], [target_x+1,target_y-1], [target_x+2,target_y-2]]
        
        for l in ways_list:
            x, y = l
            self.board_obj.board[x][y].figure_obj = FigureClass("TEST", x, y)
                    

                

        

    def war_detector(self):
        """Проверка на осуществление перехода с боем"""
        pass

    def peace_detector(self):
        """Проверка на осуществление перехода с миром"""
        pass
    
    def fieldtype_detector(self):
        """
        Проверка на все, что связано с ячейкой.
        - Проверка на существование ячейки
        - Занятость ячейки
        - Цвет ячейки
        """
        pass

class MainClass:
    """Управляющий класс с логикой игры"""
    def __init__(self):
        self.stopgame_flag = False
        #Создаем доску
        board = BoardClass()
        print(board)
        self.board = board
        self.gameprocess()

    def command_parser(self, cmd):
        """
        Осуществление парсинга и фильтрации команды, которую ввел пользователь
        Если все хорошо - вызывается проверка на уровне
        """
        movement_type_dict = {":" : "war", "-" : "peace"}
        #Разделитель строки на 2 части
        spliter = None
        detect_flag = False
        for key in movement_type_dict.keys():
            if key in cmd:
                detect_flag = True
                spliter = key
                break
        
        if not detect_flag:
            print("Не найден разделитель комманд! ':' - перемещение с боем, '-' - тихое перемещение")
            return {}
        
        command_dict = {"from": {}, "to": {}, "mode": movement_type_dict[spliter]}
        #Разделяем введенную команду на 2 части
        part1, part2 = cmd.split(spliter)
        if UtilClass.checkxy_value(part1) and UtilClass.checkxy_value(part2):
            command_dict["from"]["y"] = part1[0]
            command_dict["from"]["x"] = int(part1[1])-1
            command_dict["to"]["y"] = part2[0]
            command_dict["to"]["x"] = int(part2[1])-1
            return command_dict

        print("Некорректный ввод данных!")
        return {}

        
    def gameprocess(self):
        """Управляющая логика работы игры"""
        while not self.stopgame_flag:
            cmd = input("Введите команду -> ")
            result = self.command_parser(cmd)
            if result != {}:
                obj = AnalyserClass(result, self.board)
                print(self.board)


            #Вызов фильтрации
            #Если все ок - вызываем AnalyserClass для проверки, если все ок - осуществляем перемещение

            
    def computer_game(self):
        """Осуществление хода компьютером"""
        pass

if __name__ == "__main__":
    MainClass()