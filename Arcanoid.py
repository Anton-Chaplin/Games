import pygame
import sys

from pygame.examples.go_over_there import screen

# ініціалізація проекту
pygame.init()

# Вікно гри
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcanoid")
score = 0
lives=3
# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0 , 200)
font=pygame.font.SysFont("Arial", 30)
# Платформа
paddle_width = 100
paddle_height = 15
paddle_speed = 8
paddle = pygame.Rect(WIDTH//2-paddle_width//2,HEIGHT - 40, paddle_width, paddle_height)

#м'яч
ball_radius=20
ball_speed=[4,-4]
ball=pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_radius, ball_radius)
clock=pygame.time.Clock()
#блоки
block_rows=5
block_calls=8
block_width= WIDTH // block_calls
block_height=30
blocks=[]
for row in range(block_rows):
    for call in range (block_calls):
        block=pygame.Rect(call*block_width, row*block_height, block_width-5, block_height-5)
        blocks.append(block)
running=True
# Ігровий цикл
while running:
    screen.fill("purple")
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)
    text = font.render(f"Бали:{score}", True, WHITE)
    screen.blit(text, (10, 10))
    lives_text=font.render(f"Життя:{lives}", True, WHITE)
    screen.blit(lives_text, (WIDTH-150, 10))
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #керування платформою
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left>0:
        paddle.x-=paddle_speed
    elif keys[pygame.K_RIGHT] and paddle.right<WIDTH:
        paddle.x+=paddle_speed
    elif keys[pygame.K_a] and paddle.left>0:
        paddle.x-=paddle_speed
    elif keys[pygame.K_d] and paddle.right<WIDTH:
        paddle.x+=paddle_speed
#рух м'яча
    ball.x+=ball_speed[0]
    ball.y+=ball_speed[1]
#зіткнення з стінами
    if ball.left<=0 or ball.right>=WIDTH:
        ball_speed[0]=-ball_speed[0]
    if ball.top<=0:
        ball_speed[1]=-ball_speed[1]
#зіткнення з платформою
    if ball.colliderect(paddle):
        ball_speed[1]=-ball_speed[1]
#зіткнення з блоками
    hit_index=ball.collidelist(blocks)
    if hit_index!=-1:
        blocks.pop(hit_index)
        score+=1 # score = score + 1
        ball_speed[1]=-ball_speed[1]

    if ball.bottom>HEIGHT:
        lives -= 1
        if lives == -1:
            text=font.render("Ти програв", True, WHITE)
            screen.blit(text, (WIDTH//2-text.get_width()//2, HEIGHT//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running=False
        else:
            #перезапуск м'яча
            ball.x=WIDTH//2
            ball.y=HEIGHT//2
            ball_speed=[4, -4]
            paddle.x=WIDTH//2-paddle_width//2
    if not blocks:
        text=font.render("Ти виграв", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running=False
pygame.quit()
sys.exit()