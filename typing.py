import pygame
import random
import time
import sys

# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 1200, 800
BG_COLOR = (32, 32, 32)
TEXT_COLOR = (255, 255, 255)
CORRECT_COLOR = (0, 0, 255)
INCORRECT_COLOR = (255, 0, 0)
FONT_SIZE = 32
# Setup Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")
font = pygame.font.Font(None, FONT_SIZE)


def load_sentences(filename="sentences.txt"):
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        return lines
    except FileNotFoundError:
        return ["The quick brown fox jumps over the lazy dog."]


def draw_text(surface, text, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))


def main():
    running = True
    clock = pygame.time.Clock()

    sentences = load_sentences()
    current_sentence = random.choice(sentences)
    user_text = ""

    start_time = 0
    total_time = 0
    started = False
    finished = False

    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if not finished:
                    if not started:
                        started = True
                        start_time = time.time()

                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.unicode:  # Check if it's a printable character
                        # Prevent typing more than sentence length? Maybe not, to allow errors.
                        # Let's limit it to reasonable length or just match length
                        if len(user_text) < len(current_sentence):
                            user_text += event.unicode

                    if user_text == current_sentence:
                        finished = True
                        end_time = time.time()
                        total_time = end_time - start_time
                else:
                    # Reset on Enter
                    if event.key == pygame.K_RETURN:
                        finished = False
                        started = False
                        user_text = ""
                        current_sentence = random.choice(sentences)
                        start_time = 0
                        total_time = 0
        # Drawing
        # Draw Target Sentence
        draw_text(screen, "Type this:", (200, 200, 200), 50, 50)
        draw_text(screen, current_sentence, TEXT_COLOR, 50, 100)

        # Draw User Input with Coloring
        x_offset = 50
        y_offset = 200

        draw_text(screen, "Your input:", (200, 200, 200), 50, 150)

        for i, char in enumerate(user_text):
            if i < len(current_sentence):
                if char == current_sentence[i]:
                    color = CORRECT_COLOR
                else:
                    color = INCORRECT_COLOR
            else:
                color = INCORRECT_COLOR  # Extra characters are wrong

            char_surface = font.render(char, True, color)
            screen.blit(char_surface, (x_offset, y_offset))
            x_offset += char_surface.get_width()

        # Draw Cursor
        if not finished and time.time() % 1 > 0.5:
            pygame.draw.rect(screen, (255, 255, 255), (x_offset, y_offset, 2, FONT_SIZE))
        # Stats
        if finished:
            wpm = (len(current_sentence) / 5) / (total_time / 60) if total_time > 0 else 0
            draw_text(screen, f"Finished! Time: {total_time:.2f}s", (255, 255, 0), 50, 300)
            draw_text(screen, f"WPM: {wpm:.2f}", (255, 255, 0), 50, 350)
            draw_text(screen, "Press ENTER to play again", (200, 200, 200), 50, 450)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()