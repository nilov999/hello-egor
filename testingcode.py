import numpy as np

# Напишем функцию, которая определит среднее количество попыток угадывания числ
def score_game(random_predict):
    """_summary_

    Args:
        random_predict (_type_): _description_

    Returns:
        _type_: _description_
    """
    count_ls = []
    # наш список, где мы сохраним количество попыток
    # Если вы дважды используете одно и то же начальное значение, вы получите один и тот же результат, что означает случайное число дважды.
    np.random.seed(1)
    random_array=np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток!')
    return (score)

score_game(random_predict)
