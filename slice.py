import pygame
import cv2
import mediapipe as mp
import random
import math
# SETUP
pygame.init()

WIDTH = 1280
HEIGHT = 720
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Slice - Webcam Edition")

clock = pygame.time.Clock()
# FONTS
font_score = pygame.font.Font(None, 52)
font_combo = pygame.font.Font(None, 46)
font_small = pygame.font.Font(None, 28)
font_gameover = pygame.font.Font(None, 90)

# COLORS
WHITE = (245, 245, 245)
BLACK = (10, 10, 12)
RED = (235, 50, 55)
GREEN = (70, 220, 100)
YELLOW = (255, 220, 50)
ORANGE = (255, 145, 25)
PURPLE = (145, 70, 210)
BLUE = (70, 160, 240)
# WEBCAM
camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not camera.isOpened():
    print("Could not open webcam.")
    pygame.quit()
    raise SystemExit
# MEDIAPIPE
mp_hands = mp.solutions.hands

hand_tracker = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.65,
    min_tracking_confidence=0.65
)
# FRUIT TYPES
FRUITS = [
    "apple",
    "orange",
    "lemon",
    "watermelon",
    "plum",
    "strawberry"
]

# FRUIT CLASS
class Fruit:

    def __init__(self):

        self.kind = random.choice(FRUITS)

        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT + random.randint(30, 100)

        self.vx = random.uniform(-6.5, 6.5)
        self.vy = random.uniform(-20.5, -16.5)

        self.gravity = random.uniform(0.30, 0.37)

        self.size = random.randint(35, 52)

        self.rotation = random.randint(0, 360)
        self.rotation_speed = random.uniform(-6, 6)

    def update(self):

        self.x += self.vx
        self.y += self.vy

        self.vy += self.gravity

        self.rotation += self.rotation_speed

        if self.x < self.size:

            self.x = self.size
            self.vx *= -0.85

        if self.x > WIDTH - self.size:

            self.x = WIDTH - self.size
            self.vx *= -0.85

    def draw(self, surface):

        if self.kind == "apple":
            self.draw_apple(surface)

        elif self.kind == "orange":
            self.draw_orange(surface)

        elif self.kind == "lemon":
            self.draw_lemon(surface)

        elif self.kind == "watermelon":
            self.draw_watermelon(surface)

        elif self.kind == "plum":
            self.draw_plum(surface)

        elif self.kind == "strawberry":
            self.draw_strawberry(surface)
    # APPLE
    def draw_apple(self, surface):

        x = int(self.x)
        y = int(self.y)
        r = self.size

        color = (215, 35, 45)

        pygame.draw.circle(
            surface,
            color,
            (x - 12, y),
            r - 10
        )

        pygame.draw.circle(
            surface,
            color,
            (x + 12, y),
            r - 10
        )

        pygame.draw.circle(
            surface,
            color,
            (x, y + 8),
            r - 9
        )

        pygame.draw.circle(
            surface,
            (255, 110, 110),
            (x - 17, y - 17),
            7
        )

        pygame.draw.line(
            surface,
            (75, 45, 20),
            (x, y - r + 5),
            (x + 5, y - r - 15),
            6
        )

        pygame.draw.ellipse(
            surface,
            GREEN,
            (x + 3, y - r - 12, 25, 13)
        )
    # ORANGE
    def draw_orange(self, surface):

        x = int(self.x)
        y = int(self.y)
        r = self.size - 3

        pygame.draw.circle(
            surface,
            ORANGE,
            (x, y),
            r
        )

        for i in range(12):

            angle = i * math.pi * 2 / 12

            px = x + int(
                math.cos(angle) * r * 0.65
            )

            py = y + int(
                math.sin(angle) * r * 0.65
            )

            pygame.draw.circle(
                surface,
                (240, 125, 15),
                (px, py),
                2
            )

        pygame.draw.ellipse(
            surface,
            GREEN,
            (x - 5, y - r - 8, 25, 12)
        )

        pygame.draw.circle(
            surface,
            (255, 220, 130),
            (x - 14, y - 15),
            7
        )
    # LEMON
    def draw_lemon(self, surface):

        x = int(self.x)
        y = int(self.y)

        points = []

        for i in range(20):

            angle = 2 * math.pi * i / 20

            px = x + math.cos(angle) * self.size
            py = y + math.sin(angle) * self.size * 0.65

            points.append(
                (int(px), int(py))
            )

        pygame.draw.polygon(
            surface,
            YELLOW,
            points
        )

        pygame.draw.ellipse(
            surface,
            (255, 245, 150),
            (
                x - self.size // 2,
                y - 10,
                18,
                10
            )
        )

        pygame.draw.circle(
            surface,
            (225, 185, 30),
            (x - self.size, y),
            5
        )

        pygame.draw.circle(
            surface,
            (225, 185, 30),
            (x + self.size, y),
            5
        )
    # WATERMELON
    def draw_watermelon(self, surface):

        x = int(self.x)
        y = int(self.y)
        r = self.size

        pygame.draw.circle(
            surface,
            (35, 155, 70),
            (x, y),
            r
        )

        pygame.draw.circle(
            surface,
            (90, 205, 85),
            (x, y),
            r - 8
        )

        pygame.draw.circle(
            surface,
            (235, 55, 70),
            (x, y),
            r - 15
        )

        for i in range(7):

            angle = i * 0.9

            sx = x + int(
                math.cos(angle) * (r - 22)
            )

            sy = y + int(
                math.sin(angle) * (r - 22)
            )

            pygame.draw.ellipse(
                surface,
                BLACK,
                (sx - 3, sy - 6, 6, 12)
            )
    # PLUM
    def draw_plum(self, surface):

        x = int(self.x)
        y = int(self.y)
        r = self.size

        pygame.draw.ellipse(
            surface,
            PURPLE,
            (
                x - r,
                y - r,
                r * 2,
                r * 2 + 12
            )
        )

        pygame.draw.ellipse(
            surface,
            (205, 150, 240),
            (
                x - r // 2,
                y - r // 2,
                13,
                22
            )
        )

        pygame.draw.line(
            surface,
            (75, 45, 20),
            (x, y - r),
            (x + 3, y - r - 14),
            5
        )
    # STRAWBERRY
    def draw_strawberry(self, surface):

        x = int(self.x)
        y = int(self.y)
        r = self.size

        points = [
            (x, y + r),
            (x - r, y - r // 2),
            (x - r // 2, y - r),
            (x, y - r // 2),
            (x + r // 2, y - r),
            (x + r, y - r // 2)
        ]

        pygame.draw.polygon(
            surface,
            (225, 35, 65),
            points
        )

        for row in range(3):

            for col in range(3):

                sx = x - 18 + col * 18
                sy = y - 5 + row * 15

                pygame.draw.ellipse(
                    surface,
                    YELLOW,
                    (sx, sy, 5, 8)
                )

        pygame.draw.polygon(
            surface,
            GREEN,
            [
                (x, y - r),
                (x - 18, y - r - 10),
                (x - 5, y - r + 2),
                (x + 8, y - r - 12),
                (x + 18, y - r - 5)
            ]
        )
# BOMB CLASS
class Bomb:

    def __init__(self):

        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT + 80

        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-19, -16)

        self.gravity = 0.34

        self.radius = random.randint(34, 43)

        self.fuse_angle = 0

    def update(self):

        self.x += self.vx
        self.y += self.vy

        self.vy += self.gravity

        self.fuse_angle += 8

        if self.x < self.radius:

            self.x = self.radius
            self.vx *= -1

        if self.x > WIDTH - self.radius:

            self.x = WIDTH - self.radius
            self.vx *= -1

    def draw(self, surface):

        x = int(self.x)
        y = int(self.y)
        r = self.radius

        # Bomb body
        pygame.draw.circle(
            surface,
            (25, 25, 30),
            (x, y),
            r
        )

        # Highlight
        pygame.draw.circle(
            surface,
            (65, 65, 75),
            (
                x - r // 3,
                y - r // 3
            ),
            8
        )

        # Fuse
        pygame.draw.line(
            surface,
            (120, 75, 35),
            (x + 18, y - 28),
            (x + 35, y - 48),
            5
        )

        # Spark
        spark_x = x + 35
        spark_y = y - 48

        pygame.draw.circle(
            surface,
            YELLOW,
            (spark_x, spark_y),
            7
        )

        pygame.draw.circle(
            surface,
            ORANGE,
            (spark_x, spark_y),
            3
        )
# PARTICLES
class Particle:

    def __init__(self, x, y, color):

        self.x = x
        self.y = y

        self.vx = random.uniform(-8, 8)
        self.vy = random.uniform(-8, 3)

        self.gravity = 0.25

        self.size = random.randint(3, 8)

        self.life = random.randint(20, 40)

        self.color = color

    def update(self):

        self.x += self.vx
        self.y += self.vy

        self.vy += self.gravity

        self.life -= 1

    def draw(self, surface):

        if self.life <= 0:
            return

        pygame.draw.circle(
            surface,
            self.color,
            (int(self.x), int(self.y)),
            self.size
        )
# BLADE TRAIL

blade_points = []


def record_blade(x, y):

    blade_points.append(
        [x, y, 255]
    )

    if len(blade_points) > 18:
        blade_points.pop(0)


def render_blade(surface):

    if len(blade_points) < 2:
        return

    for i in range(1, len(blade_points)):

        x1, y1, alpha1 = blade_points[i - 1]
        x2, y2, alpha2 = blade_points[i]

        alpha = int(
            max(
                0,
                min(
                    255,
                    min(alpha1, alpha2)
                )
            )
        )

        if alpha <= 0:
            continue

        blade_layer = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )

        pygame.draw.line(
            blade_layer,
            (220, 245, 255, alpha),
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            8
        )

        surface.blit(
            blade_layer,
            (0, 0)
        )

    # Fade trail
    for point in blade_points:

        point[2] = max(
            0,
            point[2] - 18
        )

    # Remove invisible points
    blade_points[:] = [
        point
        for point in blade_points
        if point[2] > 0
    ]
# COLLISION
def line_hits_circle(
    cx,
    cy,
    radius,
    x1,
    y1,
    x2,
    y2
):

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:

        distance = math.hypot(
            cx - x1,
            cy - y1
        )

        return distance < radius

    t = (
        (cx - x1) * dx +
        (cy - y1) * dy
    ) / (dx * dx + dy * dy)

    t = max(
        0,
        min(1, t)
    )

    closest_x = x1 + t * dx
    closest_y = y1 + t * dy

    distance = math.hypot(
        cx - closest_x,
        cy - closest_y
    )

    return distance < radius
# GAME VARIABLES
fruits = []
bombs = []
particles = []

score = 0
combo = 0
lives = 3

blade_x = WIDTH // 2
blade_y = HEIGHT // 2

previous_x = blade_x
previous_y = blade_y

last_spawn = pygame.time.get_ticks()

SPAWN_DELAY = 700

game_over = False
# BACKGROUND
def draw_background():

    screen.fill(
        (14, 19, 30)
    )

    for i in range(9):

        x = (i * 170 + 80) % WIDTH
        y = 100 + (i % 4) * 170

        pygame.draw.circle(
            screen,
            (19, 27, 43),
            (x, y),
            80
        )
# RESET GAME
def reset_game():

    global fruits
    global bombs
    global particles
    global score
    global combo
    global lives
    global game_over
    global previous_x
    global previous_y

    fruits = []
    bombs = []
    particles = []

    score = 0
    combo = 0
    lives = 3

    game_over = False

    previous_x = blade_x
    previous_y = blade_y
# MAIN LOOP
running = True

while running:

    clock.tick(FPS)
    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False

            if event.key == pygame.K_r and game_over:

                reset_game()
    # WEBCAM
    success, frame = camera.read()

    if not success:
        continue

    frame = cv2.flip(
        frame,
        1
    )

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    result = hand_tracker.process(
        rgb_frame
    )

    hand_detected = False

    if result.multi_hand_landmarks:

        hand_detected = True

        hand = result.multi_hand_landmarks[0]

        fingertip = hand.landmark[8]

        target_x = int(
            fingertip.x * WIDTH
        )

        target_y = int(
            fingertip.y * HEIGHT
        )

        blade_x = int(
            blade_x * 0.35 +
            target_x * 0.65
        )

        blade_y = int(
            blade_y * 0.35 +
            target_y * 0.65
        )
    # GAME UPDATE
    if not game_over:

        # Record blade position
        record_blade(
            blade_x,
            blade_y
        )
        # SPAWN
        current_time = pygame.time.get_ticks()

        if current_time - last_spawn >= SPAWN_DELAY:

            number = random.choices(
                [1, 2, 3],
                weights=[5, 3, 1]
            )[0]

            for _ in range(number):

                fruits.append(
                    Fruit()
                )

            # Bomb chance
            if random.random() < 0.22:

                bombs.append(
                    Bomb()
                )

            last_spawn = current_time
        # UPDATE FRUITS
        for fruit in fruits[:]:

            fruit.update()

            if fruit.y > HEIGHT + 100:

                fruits.remove(fruit)

                combo = 0
        # UPDATE BOMBS
        for bomb in bombs[:]:

            bomb.update()

            if bomb.y > HEIGHT + 100:

                bombs.remove(bomb)
        # FRUIT COLLISION
        for fruit in fruits[:]:

            if line_hits_circle(
                fruit.x,
                fruit.y,
                fruit.size,
                previous_x,
                previous_y,
                blade_x,
                blade_y
            ):

                score += 10
                combo += 1

                fruit_color = {
                    "apple": (215, 35, 45),
                    "orange": ORANGE,
                    "lemon": YELLOW,
                    "watermelon": (235, 55, 70),
                    "plum": PURPLE,
                    "strawberry": (225, 35, 65)
                }[fruit.kind]

                for _ in range(35):

                    particles.append(
                        Particle(
                            fruit.x,
                            fruit.y,
                            fruit_color
                        )
                    )

                fruits.remove(fruit)
        # BOMB COLLISION
        for bomb in bombs[:]:

            # Slightly larger collision area so
            # bomb hits are easier to detect.
            if line_hits_circle(
                bomb.x,
                bomb.y,
                bomb.radius + 15,
                previous_x,
                previous_y,
                blade_x,
                blade_y
            ):

                # Explosion particles
                for _ in range(60):

                    particles.append(
                        Particle(
                            bomb.x,
                            bomb.y,
                            random.choice(
                                [
                                    RED,
                                    ORANGE,
                                    YELLOW,
                                    WHITE
                                ]
                            )
                        )
                    )

                # Remove bomb
                bombs.remove(bomb)

                # IMMEDIATE GAME OVER
                lives = 0
                combo = 0
                game_over = True

                break
        # PARTICLES
        for particle in particles[:]:

            particle.update()

            if particle.life <= 0:

                particles.remove(particle)
    # DRAW
    draw_background()

    # Fruits
    for fruit in fruits:

        fruit.draw(screen)

    # Bombs
    for bomb in bombs:

        bomb.draw(screen)

    # Particles
    for particle in particles:

        particle.draw(screen)

    # Blade
    render_blade(screen)

    if hand_detected:

        pygame.draw.circle(
            screen,
            WHITE,
            (blade_x, blade_y),
            11
        )

        pygame.draw.circle(
            screen,
            (150, 235, 255),
            (blade_x, blade_y),
            5
        )
    # SCORE
    score_text = font_score.render(
        f"SCORE: {score}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (25, 20)
    )
    # COMBO
    combo_text = font_combo.render(
        f"COMBO x{combo}",
        True,
        YELLOW
    )

    screen.blit(
        combo_text,
        (25, 70)
    )
    # LIVES
    lives_text = font_score.render(
        f"LIVES: {lives}",
        True,
        RED
    )

    screen.blit(
        lives_text,
        (WIDTH - 190, 20)
    )
    # HAND STATUS
    if hand_detected:

        status = font_small.render(
            "HAND DETECTED",
            True,
            GREEN
        )

    else:

        status = font_small.render(
            "SHOW YOUR HAND",
            True,
            RED
        )

    screen.blit(
        status,
        (25, HEIGHT - 45)
    )
    # GAME OVER
    if game_over:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill(
            (0, 0, 0, 170)
        )

        screen.blit(
            overlay,
            (0, 0)
        )

        game_over_text = font_gameover.render(
            "GAME OVER",
            True,
            WHITE
        )

        screen.blit(
            game_over_text,
            game_over_text.get_rect(
                center=(
                    WIDTH // 2,
                    HEIGHT // 2 - 50
                )
            )
        )

        final_score = font_score.render(
            f"Final Score: {score}",
            True,
            YELLOW
        )

        screen.blit(
            final_score,
            final_score.get_rect(
                center=(
                    WIDTH // 2,
                    HEIGHT // 2 + 30
                )
            )
        )

        restart = font_small.render(
            "Press R to restart",
            True,
            WHITE
        )

        screen.blit(
            restart,
            restart.get_rect(
                center=(
                    WIDTH // 2,
                    HEIGHT // 2 + 85
                )
            )
        )
    # SAVE BLADE POSITION
    previous_x = blade_x
    previous_y = blade_y
    pygame.display.flip()
# CLEANUP
camera.release()
hand_tracker.close()
pygame.quit()