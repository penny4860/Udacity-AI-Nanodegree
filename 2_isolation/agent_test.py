"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload



class MiniMaxTest(unittest.TestCase):
    """Unit tests for isolation agents"""
 
    def setUp(self):
        import sample_players
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = sample_players.RandomPlayer()
        self.game = isolation.Board(self.player1, self.player2)
 
    def test_minimax_interface(self):
         
        # minimax player first turn
        self.player1.time_left = lambda : 10000
        move_pos = self.player1.minimax(self.game, depth=1)
        self.game.apply_move(move_pos)
        print(self.game.print_board())
 
        self.game.apply_move((3,3))
        print(self.game.print_board())
 
        # minimax player second turn
        move_pos = self.player1.minimax(self.game, depth=1)
        self.game.apply_move(move_pos)
        print(self.game.print_board())


class AlphaBetaTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        import sample_players
        reload(game_agent)
        self.player1 = game_agent.AlphaBetaPlayer()
        self.player1.time_left = lambda : 10000
        self.player2 = sample_players.RandomPlayer()
        self.game = isolation.Board(self.player1, self.player2)

    def test_interface(self):
        
        move_pos = self.player1.alphabeta(self.game, 1)
        self.game.apply_move(move_pos)
        print(self.game.print_board())

        self.game.apply_move((3,3))
        print(self.game.print_board())
 
        # alphabeta player second turn
        move_pos = self.player1.alphabeta(self.game, depth=1)
        self.game.apply_move(move_pos)
        print(self.game.print_board())


if __name__ == '__main__':
    unittest.main()
