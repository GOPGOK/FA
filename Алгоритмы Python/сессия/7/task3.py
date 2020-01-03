"""
(20 баллов) Дробь задается списком из 2 чисел: числителя и знаменателя.
Например, [24,5], [2,3], [8,2].
Напишите функцию, которая выводит эту дробь в виде смешанного числа (сокращать дробь не нужно), как показано ниже. 
Если дробная часть смешанного числа равна нулю, она не печатается.
Если исходная дробь была правильной, то печатается сообщение «правильная дробь». Например,
24/5 = 4 4/5 ,		2/3 – правильная дробь ,		8/2 = 4
Параметром функции является список из 2 целых чисел.

(10 баллов) Создайте с помощью присваивания список, содержащий несколько дробей.
Вызовите созданную функцию для каждого элемента этого списка.

(10 баллов) Если параметр функции не является списком из 2 целых чисел,
то функция генерирует собственное исключение.
Добавьте в программу обработку исключений (как собственного, так и стандартных).
"""


def converter(input_list):
    
    if type(input_list) != list or input_list == []:
        raise TypeError()
    #Выходня строка
    out_str = ""
    # Разделение на 1 и 2 эелмент a и b
    a, b = input_list

    #Если исходная дробь неправильная
    if a > b:
        
        result = a/b

        #Если есть нет остатка дроби
        if int(result) == result:
            
            out_str = str(a)+"/"+str(b)+" = "+str(int(result))
        
        #Если есть остаток дроби
        else:
            
            integ = a // b # целая часть
            fract = a % b  # дробная часть

            #Результат
            out_str = str(a)+"/"+str(b)+" = "+str(integ)+" "+str(fract)+"/"+str(b)
    
    #Если исходная дробь правильная
    else:
        out_str = str(a)+"/"+str(b)+" – правильная дробь"

    #Вывод
    print(out_str)



if __name__ == "__main__":

    locale_list = [[24,5], [2,3], [8,2]]
    for e in locale_list:
        try:
            converter(e)
        except ValueError:
            print("В словаре не 2 элемента")
        
        except TypeError:
            print("Неверные аргументы в функции")
       
        except Exception as e:
            print("Неожиданная ошибка:", e)