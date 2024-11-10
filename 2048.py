import os
from random import randint

import pygame as pg

WIDTH, HEIGHT = 1792 // 2, 1280 // 2
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
ROWS = 4
COLLS = 4
CELL_SIZE = int(round(HEIGHT * 20 / 100, 0))

OFFSET_X = int(HEIGHT * 10 / 100)
OFFSET_Y = int(HEIGHT * 10 / 100)
SPACING = int(round((CELL_SIZE * 8 / 100), 0))
ROUNDING = 15  # in percentage


x = OFFSET_X + CELL_SIZE * COLLS + 2 * SPACING
y = OFFSET_Y
max_score_rect = [
    x,
    y,
    WIDTH - 2 * SPACING - (OFFSET_X + CELL_SIZE * COLLS + 2 * SPACING),
    CELL_SIZE - SPACING,
]

score_rect = [
    x,
    y + CELL_SIZE,
    WIDTH - 2 * SPACING - (OFFSET_X + CELL_SIZE * COLLS + 2 * SPACING),
    CELL_SIZE - SPACING,
]


BOARD = [[0 for x in range(COLLS)] for y in range(ROWS)]

CELLS_RECT = []

pg.font.init()
pg.init()
FONT = pg.font.Font("Roboto-Black.ttf", 40)
pg.display.set_caption("2048")


def init_cells_rect():
    cells_rect = []
    for i in range(ROWS):
        row = []
        for j in range(COLLS):
            row.append(
                [
                    i * CELL_SIZE + OFFSET_X,
                    j * CELL_SIZE + OFFSET_Y,
                    CELL_SIZE - SPACING,
                    CELL_SIZE - SPACING,
                ]
            )
        cells_rect.append(row)

    return cells_rect


def draw_board(borad, cells_rect):
    WINDOW.fill("#faf8f0")
    CELL_SIZE = int(round(HEIGHT * 20 / 100, 0))

    # Background rect
    pg.draw.rect(
        WINDOW,
        "#9b8b7d",
        [
            OFFSET_X - SPACING,
            OFFSET_Y - SPACING,
            SPACING + CELL_SIZE * ROWS,
            SPACING + CELL_SIZE * COLLS,
        ],
        0,
        int(CELL_SIZE * ROUNDING / 100) + SPACING,
    )

    # Draws Board
    for i in range(ROWS):
        for j in range(COLLS):
            pg.draw.rect(
                WINDOW,
                "#bcac99",
                [
                    i * CELL_SIZE + OFFSET_X,
                    j * CELL_SIZE + OFFSET_Y,
                    CELL_SIZE - SPACING,
                    CELL_SIZE - SPACING,
                ],
                0,
                int(CELL_SIZE * ROUNDING / 100),
            )

    # Draws Cells
    for i in range(ROWS):
        for j in range(COLLS):
            if BOARD[i][j] != 0:
                color = "#ede4db"
                pg.draw.rect(
                    WINDOW,
                    color,
                    cells_rect[i][j],
                    0,
                    int(CELL_SIZE * ROUNDING / 100),
                )

                num = FONT.render(str(BOARD[i][j]), 1, "#746453")
                WINDOW.blit(num, num.get_rect(center=pg.Rect(cells_rect[i][j]).center))


def draw_scores(score, max_score):

    # max score
    pg.draw.rect(
        WINDOW,
        "#eae7da",
        max_score_rect,
        ROUNDING,
        int(CELL_SIZE * ROUNDING / 100),
    )

    # score
    pg.draw.rect(
        WINDOW,
        "#eae7da",
        score_rect,
        0,
        int(CELL_SIZE * ROUNDING / 100),
    )


def new_game():
    global BOARD
    count = 0
    while count != 2:
        row = randint(0, 3)
        col = randint(0, 3)
        if BOARD[row][col] == 0:
            BOARD[row][col] = 2
            count += 1


def main():
    running = True
    score = 0
    max_score = 0
    new_game()
    CELLS_RECT = init_cells_rect()
    while running:
        draw_board(BOARD, CELLS_RECT)
        draw_scores(score, max_score)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


if __name__ == "__main__":
    main()
