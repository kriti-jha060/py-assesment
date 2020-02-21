matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

madrix = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}


def disp():
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end='\t')
        print()


disp()


def tic_tac_toe(madrix, n, player):
    for i in madrix:
        if n == i:
            pos = madrix[n]
            matrix[pos[0]].pop(pos[1])
            if player == 1:
                matrix[pos[0]].insert(pos[1], 'X')

            else:
                matrix[pos[0]].insert(pos[1], 'O')
    disp()


print('WELCOME TO TIC TAC TOE')


def conditions():
    for i in range(3):
        for j in range(3):
            if matrix[0][j] == matrix[1][j] == matrix[2][j] == 'X':
                print('Player 1, you have won')
                break

            elif matrix[0][j] == matrix[1][j] == matrix[2][j] == 'O':
                print('Player 2, you have won')
                break

            if i == j:
                if matrix[i][j] == 'X':
                    print('Player 1, you have won')
                    break
                elif matrix[i][j] == 'O':
                    print('Player 2, you have won')
                    break

            if matrix[2][0] == matrix[1][1] == matrix[0][2] == 'X':
                print('Player 1, you have won')
                break
            elif matrix[2][0] == matrix[1][1] == matrix[0][2] == 'O':
                print('Player 2, you have won')
                break

            else:
                continue


def game():
    count = 0
    while count < 9:
        if count % 2 == 0:
            n = int(input('Enter your position player 1: '))
            tic_tac_toe(madrix, n, 1)
            if count > 4:
                conditions()
        else:
            n = int(input('Enter your position player 2: '))
            tic_tac_toe(madrix, n, 2)
            if count > 3:
                conditions()
        count += 1
    disp()


game()
# matrix[i] == 'X' or matrix[i] == 'O' or
