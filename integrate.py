import unittest
import rpg


class intertest(unittest.TestCase):
    def dungeon_test():
        # based character
        rpg.character_view()

        # intergrate dungeon
        rpg.finished_dungeon_quest(0, 0)
        rpg.finished_dungeon_quest(1, 0)
        rpg.finished_dungeon_quest(0, 1)
        rpg.finished_dungeon_quest(1, -1)
        rpg.character_view()

    def shop_test():
        # based character
        rpg.character_view()

        # intergrate dungeon
        rpg.shop('1')
        rpg.shop('2')
        rpg.character_view()



    # dungeon_test()
    shop_test()



if __name__ == "__main__":
    unittest.main()
