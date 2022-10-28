# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
def candy_game():
    candy_count = 50
    max_take = 28
    name1 = input('Введите имя первого игрока: ')
    name2 = input('Введите имя второго игрока: ')
    player1_count = 0
    player2_count = 0
    round = 1

    m = random.randint(0, 1)

    if m == 1:
        player1 = name1
        player2 = name2
    else:
        player1 = name2
        player2 = name1

    print(f'Игрок {player1} берет первым!')
        
    while candy_count > 0:
        print(f'Круг {round}:')
        player1_take = int(input(f'{player1}, сколько конфет хочешь взять? '))

        while player1_take > max_take:
            player1_take = int(input(f'Нельзя брать больше {max_take} конфет! {player1}, выбери другое количество: '))

        candy_count -= player1_take
        
        while candy_count < 0:
            candy_count += player1_take
            player1_take = int(input(f'Нельзя брать больше, чем осталось! {player1}, возьми другое количество: '))
            candy_count -= player1_take

        if candy_count == 0:
            print(f'Победил игрок {player1}!')
            break

        player1_count += player1_take
        print(f'Осталось {candy_count} конфет')
        player2_take = int(input(f'{player2}, сколько конфет хочешь взять? '))

        while player2_take > max_take:
            player2_take = int(input(f'Нельзя брать больше {max_take} конфет! {player2}, выбери другое количество: '))

        candy_count -= player2_take
        
        while candy_count < 0:
            candy_count += player2_take
            player2_take = int(input(f'Нельзя брать больше, чем осталось! {player2}, возьми другое количество: '))
            candy_count -= player2_take

        if candy_count == 0:
            print(f'Победил игрок {player2}!')
            break
        
        player2_count += player2_take
        print(f'Итоги круга {round}:\n{player1} - {player1_count} конфет \n{player2} - {player2_count} конфет. \nОсталось {candy_count}.')
        round += 1


def candy_game_bot():
    candy_count = 50
    max_take = 28
    user_name = input('Введите имя игрока: ')
    bot_name = 'Бот'
    player1_count = 0
    player2_count = 0
    round = 1

    m = random.randint(0, 1)
    player1 = user_name
    player2 = bot_name
    if m:
        print(f'{player1} ходит первым!')
    else:
        print(f'{player2} ходит первым!')
        
    while candy_count > 0:
        print(f'Круг {round}:')
        if m:
            player1_take = int(input(f'{player1}, сколько конфет хочешь взять? '))

            while player1_take > max_take:
                player1_take = int(input(f'Нельзя брать больше {max_take} конфет! {player1}, выбери другое количество: '))

            candy_count -= player1_take
        
            while candy_count < 0:
                candy_count += player1_take
                player1_take = int(input(f'Нельзя брать больше, чем осталось! {player1}, возьми другое количество: '))
                candy_count -= player1_take

            if candy_count == 0:
                print(f'Победил игрок {player1}!')
                break

            player1_count += player1_take
            print(f'Осталось {candy_count} конфет')
            player2_take = random.randint(1, max_take)
            candy_count -= player2_take
            
            while candy_count < 0:
                candy_count += player2_take
                player2_take = random.randint(1, candy_count)
                candy_count -= player2_take

            if candy_count == 0:
                print(f'Победил игрок {player2}!')
                break
            
            player2_count += player2_take
            print(f'Бот взял {player2_take} конфет')
            print(f'Итоги круга {round}:\n{player1} - {player1_count} конфет \n{player2} - {player2_count} конфет. \nОсталось {candy_count}.')
            round += 1
        else:
            player2_take = random.randint(1, max_take)
            candy_count -= player2_take
            while candy_count < 0:
                candy_count += player2_take
                player2_take = random.randint(1, candy_count)
                candy_count -= player2_take
            if candy_count == 0:
                print(f'Победил игрок {player2}!')
                break
            player2_count += player2_take
            print(f'Бот взял {player2_take} конфет')
            
            player1_take = int(input(f'{player1}, сколько конфет хочешь взять? '))

            while player1_take > max_take:
                player1_take = int(input(f'Нельзя брать больше {max_take} конфет! {player1}, выбери другое количество: '))

            candy_count -= player1_take
        
            while candy_count < 0:
                candy_count += player1_take
                player1_take = int(input(f'Нельзя брать больше, чем осталось! {player1}, возьми другое количество: '))
                candy_count -= player1_take

            if candy_count == 0:
                print(f'Победил игрок {player1}!')
                break

            player1_count += player1_take
            print(f'Итоги круга {round}:\n{player1} - {player1_count} конфет \n{player2} - {player2_count} конфет. \nОсталось {candy_count}.')
            round += 1
        

# candy_game() - вызов игры вдвоем
# candy_game_bot() - вызов игры с ботом
