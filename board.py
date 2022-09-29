import pygame

class Board:
    def __init__(self, window, windowDimensions, cellDimension):
        # Draw board
        self.window = window
        self.dimensions = windowDimensions
        self.cellDimension = cellDimension
        self.cells = {}
        self.expireDate = 0

        for y in range(0, self.dimensions[1], self.cellDimension):
            for x in range(0, self.dimensions[0], self.cellDimension):
                self.cells[(x, y)] = Cell((x, y))

    def draw(self):
        self.drawCells()
    #     self.drawBorder()

    # def drawBorder(self):
    #     for y in range(0, self.dimensions[1], self.cellDimension):
    #         for x in range(0, self.dimensions[0], self.cellDimension):
    #             cell = pygame.Rect((x, y, self.cellDimension, self.cellDimension))
    #             pygame.draw.rect(self.window, (0, 0, 0), cell, 1)
    
    def drawCells(self):
        for cell in self.cells.values():
            rect = pygame.Rect((cell.pos[0], cell.pos[1], self.cellDimension, self.cellDimension))
            if cell.state == 0:
                colour = (30, 30, 30)
            elif cell.state == 1:
                colour = (255, 0, 0)
            elif cell.state == 2:
                colour = (0, 0, 255)
            
            if cell.state > 0:
                pygame.draw.rect(self.window, colour, rect)
                border = pygame.Rect((cell.pos[0], cell.pos[1], self.cellDimension, self.cellDimension))
                pygame.draw.rect(self.window, (0, 0, 0), border, 1)
    
    def changeCell(self, cellPos, newState):
        self.cells[cellPos].state = newState
    
    def checkCollision(self, player):
        if player.pos[0] <= 0:
            player.pos = (self.dimensions[0]-self.cellDimension, player.pos[1])
            return False
        elif player.pos[0] >= self.dimensions[0]:
            player.pos = (0, player.pos[1])
            return False
        if player.pos[1] <= 0:
            player.pos = (player.pos[0], self.dimensions[1]-self.cellDimension)
            return False
        elif player.pos[1] >= self.dimensions[1]:
            player.pos = (player.pos[0], 0)
            return False

        cell = self.cells[player.pos]
        if cell.state >= 1:
            return True
        
    
    def expire(self):
        for cell in self.cells.values():
            if cell.state > 0:
                cell.expiry -= 1
                if cell.expiry <= self.expireDate:
                    self.cells[cell.pos] = Cell(cell.pos)
                    self.expireDate -= 0.5

class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.state = 0
        self.expiry = 100


class Player:
    def __init__(self, board, startPos, player):
        self.pos = startPos
        self.board = board
        self.player = player
        self.dir = "RIGHT"
    
    def move(self):
        self.board.changeCell(self.pos, self.player)
        if self.dir == "RIGHT":
            self.pos = (self.pos[0]+self.board.cellDimension, self.pos[1])
        elif self.dir == "LEFT":
            self.pos = (self.pos[0]-self.board.cellDimension, self.pos[1])
        elif self.dir == "UP":
            self.pos = (self.pos[0], self.pos[1]-self.board.cellDimension)
        elif self.dir == "DOWN":
            self.pos = (self.pos[0], self.pos[1]+self.board.cellDimension)