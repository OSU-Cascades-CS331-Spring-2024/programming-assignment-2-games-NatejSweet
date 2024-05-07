'''
    Defines Player class, and subclasses Human and Minimax Player.
'''

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'

    def get_move(self, board):
        col,row,val = self.minimax(board, 5, self.symbol)
        print("Minimax value: ", val)
        print("Move: ", col, row)
        return col,row
    
#Source: https://en.wikipedia.org/wiki/Minimax
    def minimax(self, board, depth, symbol):
        if depth==0 or not board.has_legal_moves_remaining(symbol):
            return -1,-1, board.count_score(symbol)

        best_move = (None, None)
        if symbol == self.symbol: #maximizing player
            value = float('-inf')
            for col in range(board.get_num_cols()):
                for row in range(board.get_num_rows()):
                    if board.is_legal_move(col, row, symbol):
                        tmpBoard = board.clone_of_board()
                        tmpBoard.play_move(col, row, symbol)
                        _, _, temp_value = self.minimax(tmpBoard, depth - 1, self.oppSym)
                        if temp_value > value:
                            value = temp_value
                            best_move = (col, row)
        else: #minimizing player
            value = float('inf')
            for col in range(board.get_num_cols()):
                for row in range(board.get_num_rows()):
                    if board.is_legal_move(col, row, symbol):
                        tmpBoard = board.clone_of_board()
                        tmpBoard.play_move(col, row, symbol)
                        _, _, temp_value = self.minimax(tmpBoard, depth - 1, self.symbol)
                        if temp_value < value:
                            value = temp_value
                            best_move = (col, row)
        
        return best_move[0], best_move[1], value