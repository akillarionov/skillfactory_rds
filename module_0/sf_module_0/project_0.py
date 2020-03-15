# Проект 0. Алгоритм отгадывания случайного числа от 1 до 99
import numpy as np
number = np.random.randint(1, 99)  # загадали число number
print ("Загадано число от 1 до 99")

def game_final(number):
    count = 0
    low_border = 0 # создана нижняя граница интервала загаданного числа
    high_border = 100 # и верхняя граница интервала
    predict = np.random.randint(1, 99) # первая попытка - случайное число от 1 до 99
    while number != predict:
        count += 1
        if number > predict:
            low_border = predict # смещение нижней границы
            predict += (high_border - low_border) // 2 #следующая попытка - середина нового интервала, начинающаяся с predict
        elif number < predict:
            high_border = predict # смещение верхней границы
            predict -= (high_border - low_border) // 2 #следующая попытка - середина нового интервала, заканчивающегося predict
    return (count)  # выход из цикла, если угадали

def score_game(game_final):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(game_final(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

# запускаем
score_game(game_final)