import random
import tkinter as tk

# Basic config
MAX_ATTEMPTS = 6

WORD_LIST = [
    "apple", "banana", "orange", "grape", "mango",
    "tiger", "lion", "zebra", "horse", "monkey",
    "chair", "table", "sofa", "bed", "shelf",
    "robot", "phone", "laptop", "mouse", "keyboard",
    "water", "light", "earth", "plant", "stone",
    "house", "door", "window", "floor", "roof",
    "pizza", "bread", "butter", "cheese", "sugar",
    "train", "plane", "truck", "car", "bus",
    "river", "ocean", "beach", "island", "forest",
    "school", "college", "teacher", "student", "book","ant", "ball", "cat", "dog", "egg",
    "fan", "gift", "hat", "ice", "jar",
    "kite", "lamp", "map", "nest", "owl",
    "pen", "queen", "ring", "sun", "tree",
    "umbrella", "van", "watch", "box", "yard",
    "zoo", "actor", "baker", "candle", "doctor",
    "engine", "farmer", "garden", "hammer", "island",
    "jungle", "kitten", "ladder", "market", "needle",
    "office", "pencil", "quilt", "rocket", "school",
    "tunnel", "uniform", "village", "wallet", "yellow",
    "artist", "bridge", "circle", "desert", "energy",
    "family", "gold", "health", "idea", "jacket",
    "kitchen", "leader", "memory", "nature", "object",
    "people", "quick", "result", "system", "travel",
    "update", "vision", "window", "xray", "youth",
    "zebra", "angle", "bottle", "camera", "danger",
    "effect", "finger", "ground", "height", "income",
    "jewel", "knife", "lesson", "mirror", "number",
    "orange", "paper", "question", "reason", "signal",
    "target", "unit", "value", "world", "zone",
    "bread", "clock", "dream", "event", "field",
    "glass", "heart", "image", "joint", "key",
    "level", "model", "north", "order", "price",
    "quiet", "river", "sound", "table", "user",
    "voice", "water", "year", "zero", "light"
]


class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.root.geometry("450x600")
        self.root.resizable(False, False)

        # Game state
        self.word = random.choice(WORD_LIST)
        self.guessed = set()
        self.attempts = MAX_ATTEMPTS

        # UI Elements
        # Canvas for Drawing
        self.canvas = tk.Canvas(root, width=250, height=250, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(pady=20)
        
        self.word_label = tk.Label(root, text="", font=("Courier New", 28, "bold"))
        self.word_label.pack(pady=10)

        self.info_label = tk.Label(root, text="", font=("Arial", 12))
        self.info_label.pack()

        # Input Frame wrapper to look nice
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=15)
        
        self.entry = tk.Entry(self.input_frame, font=("Arial", 14), width=5, justify="center")
        self.entry.pack(side=tk.LEFT, padx=5)
        
        self.guess_button = tk.Button(self.input_frame, text="Guess", command=self.make_guess, font=("Arial", 12))
        self.guess_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(root, text="Restart Game", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=10)

        # Bind Enter key to entry submission
        self.root.bind('<Return>', lambda event: self.submit_guess_event())

        self.reset_game()  # Call reset to set up initial state properly

    def draw_hangman(self):
        self.canvas.delete("all")
        # Draw Gallows (always visible)
        self.canvas.create_line(50, 230, 200, 230, width=3) # Base
        self.canvas.create_line(125, 230, 125, 30, width=3) # Pole
        self.canvas.create_line(125, 30, 180, 30, width=3)  # Top
        self.canvas.create_line(180, 30, 180, 50, width=3)  # Rope

        mistakes = MAX_ATTEMPTS - self.attempts
        
        if mistakes >= 1: # Head
            self.canvas.create_oval(165, 50, 195, 80, width=3)
        if mistakes >= 2: # Body
            self.canvas.create_line(180, 80, 180, 150, width=3)
        if mistakes >= 3: # Left Arm
            self.canvas.create_line(180, 100, 150, 120, width=3)
        if mistakes >= 4: # Right Arm
            self.canvas.create_line(180, 100, 210, 120, width=3)
        if mistakes >= 5: # Left Leg
            self.canvas.create_line(180, 150, 160, 190, width=3)
        if mistakes >= 6: # Right Leg
            self.canvas.create_line(180, 150, 200, 190, width=3)

    def update_display(self):
        # Update drawing
        self.draw_hangman()
        
        # Show current word state
        display = " ".join([l if l in self.guessed else "_" for l in self.word])
        self.word_label.config(text=display)

        # Show attempts and guessed letters
        guessed_str = ", ".join(sorted(self.guessed)) if self.guessed else "None"
        info = f"Attempts left: {self.attempts}\nGuessed letters: {guessed_str}"
        self.info_label.config(text=info, fg="black")

    def submit_guess_event(self):
        # Only submit if button is active
        if self.guess_button['state'] == tk.NORMAL:
            self.make_guess()

    def make_guess(self):
        if self.attempts == 0 or all(l in self.guessed for l in self.word):
            return  # Game is already over

        letter = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)

        # Basic validation
        if len(letter) != 1 or not letter.isalpha():
            self.info_label.config(text="Please enter a valid single letter.", fg="red")
            return

        if letter in self.guessed:
            self.info_label.config(text="You already guessed that letter!", fg="orange")
            return

        self.guessed.add(letter)

        if letter not in self.word:
            self.attempts -= 1

        # Check win
        if all(l in self.guessed for l in self.word):
            self.draw_hangman()
            self.word_label.config(text=" ".join(self.word))
            self.info_label.config(text="🎉 You won! 🎉\nPress Restart to play again.", fg="green")
            self._disable_input()
            return

        # Check lose
        if self.attempts == 0:
            self.draw_hangman()
            self.word_label.config(text=" ".join(self.word)) # Reveal word
            self.info_label.config(text=f"💀 Game Over 💀\nThe word was: {self.word}\nPress Restart to play again.", fg="red")
            self._disable_input()
            return

        self.update_display()

    def _disable_input(self):
        self.entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)

    def _enable_input(self):
        self.entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)

    def reset_game(self):
        # Reset game state
        self.word = random.choice(WORD_LIST)
        self.guessed.clear()
        self.attempts = MAX_ATTEMPTS
        self._enable_input()
        self.update_display()
        self.entry.focus_set()


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
