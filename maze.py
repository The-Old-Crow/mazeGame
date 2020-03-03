import pygame

pygame.init()
win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Simple Maze")
wwin, hwin = pygame.display.get_surface().get_size()

green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

wall_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y, w, h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([w, h])
		self.image.fill(white)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


class Player(pygame.sprite.Sprite):

	velocity = (0,0)

	def __init__(self, x, y, w, h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([15, 15])
		self.image.fill(green)
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = 5
	
	def draw(self, wall):
		self.rect.x += (self.speed * self.velocity[0])

		wall_collisions = pygame.sprite.spritecollide(self, wall_group, False)
		for wall in wall_collisions:
			# player moving right
			if self.velocity[0] > 0:
				self.rect.right = wall.rect.left
			# player moving left
			else:
				self.rect.left = wall.rect.right
			
		self.rect.y += (self.speed * self.velocity[1])
		wall_collisions = pygame.sprite.spritecollide(self, wall_group, False)
		for wall in wall_collisions:
			# player moving down
			if self.velocity[1] > 0:
				self.rect.bottom = wall.rect.top
			# player moving up
			else:
				self.rect.top = wall.rect.bottom


player = Player(50, 50, 20, 20)
all_sprites.add(player)

left_wall = Wall(0, 0, 10, hwin)
wall_group.add(left_wall)
all_sprites.add(left_wall)

right_wall = Wall(wwin-10, 0, 10, hwin)
wall_group.add(right_wall)
all_sprites.add(right_wall)

top_wall = Wall(0, 0, wwin, 10)
wall_group.add(top_wall)
all_sprites.add(top_wall)

bottom_wall = Wall(0, hwin-10, wwin, 10)
wall_group.add(bottom_wall)
all_sprites.add(bottom_wall)

middle_wall = Wall(((wwin//2)-10), 0, 10, (hwin//2))
wall_group.add(middle_wall)
all_sprites.add(middle_wall)

running = True
while running:
	clock.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_ESCAPE]:
		running = False
	if keys[pygame.K_UP]:
		player.velocity = (0, -1)
		
	if keys[pygame.K_DOWN]:
		player.velocity = (0, 1)
		
	if keys[pygame.K_LEFT]:
		player.velocity = (-1, 0)
		
	if keys[pygame.K_RIGHT]:
		player.velocity = (1, 0)
		
	player.draw(wall_group)
	win.fill(black)
	all_sprites.draw(win)
	pygame.display.flip()
pygame.quit()