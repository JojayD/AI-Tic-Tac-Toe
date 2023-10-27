import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280 ,720))
clock = pygame.time.Clock()
WHITE = (255 ,255 ,255)
running = True

white = (255 ,255 ,255)
green = (0 ,255 ,0)
blue = (0 ,0 ,128)
black = (0,0,0)

def button(x ,y ,w ,h ,text ,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen ,blue ,(x ,y ,w ,h))
		if click[0] == 1 and action is not None:
			action()
	else:
		pygame.draw.rect(screen ,green ,(x ,y ,w ,h))

	text_surface = font.render(text ,True ,black)
	text_rect = text_surface.get_rect()
	text_rect.center = ((x + w // 2) ,(y + h // 2))
	screen.blit(text_surface ,text_rect)


def button_action():
	print("I was clicked")


while running:
	screen.fill(WHITE)

	font = pygame.font.Font('freesansbold.ttf' ,32)
	text = font.render('GeeksForGeeks' ,True ,green ,blue)
	textRect = text.get_rect()
	textRect.center = (1280 // 2 ,720 // 2)

	screen.blit(text ,textRect)
	button(350 ,250 ,300 ,50 ,"Click me" ,button_action)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()
	clock.tick(60)  # limits FPS to 60

pygame.quit()
