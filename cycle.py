# Вводим имена игроков и вводи их счет.
# Цикл
#   Игроки делают ставки.
#   Игроки бросили кубики.
#       Если у первого игрока больше очков, то он выигрывает.
#           То первый игрок забирает ставкку второго.
#       второй теряет свою ставку.
#   Иначе если  воторого игрока очков больше то:
#            То второй игрок забирает ставкку второго.
#       первый теряет свою ставку.
#       Иначе 
#       Ничья
#   Если у первого игрока на счету 0 или меньше. то он проиграл
#   Если у второго игрока на счету 0 или меньше. то он проиграл
import random,math
player1= {"кеш": 5000}
player2= {"кеш": 5000}

player1["имя"] = input("Введите имя первого игрока ")
player2["имя"] = input("Введите имя второго игрока ")
while True:
    player1["ставка"] = int(input("Введите ставку " + player1["имя"] +": "))
    player2["ставка"] = int(input("Введите ставку " + player2["имя"] +": "))
    player1["Бросок"] = random.randint(2, 12)
    player2["Бросок"] = random.randint(2, 12)

    if player1["Бросок"] > player2["Бросок"]: 
        print(player1["имя"]+" выиграл ")
        player1["кеш"] += player2["ставка"]
        player1["кеш"] -= player2["ставка"]
    elif player1["Бросок"] > player2["Бросок"]:
        print(player1["имя"]+" выиграл ")
        player2["кеш"] += player1["ставка"]
        player1["кеш"] -= player1["ставка"]
    else:
         print("ничья")
         print(player1["имя"], player1["кеш"])
         print(player2["имя"], player2["кеш"])

    if player1["кеш"]<= 0:
        print(player1["имя"], "проиграл")
        break
    


    
