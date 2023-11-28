import os
import random as rn

char_atk = 1
char_def = 1
money = 1000
xp = 10
status = False


def cover():
    clear()
    print(
        """                                         `                                                                                                                             ``           
       ./:------...`           `-/      ..........`       .......   `.....           `-:::-.`      `.----.`     .......     ......`.......           .----.`   ..           
       `+yNNNdyssyhddy/.     `/hNN-     /yNNNdyydmdo.     :yNNNy-  `ommhs/`        .ymmyssdmy`  `/sdho++oydy+.  :smmmo:     :smmo-`/ymmmo/        `/hds+oymh-               
         .MMM:    `:hMMms`   `hMMMd`     .NMMo``.yMMm.     :MMM-  .yNd/.          `hMM+`  .sy` /dMm/`    `/mMmo` .NMM.       `dh`   /MMd`         +MMo`` `/d:               
         `MMN.      `yMMMs   :NhNMMs`    `NMMo   +MMM-     :MMM.`+mm+`    ```     `dMMd/`  `` :NMM/        -dMMy``NMM.       `hy    :MMd`         +MMm/.   `                
`````````.MMM. ``.```:NMMN-.-dh:sMMN/```.-NMMy//omMms.``   :MMMhdMd:```  ``` `     -dNMMmy+-.`yMMN-````````.oMMM:-NMM-```.```.dy.```/MMd.````  ```.smMMmho:...``````        
 ````````.NMM- ```` `.mMMN..hMhyyNMMm-``..NMMdsmMMm:```    :MMMsdMNy:``.          ` `:ohNMMNo.sMMN-`````````+MMM/.NMM-`````` .my`  `/MMd`` `    ````.+ymMMNy.````           
         `mMM.       -NMN+`sN+:::/NMMy`  `NMMs`-hMMh-      :MMM-`+mMNs..          ./   `-sMMN--mMMo`       `hMMh``mMM:       .No    /MMd`      `  :`   `/mMM/               
         `mMM:    `./mMd/`+Ms     /MMM+  .NMMs  `sNMm/`    :MMM-  .sNMmo.        `yNo.   `mMN- :mMMo.     .sMNy.  oNMd-     .ym-    /MMm`     -h:+Ns.    +MM+               
       `+sNMMmsooshdds/./sNN/`    -mNNmo/sNNNd:   :ymmy:` -sNNNo`  `oNNNdo-`     `/mNms//smy-   .+dmho++oshds:`    /hNmhoooyhs-   ./hNNNs+//+odN/-yNds//odmo`               
       `:::::::::--.`  `--:--`    .------------     `.--` .-----`   .------.       .:////:.       `.-:///:.`         .:///:-`     .-------------`  -:///:-`               
\n"""
        + " " * 70
        + "T E X T   R P G \n\n"
    )


def clear():
    os.system("cls")


def credits():
    print(
        """\n\n\n
                     ______ _______  _______  __            __    __ ________ __       ______  __       __ _______   ______  __    __       ______  
                    |      |       \|       \|  \          |  \  /  |        |  \     /      \|  \     /  |       \ /      \|  \  /  \     /      \ 
                     \$$$$$| $$$$$$$| $$$$$$$| $$          | $$ /  $| $$$$$$$| $$    |  $$$$$$| $$\   /  $| $$$$$$$|  $$$$$$| $$ /  $$    |  $$$$$$\\
                      | $$ | $$__/ $| $$__/ $| $$          | $$/  $$| $$__   | $$    | $$  | $| $$$\ /  $$| $$__/ $| $$  | $| $$/  $$     | $$__/ $$
                      | $$ | $$    $| $$    $| $$          | $$  $$ | $$  \  | $$    | $$  | $| $$$$\  $$$| $$    $| $$  | $| $$  $$       \$$    $$
                      | $$ | $$$$$$$| $$$$$$$| $$          | $$$$$\ | $$$$$  | $$    | $$  | $| $$\$$ $$ $| $$$$$$$| $$  | $| $$$$$\       _\$$$$$$$
                     _| $$_| $$     | $$     | $$_____     | $$ \$$\| $$_____| $$____| $$__/ $| $$ \$$$| $| $$     | $$__/ $| $$ \$$\     |  \__/ $$
                    |   $$ | $$     | $$     | $$     \    | $$  \$$| $$     | $$     \$$    $| $$  \$ | $| $$      \$$    $| $$  \$$\     \$$    $$
                     \$$$$$$\$$      \$$      \$$$$$$$$     \$$   \$$\$$$$$$$$\$$$$$$$$\$$$$$$ \$$      \$$\$$       \$$$$$$ \$$   \$$      \$$$$$$ 
                                                            
    """
    )
    print(" " * 70, "# Anhar Mukhlis")
    print(" " * 70, "# Dwi Ananta")
    print(" " * 70, "# Danu Adiwidya")
    print(" " * 70, "# Thariq Aziz")
    print(" " * 70, "# Agung Firman")
    input("\nPress enter to Back ...")


