import time


def repeater(call_count=3, start_sleep_time=2, factor=3, border_sleep_time=10):
    def decorator(foo):
        def wrapper(number):
            print(f'Кол-во запусков = {call_count}')
            print('Начало работы')
            t = start_sleep_time
            for i in range(call_count):
                func_result = foo(number)
                if i == call_count-1:
                    print(f'Запуск номер {i + 1}. Результат декорируемой функций = {func_result}.')
                    break
                print(f'Запуск номер {i + 1}. Ожидание: {t} секунд. Результат декорируемой функций = {func_result}.')
                time.sleep(t)
                t = t * 2 ** factor
                if t > border_sleep_time:
                    t = border_sleep_time
        return wrapper
    return decorator


def main():
    @repeater(call_count=4, start_sleep_time=1, border_sleep_time=9)
    def multiplier(number: int):
        return number * 2

    multiplier(7)


if __name__ == '__main__':
    main()
