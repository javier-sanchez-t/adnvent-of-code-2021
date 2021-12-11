import copy

def read_random_numbers(fileName):
    file = open(fileName)
    numbers = []

    for line in file:
        numbers += line.split(',')

    file.close();
    return numbers;


def read_boards(fileName):
    file = open(fileName)
    boards = []
    board = []
    
    for line in file:
        numbers = line.replace('\n', '')
        numbers = numbers.replace('  ', ' ')
        numbers = numbers.strip()
        if len(numbers)>=1:
            board.append(numbers.split(' '))
        else: 
            bingo_board = {
                'board': board,
                'winner': False,
                'random_number': 0
            }
            boards.append(bingo_board)
            board = []

    file.close();
    return boards;


def get_sum(board):
    sum_unmarked = 0
    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            if(''.join(board[row_index][col_index]).count('x')==0):
                sum_unmarked+=int(board[row_index][col_index])
    return sum_unmarked;


def get_winner_boards(boards, random_numbers):
    winner_boards = []

    for random_number in random_numbers:

        for bingo_board in boards:
            board = bingo_board['board']

            if(bingo_board['winner'] == False):
                for row_index in range(len(board)):
                    col_x_counter = 0
                    for col_index in range(len(board[row_index])):
                        
                        # Mark number with X
                        if(str(board[row_index][col_index])==str(random_number)):
                            board[row_index][col_index] += 'x'

                        if(''.join(board[col_index][row_index]).count('x')==1):
                            col_x_counter += 1

                    if(''.join(board[row_index]).count('x')==5 or col_x_counter==5):
                        bingo_board['winner'] = True
                        bingo_board['board'] = copy.deepcopy(board)
                        bingo_board['random_number'] = random_number
                        winner_boards.append(bingo_board)

    return winner_boards;


def display_winner_result(winner):
    for row in winner['board']:
        print (row)
    winnerSum = get_sum(winner['board'])
    winnerResult = int(winner['random_number'])*winnerSum
    print('Random number: '+winner['random_number'])
    print('Sum: '+str(winnerSum))
    print('Result: '+str(winnerResult))


def get_bingo_winner():
    boards = read_boards('boards.txt')
    random_numbers = read_random_numbers('random_numbers.txt')
    winner_boards = get_winner_boards(boards, random_numbers)
    # puzzle1
    # display_winner_result(winner_boards[0])
    # puzzle2
    display_winner_result(winner_boards[len(winner_boards)-1])


get_bingo_winner()