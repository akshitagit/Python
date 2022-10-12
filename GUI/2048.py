from __future__ import print_function
import tkinter as tk
import tkinter.messagebox as messagebox
import random

class Grid:
    def __init__ (self, n):
        self.size = n
        self.cells = self.generate_empty_grid()
        self.compressed = False
        self.merged = False
        self.moved = False
        self.current_score = 0

    def random_cell(self):
        cell = random.choice(self.retreive_empty_cells())
        i = cell[0]
        j = cell[1]
        self.cells[i][j] = 2 if random.random() < 0.9 else 4

    def retreive_empty_cells(self):
        empty_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] == 0:
                    empty_cells.append((i,j))
        return empty_cells

    def generate_empty_grid(self):
        return [[0] * self.size for i in range(self.size)]

    def transpose(self):
        self.cells = [list(t) for t in zip(*self.cells)]

    def reverse(self):
        for i in range(self.size):
            start = 0
            end = self.size - 1
            while start < end:
                self.cells[i][start], self.cells[i][end] = self.cells[i][end], self.cells[i][start]
                start += 1
                end -= 1

    def clear_flags(self):
        self.compressed = False
        self.merged = False
        self.moved = False

    def left_compress(self):
        self.compressed = False
        new_grid = self.generate_empty_grid()
        for i in range(self.size):
            count=0
            for j in range(self.size):
                if self.cells[i][j] != 0:
                    new_grid[i][count] = self.cells[i][j]
                    if count !=j:
                        self.compressed = True
                    count += 1
        self.cells = new_grid

    def left_merge(self):
        self.merged = False
        for i in range(self.size):
            for j in range(self.size -1):
                if self.cells[i][j] == self.cells[i][j+1] and self.cells[i][j] != 0:
                    self.cells[i][j]*= 2
                    self.cells[i][j+1] = 0
                    self.current_score += self.cells[i][j]
                    self.merged = True
        print('left merged')

    def found_2048(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][i] >= 2048:
                    return True
        return False

    def has_empty_cells(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] == 0:
                    return True
        return False

    def can_merge(self):
        for i in range(self.size):
            for j in range(self.size-1):
                if self.cells[i][j] == self.cells[i][j+1]:
                    return True
        for j in range(self.size):
            for i in range(self.size - 1):
                if self.cells[i][j] == self.cells[i+1][j]:
                    return True
        return False

    def set_cells(self, cells):
        self.cells=cells

    def print_grid(self):
        print('='*40)
        for i in range(self.size):
            for j in range(self.size):
                print('%d\t', self.cells[i][j], end='')
            print()
        print('='*40)

class GamePanel:
    '''The GUI view class of the 2048 game show''' 
    CELL_PADDING= 10
    BACKGROUND_COLOR = '#92877d'
    EMPTY_CELL_COLOR='#9e948a'
    CELL_BACKGROUND_COLOR_DICT = {
        '2': '#eee4da', 
        '4': '#ede0c8',
        '8': '#f2b179',
        '16': '#f59563',
        '32': '#f67c5f',
        '64': '#f65a3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#edc850',
        '1024': '#edc53f', 
        '2048': '#edc22e',
        'beyond': '#3c3a32'}

    CELL_COLOR_DICT = {
        '2': '#776e65',
        '4': '#776e65',
        '8':'#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
        'beyond': '#19f6f2'}

    FONT=('COMIC SANS', 18, 'bold')
    UP_KEYS = ('Up')
    DOWN_KEYS = ('Down')
    LEFT_KEYS = ('Left')
    RIGHT_KEYS = ('Right')

    def __init__(self, grid):
        self.grid = grid
        self.root = tk.Tk()
        self.root.title('2048')
        self.background = tk.Frame(self.root, bg= GamePanel.BACKGROUND_COLOR)
        self.cell_labels = []
        for i in range(self.grid.size):
            row_labels =[]
            for j in range(self.grid.size):
                label = tk.Label(self.background, text='',
                    bg=GamePanel.EMPTY_CELL_COLOR, justify=tk.CENTER,
                    font=GamePanel.FONT, width=4, height=2)
                label.grid(row=i, column=j, padx=10, pady=10)
                row_labels.append(label)
            self.cell_labels.append(row_labels)
        self.background.grid()

    def paint(self):
        for i in range(self.grid.size):
            for j in range(self.grid.size):
                if self.grid.cells[i][j]== 0:
                    self.cell_labels[i][j].configure(text='', bg=GamePanel.EMPTY_CELL_COLOR)
                else:
                    cell_text = str(self.grid.cells[i][j])
                    if self.grid.cells[i][j]>2048:
                        bg_color=GamePanel.CELL_BACKGROUND_COLOR_DICT.get("beyond")
                        fg_color=GamePanel.CELL_COLOR_DICT.get("beyond")
                    else:
                        bg_color = GamePanel.CELL_BACKGROUND_COLOR_DICT.get(cell_text)
                        fg_color = GamePanel.CELL_COLOR_DICT.get(cell_text)
                    self.cell_labels[i][j].configure(text=cell_text,
                                            bg=bg_color, fg=fg_color)

class Game:
    '''The main Game class which is the controller of the whole game.'''
    def __init__ (self, grid, panel):
        self.grid = grid
        self.panel=panel
        self.start_cells_num=2
        self.over=False
        self.won = False
        self.keep_playing=False
    
    def is_game_terminated(self):
        return self.over or (self.won and (not self.keep_playing))

    def start(self):
        self.add_start_cells()
        self.panel.paint()
        self.panel.root.bind('<Key>', self.key_handler)
        self.panel.root.mainloop()

    def add_start_cells(self):
        for i in range(self.start_cells_num):
            self.grid.random_cell()

    def can_move(self):
       return self.grid.has_empty_cells() or self.grid.can_merge()

    def key_handler(self, event):
        if self.is_game_terminated():
            return

        self.grid.clear_flags()
        key_value = event.keysym

        print('{} key pressed'.format(key_value))
        if key_value in GamePanel.UP_KEYS:
            self.up()
            #self.grid.print_grid
        elif key_value in GamePanel.LEFT_KEYS:
            self.left()
            #self.grid print_grid
        elif key_value in GamePanel.DOWN_KEYS:
            self.down()
            #self.grid.print_grid()
        elif key_value in GamePanel.RIGHT_KEYS:
            self.right()
            #self.grid.print_grid()
        else:
            pass

        self.panel.paint()
        print('Score: {}'.format(self.grid.current_score))
        if self.grid.found_2048():
            self.you_win()
            if not self.keep_playing:
                return

        if self.grid.moved:
            self.grid.random_cell()

        self.panel.paint()
        if not self.can_move():
            self.over = True
            self.game_over()

    def you_win(self):
        if not self.won:
            self.won = True 
            print('You Win!')
            if messagebox.askyesno('2048', 'You Win!\n'
                            'Are you going to continue the 2048 game?'):
                self.keep_playing = True

    def game_over(self): 
        print('Game Over!')
        messagebox.showinfo('2048', 'Oops!\n'
                        'Game Over!')

    def up(self):
        self.grid.transpose()
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()
        self.grid.transpose()

    def left(self):
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()

    def down(self):
        self.grid.transpose()
        self.grid.reverse()
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid .moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()
        self.grid.reverse()
        self.grid.transpose()

    def right(self):
        self.grid.reverse()
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()
        self.grid.reverse()

if __name__ == '__main__':
    size = 4
    grid = Grid(size)
    panel = GamePanel(grid)
    game2048 = Game(grid, panel)
    game2048.start()