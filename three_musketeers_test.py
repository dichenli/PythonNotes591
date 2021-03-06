import unittest
from three_musketeers import *
left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'
class TestThreeMusketeers(unittest.TestCase):
def setUp(self):
set_board([ [_, _, _, M, _],
[_, _, R, M, _],
[_, R, M, R, _],
[_, R, _, _, _],
[_, _, _, R, _] ])
def test_create_board(self):
create_board()
self.assertEqual(at((0, 0)), 'R')
self.assertEqual(at((0, 4)), 'M')
def test_set_board(self):
self.assertEqual(at((0, 0)), '-')
self.assertEqual(at((1, 2)), 'R')
self.assertEqual(at((1, 3)), 'M')
def test_get_board(self):
self.assertEqual([ [_, _, _, M, _],
[_, _, R, M, _],
[_, R, M, R, _],
[_, R, _, _, _],
[_, _, _, R, _] ],
get_board())
def test_string_to_location(self):
self.fail() # Replace with tests
def test_location_to_string(self):
self.fail() # Replace with tests
def test_at(self):
self.fail() # Replace with tests
def test_all_locations(self):
self.fail() # Replace with tests
def test_adjacent_location(self):
self.fail() # Replace with tests
def test_is_legal_move_by_musketeer(self):
self.fail() # Replace with tests
def test_is_legal_move_by_enemy(self):
self.fail() # Replace with tests
def test_is_legal_move(self):
self.fail() # Replace with tests
def test_can_move_piece_at(self):
self.fail() # Replace with tests
def test_has_some_legal_move_somewhere(self):
set_board([ [_, _, _, M, _],
[_, R, _, M, _],
[_, _, M, _, R],
[_, R, _, _, _],
[_, _, _, R, _] ] )
self.assertFalse(has_some_legal_move_somewhere('M'))
self.assertTrue(has_some_legal_move_somewhere('R'))
self.fail() # Put additional tests here
def test_possible_moves_from(self):
self.fail() # Replace with tests
def test_can_move_piece_at(self):
set_board([ [_, _, _, M, R],
[_, _, _, M, M],
[_, _, R, _, _],
[_, _, _, _, _],
[_, _, _, _, _] ] )
self.fail() # Replace with tests
def test_is_legal_location(self):
self.fail() # Replace with tests
def test_is_within_board(self):
self.fail() # Replace with tests
def test_all_possible_moves_for(self):
set_board([ [_, _, R, M, R],
[_, _, _, M, M],
[_, _, _, _, _],
[_, _, _, _, _],
[_, _, _, _, _] ] )
self.fail() # Replace with tests
def test_make_move(self):
self.fail() # Replace with tests
def test_choose_computer_move(self):
self.fail() # Replace with tests; should work for both 'M' and 'R'
def test_is_enemy_win(self):
self.fail() # Replace with tests
unittest.main()
