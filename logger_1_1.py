# 1.Доработать декоратор logger в коде ниже. 
# Должен получиться декорaтор, который записывает в 
# файл 'main.log' дату и время вызова функции, имя функции, аргументы, 
# с которыми вызвалась и возвращаемое значение. 
# Функция test_1 в коде ниже также должна отработать без ошибок.

import os
import datetime
import logging


def logger(old_function):
    time_now = datetime.datetime.now()    
    def new_function(*args, **kwargs):
        
        print(f'Дата и время вызова функции {time_now}')
        print(f'Имя функции {old_function.__name__}')
        print(f'{args=}')
        print(f'{kwargs=}')
        
        value = old_function(*args, **kwargs)
        
        print(f'returned value is {value}')
        
        message = (f'{time_now}, {old_function.__name__}, {args=}, {kwargs=}, {value}')
        logging.basicConfig(filename='main.log', level=logging.DEBUG)
        logging.debug(message)
        

        return value
    
    return new_function
    

def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()

