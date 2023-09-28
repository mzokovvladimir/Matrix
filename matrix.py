import sys
import random
import time

# Підключаємо додаткові модулі
try:
    import bext, colorama
except ImportError:
    print('Для запуску програми потрібні модулі bext та colorama.')
    sys.exit()


class Drop:
    def __init__(self):
        self.x: int = random.randint(0, width)  # Початкове положення по горизонталі
        self.y: int = -1  # Початкове положення по вертикалі - за верхньою межею екрану
        self.drop_type: int = random.randint(0, 1)  # Тип: антикрапля або крапля
        self.timeout: int = random.randint(0, 3)  # Затримка до наступного переміщення
        self.wait_count: int = random.randint(0, 3)  # Лічильник паузи

    def renew(self):
        self.__init__()

    def move(self) -> bool:
        if drop.wait_count < drop.timeout:  # Поки рано переміщувати
            drop.wait_count += 1  # Збільшуємо лічильник паузи
            return False
        else:  # Вже можна переміщувати
            drop.wait_count = 0  # Скидаємо лічильник паузи
            drop.y += 1  # Переміщуємо краплю або антикраплю на крок вниз
            return True

    def draw(self):
        if self.drop_type == 1:
            symbol = str(random.randint(1, 9))
            con_print(self.x, self.y, green, symbol)
            self.zero_draw()  # Малюємо яскравий нуль
        else:
            con_print(self.x, self.y, green, ' ')

    def zero_draw(self):
        if self.y < height:
            con_print(self.x, self.y + 1, lgreen, '0')


def is_rb_corner(x: int, y: int) -> bool:
    if x == width and y == height:
        return True
    else:
        return False


def con_print(x: int, y: int, color: str, symbol: str):
    if not is_rb_corner(x, y):
        bext.goto(x, y)
        sys.stdout.write(color)
        print(symbol, end='')


bext.title('Matrix')  # Змінюємо заголовок консольного вікна
bext.clear()  # Очищуємо консольне вікно
bext.hide()  # Ховаємо курсор у консольному вікні
width, height = bext.size()  # Отримаємо розмір консольного вікна
width -= 1
height -= 1

green = colorama.Fore.GREEN
lgreen = colorama.Fore.LIGHTGREEN_EX

# Створюємо масив крапель та антикрапель
drops: list = []
for i in range(1, width * 2 // 3):
    drop = Drop()
    drops.append(drop)

while True:
    for drop in drops:
        if drop.move():  # Перевіряємо переміщення елементу
            drop.draw()  # Відображаємо елемент
            if drop.y >= height:  # Досягли дна
                drop.renew()  # Оновлюємо елемент
    key = bext.getKey(blocking=False)  # Перевіряємо, чи натиснута клавіша
    if key == 'esc':  # Якщо натиснута ESC, то виходимо з програми
        bext.clear()
        sys.exit()
    time.sleep(0.02)  # Затримка
