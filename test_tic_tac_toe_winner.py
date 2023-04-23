
from  tic_tac_toe import tic_tac_toe_winner

def test_import_tic_tac_toe_winner():
    try:
        from tic_tac_toe.tic_tac_toe import tic_tac_toe_winner
        assert callable(tic_tac_toe_winner), "tic_tac_toe not callable"
    except ImportError as error: 
        assert False, error

def test_empty_board():
    assert tic_tac_toe_winner(' ' * 9) is None

def test_3x_in_a_row():
    winner = tic_tac_toe_winner('XXX O O  ')
    assert winner == 'X', f"expected X, got {winner}"

def test_illegal_board_symbols():
    try:
        tic_tac_toe_winner('Ala ma kota')
        assert False, "ValueError expected"
    except ValueError:
        pass

def test_illegal_board_size():
    try:
        tic_tac_toe_winner('XXX')
        assert False, "ValueError expected"
    except ValueError:
        pass

if __name__ == '__main__':
    for test in (
        test_import_tic_tac_toe_winner, test_empty_board, test_3x_in_a_row, test_illegal_board_symbols, test_illegal_board_size):  #➜ 4
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)
            print('NOK')