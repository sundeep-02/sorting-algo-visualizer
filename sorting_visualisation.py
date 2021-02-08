import pygame
from pygame.locals import *
from pygame import Color
import random
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

HEIGHT = 700
WIDTH = 1040
NO_OF_BARS = 100
TIME_DELAY = 10
RECT_WIDTH = (WIDTH - 40) // NO_OF_BARS
BASE = HEIGHT - 20

arr = random.sample(range(20, 450), NO_OF_BARS)

pygame.init()
pygame.display.set_caption("Sorting Algorithm Visualisation")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def introScreen():
    font_ = pygame.font.SysFont('Candara', 80)
    text_ = font_.render("Sorting Algorithms Visualisation", True, Color('cyan')) 
    textRect_ = text_.get_rect()
    textRect_.center = ((WIDTH//2), (HEIGHT//2))
    screen.fill((30, 30, 40))
    screen.blit(text_, textRect_)
    pygame.display.update()
    pygame.time.delay(2000)

def isQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

def drawBars(arr, pos1, pos2):
    screen.fill((30, 30, 40))
    for i in range(len(arr)):
        RECT_HEIGHT = arr[i]
        if pos1 == i:
            pygame.draw.rect(screen, Color('violet'), (i*RECT_WIDTH + 20 , BASE, RECT_WIDTH - 1, -RECT_HEIGHT))
        elif pos2 == i:
            pygame.draw.rect(screen, Color('orange'), (i*RECT_WIDTH + 20 , BASE, RECT_WIDTH - 1, -RECT_HEIGHT))
        else:
            pygame.draw.rect(screen, Color('lightblue'), (i*RECT_WIDTH + 20 , BASE, RECT_WIDTH - 1, -RECT_HEIGHT))
            
def clickButton(info, x, y, width, height, val, font_size, lightcolor, darkcolor):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x < mouse[0] < x + width) and (y < mouse[1] < y + height):
        pygame.draw.rect(screen, darkcolor, (x, y, width, height))
        if click[0]:
            return 1
    else:
        pygame.draw.rect(screen, lightcolor, (x, y, width, height))
        
    font = pygame.font.SysFont('Calibri', font_size)
    text = font.render(info, True, Color('black')) 
    textRect = text.get_rect()
    textRect.center = ((x + width//2), (y + height//2))
    screen.blit(text, textRect)
    if val == 1:    pygame.display.update()
    
def bubbleSort(arr): 
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            drawBars(arr, j, j+1)
            if clickButton("Stop", WIDTH-70, 10, 60, 30, 0, 20, (250, 100, 100), (150, 100, 100)):
                return 0
            pygame.display.update()
            pygame.time.delay(TIME_DELAY)

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            if isQuit():    pygame.quit()
            
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            drawBars(arr, min, j)
            if clickButton("Stop", WIDTH-70, 10, 60, 30, 0, 20, (250, 100, 100), (150, 100, 100)):
                return 0
            pygame.display.update()
            pygame.time.delay(TIME_DELAY)
            if isQuit():    pygame.quit()
            
            if arr[min] > arr[j]:
                min = j
    
        arr[i], arr[min] = arr[min], arr[i]

def insertionSort(arr):  
    for i in range(1, len(arr)):  
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            drawBars(arr, j, j+1)
            if clickButton("Stop", WIDTH-70, 10, 60, 30, 0, 20, (250, 100, 100), (150, 100, 100)):
                return 0
            pygame.display.update()
            pygame.time.delay(TIME_DELAY)
            if isQuit():    pygame.quit()

            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 

def shellSort(arr): 
    n = len(arr) 
    gap = n//2
  
    while gap > 0: 
        for i in range(gap,n): 
            temp = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] > temp:
                drawBars(arr, j, i)
                if clickButton("Stop", WIDTH-70, 10, 60, 30, 0, 20, (250, 100, 100), (150, 100, 100)):
                    return 0
                pygame.display.update()
                pygame.time.delay(TIME_DELAY)
                if isQuit():    pygame.quit()

                arr[j] = arr[j-gap] 
                j -= gap 
  
            arr[j] = temp 
        gap = gap // 2

run = True
intro = True
while run:
    if intro == True:
        introScreen()
        intro = False

    if isQuit():    run = False
    execute = 0

    if clickButton("Shuffle", 45, 50, 150, 40, 0, 30, (250, 150, 150), (150, 100, 100)):
        execute = 0
        arr = random.sample(range(20, 400), NO_OF_BARS)

    if clickButton("Bubble", 245, 50, 150, 40, 0, 30, (150, 150, 250), (100, 100, 150)):
        execute = 1

    if clickButton("Selection", 445, 50, 150, 40, 0, 30, (150, 250, 150), (100, 150, 100)):
        execute = 2

    if clickButton("Insertion", 645, 50, 150, 40, 0, 30, (250, 250, 150), (150, 150, 100)):
        execute = 3

    if clickButton("Shell", 845, 50, 150, 40, 1, 30, (250, 150, 250), (150, 100, 150)):
        execute = 4

    if execute == 0:    
        drawBars(arr, 999, 999)

    elif execute == 1:    
        execute = bubbleSort(arr)
    
    elif execute == 2:   
        execute = selectionSort(arr)

    elif execute == 3:   
        execute = insertionSort(arr)

    elif execute == 4:   
        execute = shellSort(arr)

pygame.quit()