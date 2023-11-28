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
    temp_list = [str(i + 1) for i in range(len(main_menu_options))]

    if user_choice not in temp_list and user_choice != '0':
        # alert
        print('wrong input')
        return main_menu()
    return main_menu_options[int(user_choice)-1]

def lobby(menu):
    if menu == '1':
        pass
    elif menu == '2':
        clear()
        return 'IPPL KELOMPOK 9'
        input()
        main_menu()
    elif menu == '3':
        clear()
        return 'Exit Game'        


# def lobby():


# main_menu()
if __name__ == '__main__':
    lobby(main_menu())
