# ConnectFour
# CZK, CMS430 

human_moves_first = True

if human_moves_first:
    computer_symbol = 'O'
    human_symbol = 'X'
    turn_index = 0
else:
    computer_symbol = 'X'
    human_symbol = 'O'
    turn_index = 1

def wins(board, player):
    
    """ Return True if play has four in a row """
    
    # Row wins
    for num_row in range(6):
        for num_col in range(4):
            if(board[7 * num_row + num_col] == player and 
            board[7 * num_row + num_col + 1] == player and
            board[7 * num_row + num_col + 2] == player and
            board[7 * num_row + num_col + 3] == player):
                return True
                
    # Column wins
    for num_col in range(7):
        for num_row in range(3):
            if(board[7 * num_row + num_col] == player 
            and board[7 * num_row + num_col + 7] == player
            and board[7 * num_row + num_col + 14] == player 
            and board[7 * num_row + num_col + 21] == player): 
                return True
                
    # Diagonal wins
    # Diagonal going right
    for i in range(21, 39):
        if(board[i] == player and board[i-6] == player
        and board[i-12] == player and board[i-18] == player):
            return True
    # Diagonal going left
    for i in range(24, 42):
        if(board[i] == player and board[i-8] == player
        and board[i-16] == player and board[i-24] == player):
            return True
    
    return False

def score(board):
    
    if wins(board, computer_symbol):
        return 1
    elif wins(board, human_symbol):
        return -1
    else:
        return 0


def minimax(board, depth, alpha, beta, is_max_player):
    
    """ Executes minimax algorithm with alpha-beta pruning to find best outcome 
        for each player. Works recursively based on set depth. 
        
        Returns: best score and best move"""  
    
    current_score = score(board)
    if current_score != 0 or depth == 0:
        return current_score, None
    
    if is_max_player:
        best_value = -2 ** 40
        best_move = None
        
        for move in range(7):
            if board[move] != None:
                continue
            
            move = comp_move(board, move)
            
            board[move] = computer_symbol
            value, response = minimax(board, depth - 1, alpha, beta, False)
            board[move] = None
            
            alpha = max(alpha, value)
            
            if value > best_value:
                best_value = value
                best_move = move
            
            if beta <= alpha:
                break
            

    if not is_max_player:
        best_value = 2 ** 40
        best_move = None
        
        for move in range(7):
            if board[move] != None:
                continue
            
            move = comp_move(board, move)
            
            board[move] = human_symbol
            value, response = minimax(board, depth - 1, alpha, beta, True)
            board[move] = None
            
            beta = min(beta, value)
            
            if value < best_value:
                best_value = value
                best_move = move
                        
            if beta<= alpha:
                break

    return best_value, best_move
    
def display(board): 
    print ''
    
    for i in range(7):
        print '', i, '',
        
    print ''
    
    for i in range(42):
        if board[i] is None:
            print '', '.', '',
        else:
            print '', board[i], '',
    
        if (i == 6 or i == 13 or i == 20
        or i == 27 or i == 34 or i == 41):
            print ''
   
    print ''

def comp_move(board, move):
    
    move_below = move + 7
    
    if(board[move+35] is None):
        move = move + 35
    else:
        while(board[move_below] is None):
            move = move_below
            move_below = move_below + 7
            
    return move
    
def get_move(board):
    looping = True;
    
    while looping:
        looping = False
        
        print 'Choose a column 0-6', 
        move = int(raw_input())
        
        if(move < 0 or move > 6):
            print 'Choose a different position.'
            print ''
            looping = True
            continue
            
        move_below = move + 7
        
        if( board[move+35] is None ):
            move = move + 35
        else:
            while(board[move_below] is None):
                move = move_below
                move_below = move_below + 7

        if board[move] != None:
            print 'Column is full'
            looping = True
            
    return move

def play():
    board = {}
    
    # Create a board dictionary with 42 spaces set to None
    for i in range(42):
        board[i] = None
    
    display(board)
    
    turn = 0
    
    while turn < 42:
        
        if turn % 2 == turn_index:
            move = get_move(board)
            board[move] = human_symbol
        
        else:
            best_value, best_move = minimax(board, 5, -240, 240, True)
            board[best_move] = computer_symbol
        
        display(board)
        
        if wins(board, human_symbol):
            print 'You win! I am so proud.'
            turn = 42
        elif wins(board, computer_symbol):
            print 'You lose. Sorry not sorry.'
            turn = 42
        
        turn += 1
    
    if turn == 42:
        print 'It seems we are at an impasse.'
     
if __name__ == '__main__':
    play()
