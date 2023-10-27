import sys

import pygame
from pygame import *

import AI

current_scene = 'welcome'
first_click_in_game_scene = True
button_was_clicked = False
# Initialize pygame
pygame.init()
max_turn = False
WHITE = (255 ,255 ,255)
BLACK = (0 ,0 ,0)
BLUE = (0 ,0 ,255)
GREEN = (0 ,255 ,0)

human_marker ,ai_marker = 'X' ,'O'
WIDTH ,HEIGHT = 700 ,700
ROWS ,COLS = 3 ,3
CELL_WIDTH: int = WIDTH // COLS
CELL_HEIGHT: int = HEIGHT // COLS
player_1 = []
ai_moves = []
print(CELL_HEIGHT ,CELL_WIDTH)

BOARD_COLOR = (0 ,0 ,0)
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf' ,32)
board = [['' ,'' ,''] ,['' ,'' ,''] ,['' ,'' ,'']]


def button(x ,y ,w ,h ,text ,action=None ,events=None):
	global button_was_clicked
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	button_color = GREEN  # Default button color

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		button_color = BLUE
		if click[0] == 1 and action is not None:
			button_was_clicked = True
			action()
	pygame.draw.rect(screen ,button_color ,(x ,y ,w ,h))

	text_surface = font.render(text ,True ,BLACK)
	text_rect = text_surface.get_rect()
	text_rect.center = ((x + w // 2) ,(y + h // 2))
	screen.blit(text_surface ,text_rect)


def reset_button_state():
	global button_was_clicked
	button_was_clicked = False


def clear():
	screen.fill((0 ,0 ,0))
	pygame.display.flip()


def determine_winner(turn):
	# horizontals
	# verticals
	# diagonals
	print("Check")
	win_state = [
		[(0 ,0) ,(0 ,1) ,(0 ,2)] ,
		[(1 ,0) ,(1 ,1) ,(1 ,2)] ,
		[(2 ,0) ,(2 ,1) ,(2 ,2)] ,
		[(0 ,0) ,(1 ,0) ,(2 ,0)] ,
		[(0 ,1) ,(1 ,1) ,(2 ,1)] ,
		[(0 ,2) ,(1 ,2) ,(2 ,2)] ,
		[(0 ,0) ,(1 ,1) ,(2 ,2)] ,
		[(2 ,0) ,(1 ,1) ,(0 ,2)]
	]

	if turn:
		for state in win_state:
			if all(element in ai_moves for element in state):
				return True
				break

	else:
		for state in win_state:
			if all(element in player_1 for element in state):
				return True
				break


def clear():
	screen.fill(WHITE)
	pygame.display.update()


def check_moves_left(board):
	for i in range(3):
		for j in range(3):
			if board[i][j] == '':
				return True
	return False


def draw_grid():
	for row in range(ROWS):
		for col in range(COLS):
			pygame.draw.rect(screen ,BOARD_COLOR ,
			                 (col * CELL_WIDTH ,row * CELL_HEIGHT ,
			                  CELL_WIDTH ,CELL_HEIGHT) ,1)


def evaluate(board):
	for row in range(3):
		if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
			if board[row][0] == human_marker:
				return 10
			elif board[row][0] == ai_marker:
				return -10
	for col in range(3):
		if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
			if board[0][col] == human_marker:
				return 10
			elif board[0][col] == ai_marker:
				return -10

	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		if board[0][0] == human_marker:
			return 10
		elif board[0][0] == ai_marker:
			return -10

	if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		if board[0][2] == human_marker:
			return 10
		elif board[0][2] == ai_marker:
			return -10
	return 0


def draw_circles(player_positions ,color):
	for row ,col in player_positions:  # Renamed for clarity
		circle_x = col * CELL_WIDTH + CELL_WIDTH // 2  # col is x-coordinate
		circle_y = row * CELL_HEIGHT + CELL_HEIGHT // 2  # row is y-coordinate
		pygame.draw.circle(screen ,color ,(circle_x ,circle_y) ,20)


def find_best_move(board):
	bestVal = float('-inf')
	bestMove = (-1 ,-1)

	for i in range(3):
		for j in range(3):
			if board[i][j] == '':
				board[i][j] = ai_marker
				moveVal = minimax(board ,0 ,False)
				board[i][j] = ''

				if moveVal > bestVal:
					bestMove = (i ,j)
					bestVal = moveVal

	return bestMove

def minimax(board ,depth ,maximizing):
	if evaluate(board) == 10:
		return -10 + depth
	if evaluate(board) == -10:
		return 10 - depth

	if not check_moves_left(board):
		return 0

	if maximizing:
		maxEval = float('-inf')
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					board[i][j] = ai_marker
					eval = minimax(board ,depth + 1 ,False)
					board[i][j] = ''
					maxEval = max(maxEval ,eval)
		return maxEval

	else:
		minEval = float('inf')
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					board[i][j] = human_marker
					eval = minimax(board ,depth + 1 ,True)
					board[i][j] = ''
					minEval = min(minEval ,eval)
		return minEval


def ret_pos(x_pos ,y_pos):
	for row in range(ROWS):
		for col in range(COLS):
			if (col * CELL_WIDTH <= x_pos < (col + 1) * CELL_WIDTH) and (
				 row * CELL_HEIGHT <= y_pos < (row + 1) * CELL_HEIGHT):
				print(f"Mouse over cell {row ,col}")
				return row ,col


max_turn = False

"""
PYGAME STATES 
welcome_screen()
quit()
game_scene()

"""


def welcome_screen(events):
	global current_scene ,button_was_clicked ,first_click_in_game_scene
	screen.fill(WHITE)
	text = font.render('Tic-Tac-Toe AI' ,True ,GREEN ,BLUE)
	textRect = text.get_rect()
	textRect.center = (700 // 2 ,700 // 2)

	button(200 ,500 ,300 ,50 ,"Click me" ,lambda: game_scene(events) ,events)
	button(200 ,600 ,300 ,50 ,"Quit" ,lambda: quit_game() ,events)
	if button_was_clicked:
		current_scene = 'game'
		first_click_in_game_scene = True
		pygame.event.clear()

	screen.blit(text ,textRect)


"""
Creating quit button
"""


def quit_game():
	print("I was clicked")
	sys.exit()


def show_winner(winner: bool):
	text = font.render("HUMAN wins" ,True ,"GREEN" ,"BLUE") if winner else font.render("AI wins" ,True ,"GREEN" ,"BLUE")
	text_rect = text.get_rect()
	text_rect.center = (700 // 2 ,700 // 2)
	screen.blit(text ,text_rect)

	button(WIDTH//2,600,200,200, "Quit", lambda: quit_game(), events)


def game_scene(events):
	global max_turn ,first_click_in_game_scene
	screen.fill(WHITE)
	for event in events:
		if event.type == MOUSEBUTTONDOWN:
			if first_click_in_game_scene:
				first_click_in_game_scene = False
				continue
			x ,y = pygame.mouse.get_pos()
			x_pos ,y_pos = ret_pos(x ,y)
			print(f"These are the positions {x_pos}, {y_pos} ")
			if not max_turn and board[x_pos][y_pos] == '':
				board[x_pos][y_pos] = 'X'
				player_1.append((x_pos ,y_pos))
				max_turn = True
		if max_turn:
			max_choice = find_best_move(board)
			x ,y = max_choice
			if max_choice and board[x][y] == '':
				ai_moves.append((x ,y))
				board[x][y] = 'O'
				max_turn = False
				print(board ,ai_moves)

	AI.draw_grid(ROWS ,COLS ,screen ,BOARD_COLOR ,CELL_WIDTH ,CELL_HEIGHT)

	draw_circles(player_1 ,(0 ,0 ,0))
	draw_circles(ai_moves ,(255 ,0 ,0))
	print(max_turn)
	res = determine_winner(max_turn)
	print(board)
	if res is not None:
		screen.fill(WHITE)
		show_winner(res)
		pygame.display.flip()

	pygame.display.update()


screen = pygame.display.set_mode((WIDTH ,HEIGHT))
running = True
current_scene = 'welcome'
"""
Maximizer = AI

"""

while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	if current_scene == 'welcome':
		welcome_screen(events)
	elif current_scene == 'game':
		game_scene(events)

	pygame.display.update()
	clock.tick(60)
