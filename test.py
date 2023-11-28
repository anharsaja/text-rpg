import unittest
import rpg


class testcal(unittest.TestCase):
    def test_finished_dungeon_victory1(self):
        result = rpg.finished_dungeon_quest(0, 0)
        self.assertEqual(result, 'VICTORY')

    def test_finished_dungeon_victory2(self):
        result = rpg.finished_dungeon_quest(1, 0)
        self.assertEqual(result, 'VICTORY')

    def test_finished_dungeon_draw(self):
        result = rpg.finished_dungeon_quest(1, 1)
        self.assertEqual(result, 'DRAW')
    def test_finished_dungeon_draw2(self):
        result = rpg.finished_dungeon_quest(2, 0)
        self.assertEqual(result, 'DRAW')

    def test_finished_dungeon_defeat(self):
        result = rpg.finished_dungeon_quest(2, 2)
        self.assertEqual(result, 'DEFEAT')

    def test_finished_dungeon_defeat2(self):
        result = rpg.finished_dungeon_quest(2, 3)
        self.assertEqual(result, 'DEFEAT')


    
    def test_lobby(self):
        result = rpg.lobby('3')
        self.assertEqual(result, 'exit game')

    def test_lobby1(self):
        result = rpg.lobby('random')
        self.assertEqual(result, 'wrong input')



    def test_shop(self):
        result = rpg.shop('1')
        self.assertEqual(result, 'success')

    def test_shop2(self):
        result = rpg.shop('2')
        self.assertEqual(result, 'success')

    def test_shop3(self):
        result = rpg.shop('1')
        self.assertEqual(result, 'failed')

    def test_shop4(self):
        result = rpg.shop('2')
        self.assertEqual(result, 'failed')





if __name__ == "__main__":
    unittest.main()
