import logging

# Работа с логированием
logger = logging.getLogger("LoggerLogger")
logger.setLevel(logging.INFO)

# Создан файл для логирования
file_handler = logging.FileHandler("log.log")
# Создание форматера отображающего дату, время, имя логгера, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

while True:
    logger.info('Program started')
    # Проверка на ввод данных и соответственно ввод данных
    try:
        k = int(input('Введите координату клетки фигуры по горизонтали: '))
        if k > 8 or k < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value. Out of range')
            continue
        l = int(input('Введите координату клетки фигуры по вертикали: '))
        if l > 8 or l < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value. Out of range')
            continue
        m = int(input('Введите координату атакуемой клетки по горизонтали: '))
        if m > 8 or m < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value. Out of range')
            continue
        n = int(input('Введите координату атакуемой клетки по вертикали: '))
        if n > 8 or n < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value. Out of range')
            continue
        figure = int(input('''Какую фигуру вы хотите использовать?
        1 -- Ферзь
        2 -- Ладья
        3 -- Слон
        4 -- Конь
        Ваш выбор: '''))
        if figure > 4 or figure < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value. Out of range')
            continue
    except ValueError:
        print('Введены некорректные данные. Попробуйте снова.')
        logger.error('Incorrect value. Incorrect input')
        continue
    fig = {1: 'ferzin', 2: 'rook', 3: 'bishop', 4: 'knight'}
    logger.info(f'Added coordinates ({k}; {l}) and ({m}; {n}) and chosen figure -- {fig[figure]}')
    # Проверка на совпадение цвета
    if (k + l) % 2 == (m + n) % 2:
        print('Они одного цвета --', end=' ')
        if (k + l) % 2 == 0:
            print('белого')
            logger.info('output: Они одного цвета -- белого')
        else:
            print('черного')
            logger.info('output: Они одного цвета -- черного')
    else:
        print('Нет, они не одного цвета')
        logger.info('output: Нет, они не одного цвета')

    # Расстояние по горизонтали и вертикали
    dx = abs(k - m)
    dy = abs(l - n)

    # Проверка угрожает ли фигура полю, а так же второй ход
    if figure == 1:     # Ферзь
        if k == m or l == n or dx == dy:
            print(f'Ферзь угрожает полю ({m}; {n})')
            logger.info(f'output: Ферзь угрожает полю ({m}; {n})')
        else:
            print(f'Ферзь не угрожает полю ({m}; {n})')
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m}; {l})')
            logger.info(f'output: Ферзь не угрожает полю ({m}; {n})'
                        f'\nЧтобы за два хода попасть в это поле необходимо встать на поле ({m}; {l})')
    elif figure == 2:   # Ладья
        if k == m or l == n:
            print(f'Ладья угрожает полю ({m}; {n})')
            logger.info(f'Ладья угрожает полю ({m}; {n})')
        else:
            print(f'Ладья не угрожает полю ({m}; {n})')
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m}; {l})')
            logger.info(f'Ладья не угрожает полю ({m}; {n})'
                        f'\nЧтобы за два хода попасть в это поле необходимо встать на поле ({m}; {l})')
    elif figure == 3:   # Слон
        if dx == dy:
            print(f'Слон угрожает полю ({m}; {n})')
            logger.info(f'Слон угрожает полю ({m}; {n})')
        else:
            print(f'Слон не угрожает полю ({m}; {n})')
            logger.info(f'Слон не угрожает полю ({m}; {n})')
            if (k + l) % 2 != (m + n) % 2:
                print(f'Слон никаким образом не может угрожать полю ({m}; {n})')
                logger.info(f'Слон никаким образом не может угрожать полю ({m}; {n})')
            else:   # Простите, мне лень придумывать нормальный алгоритм
                m0, n0, m1, n1 = m, n, 0, 0
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 += 1
                    n0 += 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = m
                n0 = n
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 += 1
                    n0 -= 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = m
                n0 = n
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 -= 1
                    n0 += 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = m
                n0 = n
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 -= 1
                    n0 -= 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m1}; {n1})')
                logger.info(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m1}; {n1})')
    else:   # Конь
        if abs(dx - dy) == 1:
            print(f'Конь угрожает полю ({m}; {n})')
            logger.info(f'Конь угрожает полю ({m}; {n})')
        else:
            print(f'Конь не угрожает полю ({m}; {n})')
            logger.info(f'Конь не угрожает полю ({m}; {n})')
    break
input('Press ENTER to exit')
logger.info('Program done')
