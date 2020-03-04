#TODO возможность ставить на несколько тараканов
from random import randint
from faker import Faker
from time import sleep
import texttable


class CockroachClass():
    """
    Класс таракан
    """

    def __init__(self, name):
        self.__name = name
        self.__current_location = 0
        self.__speed_generator()

    def movement_changer(self):
        self.movement = bool(randint(0, 1))
        # Если было перемещение
        if self.movement:
            self.__current_location += self.__speed

    def __speed_generator(self):
        # Генерация скорости
        self.__speed = randint(1, 10)

    @property
    def name(self):
        return self.__name

    @property
    def current_location(self):
        return self.__current_location

    @property
    def speed(self):
        return self.__speed

class GamerClass():
    """
    Класс геймер, что у него есть:
    - Таракан ( может ващ объект передавать?)
    - Деньги

    Один игрок = один таракан
    """

    def __init__(self, name):
        self.__name = name
        self.__cockroach_obj = None
        self.__money = None

    @property
    def cockroach_obj(self):
        return self.__cockroach_obj

    @cockroach_obj.setter
    def cockroach_obj(self, obj):
        assert isinstance(obj, CockroachClass), "Некорректное значение"
        self.__cockroach_obj = obj

    @property
    def name(self):
        return self.__name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, val):
        """
        Осуществление set'а ставки
        """
        assert type(val) == float, "Некорректное значение"
        self.__money = val


class MainClass():

    def __init__(self):

        self.COCKROACH_ICON = "🦗"
        self.GRASS_ICON = "_"
        self.COCKROACH_COUNT = 4
        self.ITERATIONS_COUNT = 50

        # Хранит объекты тараканов
        self.cockroach_list = []
        
        # Храние объекты игроков
        self.user_list = []
        fake = Faker(['ru_RU'])

        # Генерация пользователей
        self.user_input_generator()

        # Начальная матрица
        self.start_matrix_generator()

        # Генерируем тараканов
        for i in range(self.COCKROACH_COUNT):
            cockroach_obj = CockroachClass(fake.word())
            self.cockroach_list.append(cockroach_obj)

        # Выбор ассоциации пользователь -> таракан
        self.user_chooser()

        # Основная логика
        for current_iteration in range(self.ITERATIONS_COUNT):

            print("Итерация №{}".format(current_iteration))
            # Отображение рейтинга тараканов
            self.rating_drawer()
            self.game_field_drawer()
            input()

            try:
                self.cockroach_changer()
            # Если допрыгались до IndexError
            except IndexError:
                self.winner_detector()
                break

    def user_chooser(self):
        """
        Выбор ассоциации пользователь -> таракан
        """
        
        for user in self.user_list:
            
            
                    
            allowed_cockroach_list = []
                    

            table = texttable.Texttable()
            table_list = [["№", "Кличка", "Скорость"],]
                    
            for i in range(len(self.cockroach_list)):
                        
                e = self.cockroach_list[i]
                allowed_cockroach_list.append(i+1)
                table_list.append([str(i+1), e.name, str(e.speed)])

            table.add_rows(table_list)
            print(table.draw() + "\n")


            processing_flag = True
            while processing_flag:
                try:
                    print("Выберите № таракана для игрока '{}':".format(user.name))
                    
                    # Выбираем таракана
                    selected_cockroach = int(input("\n-> "))
                    if selected_cockroach not in allowed_cockroach_list:
                        raise ValueError("Некорректный ввод номера таракана")
                    
                    obj = self.cockroach_list[selected_cockroach-1]
 
                    # Делаем ставку
                    money = float(input("Введите вашу ставку на выигрыш '{}' -> ".format(obj.name)))

                    # Вводим ассоциацию
                    obj.selected = True
                    user.cockroach_obj = obj
                    user.money = money
                    processing_flag = False
                
                except ValueError as e:
                    print(e)
                    continue

    def rating_drawer(self):
        """
        Рисовальщик рейтинга тараканов
        """
        #TODO вывод игрока
        cockroach_list = self.cockroach_list.copy()
        cockroach_list.sort(key=lambda e: e.current_location, reverse=True)
        table = texttable.Texttable()
        
        table_list = [
            ["Место", "Кличка", "Точка"],
        ]

        for i in range(len(cockroach_list)):
            e = cockroach_list[i]
            table_list.append([str(i+1), e.name, str(e.current_location)])

        table.add_rows(table_list)
        print(table.draw() + "\n")

    def winner_detector(self):
        """
        Метод, определяющий то, какой таракан выиграл
        """
        winner = sorted(self.cockroach_list,
                        key=lambda e: e.current_location, reverse=True)[0]
        print("Победитель: {}".format(winner.name))
        self.rating_drawer()

        # Обнуляем все т.к. в подобных играх все по дефолту проигрывают
        for u in self.user_list:
            u.money = 0.0

        old_money = []
        win_obj_usesrs_list = []
        # Ищем игроков-победителей
        # Ищем игрока-победителя
        for u in self.user_list:
            if u.cockroach_obj == winner:
                win_obj_usesrs_list.append(u)
            else:
                
                all_money = GamerClass.static_all_money
                print("{} получает сумму {} руб.!".format(u.name, all_money))
                u.money = float(all_money)

    def user_input_generator(self):
        """
        Ввод количества пользователей для ставок
        """
        input_flag = True
        while input_flag:
            try:
                users_count = int(input("Введите количество игроков -> "))
                input_flag = False
            except ValueError:
                continue
    
        # Генерируем пользователей
        for i in range(users_count):
            curent_user_name = input("Введите ФИО пользователя №{} -> ".format(i+1))
            user_obj = GamerClass(curent_user_name)
            self.user_list.append(user_obj)
        

    def start_matrix_generator(self):
        """
        Метод генерации начальной матрицы
        """
        # Начальная матрица
        self.matrix = [[self.GRASS_ICON for c in range(
            self.ITERATIONS_COUNT)] for r in range(self.COCKROACH_COUNT)]
        for i in range(len(self.matrix)):
            self.matrix[i][0] = self.COCKROACH_ICON

    def cockroach_changer(self):
        """
        Осуществление перемещения таракана
        """
        self.matrix = [[self.GRASS_ICON for c in range(
            self.ITERATIONS_COUNT)] for r in range(self.COCKROACH_COUNT)]

        for i in range(len(self.cockroach_list)):

            e = self.cockroach_list[i]
            e.movement_changer()
            self.matrix[i][e.current_location] = self.COCKROACH_ICON

    def game_field_drawer(self):
        """
        Отображение на экране
        """

        for i in range(len(self.matrix)):
            print(i+1, end=" ")
            for j in range(len(self.matrix[i])):
                print('{}'.format(self.matrix[i][j]), end=" ")
            print("|   Таракан '{}'".format(self.cockroach_list[i].name))

        print("\n")


if __name__ == "__main__":
    obj = MainClass()
