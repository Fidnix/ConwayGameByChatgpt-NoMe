import pygame
import numpy as np
import time

def init_board(width, height):
    board = np.zeros((height, width))
    margen = 100
    for i in range(height):
        for j in range(width):

            # if np.random.randint(0, 2) == 0:
            #     board[i][j] = 1
            # else:
            #     board[i][j] = 0
            if((i>300 - margen//2) & (i<300 + margen//2)):
                board[i][j] = 1
                continue

    return board

def update_board(board):
    new_board = np.copy(board)
    height, width = board.shape
    for i in range(height):
        for j in range(width):
            num_neighbors = (
                board[(i - 1) % height][(j - 1) % width]
                + board[(i - 1) % height][j]
                + board[(i - 1) % height][(j + 1) % width]
                + board[i][(j - 1) % width]
                + board[i][(j + 1) % width]
                + board[(i + 1) % height][(j - 1) % width]
                + board[(i + 1) % height][j]
                + board[(i + 1) % height][(j + 1) % width]
            )
            if board[i][j] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                new_board[i][j] = 0
            elif board[i][j] == 0 and num_neighbors == 3:
                new_board[i][j] = 1
    return new_board

def draw_board(screen, board):
    height, width = board.shape
    for i in range(height):
        for j in range(width):
            if board[i][j] == 1:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, color, rect)

def main():
    width, height = 800, 600
    global cell_size
    cell_size = 7
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Conway's Game of Life")
    board = init_board(width // cell_size, height // cell_size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        draw_board(screen, board)
        board = update_board(board)
        pygame.display.flip()
        time.sleep(0.1)
    pygame.quit()

if __name__ == '__main__':
    main()