def character_view():
    main_menu_options = ["Level", "XP", "Attack Power", "Deffend", "Money"]
    stats = [xp // 10, xp, char_atk, char_def, money]
    st = 0
    for index in range(len(main_menu_options)):
        chose = main_menu_options[index].upper()
        print(" " * 58 + "=" * 40)
        print(
            " " * 57
            + "|"
            + " " * 5
            + chose
            + " " * (15 - len(chose))
            # + stats[index]
            + "|"
            + " " * 4
            + str(stats[st])
            + " " * (15 - len(str(stats[st])))
            + "|"
        )
        st += 1

    print(" " * 58 + "=" * 40)
    input(" " * 70 + "enter to Back ...")
    survival()


def dungeon_quest():
    name_monster = [
        "Crocodile",
        "Skeleton",
        "Eagle",
        "Ghost",
        "Crussader",
        "Phoenix",
        "Giant",
    ]
    monster_atk1 = rn.randint(char_atk - 1, char_atk + 2)
    monster_def1 = rn.randint(char_def - 1, char_def + 2)
    monster_atk2 = rn.randint(char_atk - 1, char_atk + 2)
    monster_def2 = rn.randint(char_def - 1, char_def + 2)
    monster_atk3 = rn.randint(char_atk - 1, char_atk + 2)
    monster_def3 = rn.randint(char_def - 1, char_def + 2)

    print(
        f"""
    1. {name_monster[rn.randint(0, 6)]}, attack : {monster_atk1}, deffend : {monster_def1}
    2. {name_monster[rn.randint(0, 6)]}, attack : {monster_atk2}, deffend : {monster_def2}
    3. {name_monster[rn.randint(0, 6)]}, attack : {monster_atk3}, deffend : {monster_def3}
    4. Back
"""
    )

    menu = input("Pilih monster / Enter untuk refresh monster : ")
    if menu == "1":
        finished_dungeon_quest(monster_atk1, monster_def1)
        clear()
        dungeon_quest()
    elif menu == "2":
        finished_dungeon_quest(monster_atk2, monster_def2)
        clear()
        dungeon_quest()
    elif menu == "3":
        finished_dungeon_quest(monster_atk3, monster_def3)
        clear()
        dungeon_quest()
    elif menu == "4":
        main_menu()
    else:
        clear()
        dungeon_quest()


def finished_dungeon_quest(monster_atk, monster_def):
    global xp
    global money
    if char_atk + char_def > monster_atk + monster_def:
        xp += 5
        money += 100
        return "VICTORY"
    elif char_atk + char_def < monster_atk + monster_def:
        return "DEFEAT"
    else:
        return "DRAW"


def shop_menu():
    main_menu_options = ["Increase Attack (500)", "Increase Deffend (500)", "Back Menu"]
    for index in range(len(main_menu_options)):
        chose = main_menu_options[index].upper()
        print(" " * 58 + "=" * 40)
        print(
            " " * 49
            + f"<| {index + 1} |> "
            + "|"
            + " " * (20 - len(chose) // 2)
            + chose
            + " " * (20 - len(chose) // 2 - len(chose) % 2)
            + "|"
            + f" <| {index + 1} |> "
        )
    print(" " * 58 + "=" * 40)
    print(" " * 70, f"money : {money}")
    user_choice = input("\n" + " " * 75 + ">| ")
    shop(user_choice)
    clear()
    shop_menu()
    if user_choice == "1":
        shop(user_choice)
        clear()
        shop_menu()
    elif user_choice == "2":
        shop(user_choice)
        clear()
        shop_menu()
    else:
        clear()
        survival()


def shop(user_choice):
    global char_atk
    global char_def
    global money
    if user_choice == "1":
        if money >= 500:
            char_atk += 1
            money -= 500
            return 'success'
        else:
            return "failed"
    elif user_choice == "2":
        if money >= 500:
            char_def += 1
            money -= 500
            return 'success'
        else:
            return "failed"


# unit testing ==================================================================


def main_menu():
    cover()
    main_menu_options = ["Play Game", "Credits", "Exit Game"]
    for index in range(len(main_menu_options)):
        chose = main_menu_options[index].upper()
        print(" " * 58 + "=" * 40)
        print(
            " " * 49
            + f"<| {index + 1} |> "
            + "|"
            + " " * (20 - len(chose) // 2)
            + chose
            + " " * (20 - len(chose) // 2 - len(chose) % 2)
            + "|"
            + f" <| {index + 1} |> "
        )
    print(" " * 58 + "=" * 40)

    # input part
    user_choice = input("\n" + " " * 75 + ">| ")
    lobby(user_choice)


def survival():
    clear()
    print("\n", " " * 55, "==== GAME LOBBY ====\n")
    menu = ["Character Stats", "Dungeon", "Shop", "Back Menu"]
    for index in range(len(menu)):
        chose = menu[index].upper()
        print(" " * 58 + "-" * 20)
        print(
            " " * 49
            + f"  ( {index + 1} ) "
            + "|"
            + " " * (10 - len(chose) // 2)
            + chose
            + " " * (10 - len(chose) // 2 - len(chose) % 2)
            + "|"
        )
    print(" " * 58 + "-" * 20)

    choice = int(input("\n" + " " * 66 + ">| "))
    if choice == 1:
        clear()
        character_view()
    elif choice == 2:
        clear()
        dungeon_quest()
    elif choice == 3:
        clear()
        shop_menu()
    elif choice == 4:
        clear()
        main_menu()
    else:
        pass


def lobby(menu):
    if menu == "1":
        survival()
    elif menu == "2":
        clear()
        credits()
        main_menu()
    elif menu == "3":
        clear()
        return "exit game"
    else:
        return "wrong input"


# main_menu()
if __name__ == "__main__":
    main_menu()
