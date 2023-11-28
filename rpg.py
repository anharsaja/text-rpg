import os

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
    os.system('cls')

def credits():
    print("""\n\n\n
                     ______ _______  _______  __            __    __ ________ __       ______  __       __ _______   ______  __    __       ______  
                    |      |       \|       \|  \          |  \  /  |        |  \     /      \|  \     /  |       \ /      \|  \  /  \     /      \ 
                     \$$$$$| $$$$$$$| $$$$$$$| $$          | $$ /  $| $$$$$$$| $$    |  $$$$$$| $$\   /  $| $$$$$$$|  $$$$$$| $$ /  $$    |  $$$$$$\\
                      | $$ | $$__/ $| $$__/ $| $$          | $$/  $$| $$__   | $$    | $$  | $| $$$\ /  $$| $$__/ $| $$  | $| $$/  $$     | $$__/ $$
                      | $$ | $$    $| $$    $| $$          | $$  $$ | $$  \  | $$    | $$  | $| $$$$\  $$$| $$    $| $$  | $| $$  $$       \$$    $$
                      | $$ | $$$$$$$| $$$$$$$| $$          | $$$$$\ | $$$$$  | $$    | $$  | $| $$\$$ $$ $| $$$$$$$| $$  | $| $$$$$\       _\$$$$$$$
                     _| $$_| $$     | $$     | $$_____     | $$ \$$\| $$_____| $$____| $$__/ $| $$ \$$$| $| $$     | $$__/ $| $$ \$$\     |  \__/ $$
                    |   $$ | $$     | $$     | $$     \    | $$  \$$| $$     | $$     \$$    $| $$  \$ | $| $$      \$$    $| $$  \$$\     \$$    $$
                     \$$$$$$\$$      \$$      \$$$$$$$$     \$$   \$$\$$$$$$$$\$$$$$$$$\$$$$$$ \$$      \$$\$$       \$$$$$$ \$$   \$$      \$$$$$$ 
                                                            
    """)
    print(' '*65, 'Anhar Mukhlis')
    print(' '*65, 'Danu Adiwidya')
    input()


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


# unit testing ==================================================================

def lobby(menu):
    if menu == '1':
        
        return 'play game'
    elif menu == '2':
        clear()
        credits()
        main_menu()
        return 'credits menu'
    elif menu == '3':
        clear()
        return 'exit game'    
    else:
        main_menu()
        return 'wrong input'    


# def lobby():


# main_menu()
if __name__ == '__main__':
    main_menu()
