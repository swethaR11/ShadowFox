#Hangman: Implement the wordguessing game with visual progress and hints.
import random

class Hangman:
    def __init__(self):
        self.words = [
            {"word": "python", "hint": "A popular programming language"},
            {"word": "hangman", "hint": "The name of this game"},
            {"word": "computer", "hint": "The device you're using now"},
            {"word": "keyboard", "hint": "Input device with keys"},
            {"word": "developer", "hint": "Person who writes code"},
            {"word": "algorithm", "hint": "Step-by-step procedure"},
            {"word": "variable", "hint": "Stores data in programming"}
        ]
        self.reset_game()
        
        # Hangman drawings for each wrong guess
        self.hangman_drawings = [
            """
               +---+
                   |
                   |
                   |
                  ===
            """,
            """
               +---+
               O   |
                   |
                   |
                  ===
            """,
            """
               +---+
               O   |
               |   |
                   |
                  ===
            """,
            """
               +---+
               O   |
              /|   |
                   |
                  ===
            """,
            """
               +---+
               O   |
              /|\\  |
                   |
                  ===
            """,
            """
               +---+
               O   |
              /|\\  |
              /    |
                  ===
            """,
            """
               +---+
               O   |
              /|\\  |
              / \\  |
                  ===
            """
        ]
    
    def reset_game(self):
        """Reset the game state"""
        self.selected_word = random.choice(self.words)
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
        self.game_over = False
    
    def display_game(self):
        """Display the current game state"""
        # Clear screen (works on Windows and Unix-like systems)
        print("\033c", end="")
        
        # Display hangman drawing
        print(self.hangman_drawings[self.wrong_guesses])
        
        # Display word with blanks for unguessed letters
        display_word = []
        for letter in self.selected_word["word"]:
            if letter in self.guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
        print(" ".join(display_word))
        print()
        
        # Display used letters
        print("Used letters:", " ".join(sorted(self.guessed_letters)))
        print()
    
    def get_hint(self):
        """Display the hint for the current word"""
        print(f"Hint: {self.selected_word['hint']}")
        input("\nPress Enter to continue...")
    
    def make_guess(self, letter):
        """Process a letter guess"""
        if self.game_over or letter in self.guessed_letters:
            return
        
        self.guessed_letters.append(letter)
        
        if letter not in self.selected_word["word"]:
            self.wrong_guesses += 1
            print(f"'{letter}' is not in the word!")
        else:
            print(f"Good guess! '{letter}' is in the word.")
        
        # Check win/lose conditions
        if all(letter in self.guessed_letters for letter in self.selected_word["word"]):
            self.display_game()
            print(f"Congratulations! You won! The word was '{self.selected_word['word']}'")
            self.game_over = True
        elif self.wrong_guesses >= self.max_wrong_guesses:
            self.display_game()
            print(f"Game Over! The word was '{self.selected_word['word']}'")
            self.game_over = True
        
        input("\nPress Enter to continue...")
    
    def play(self):
        """Main game loop"""
        while True:
            self.display_game()
            
            if self.game_over:
                choice = input("Would you like to play again? (y/n): ").lower()
                if choice == 'y':
                    self.reset_game()
                    continue
                else:
                    print("Thanks for playing!")
                    break
            
            print("1. Guess a letter")
            print("2. Get a hint")
            print("3. Quit game")
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                letter = input("Enter a letter: ").lower()
                if len(letter) != 1 or not letter.isalpha():
                    print("Please enter a single letter.")
                    input("\nPress Enter to continue...")
                else:
                    self.make_guess(letter)
            elif choice == '2':
                self.get_hint()
            elif choice == '3':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    game = Hangman()
    game.play()