import random
import time
from colorama import Fore, Style, init

# Initialize colorama for cross-platform compatibility
init(autoreset=True)

def get_random_word(word_list):
    """Returns a random word from the given word list"""
    return random.choice(word_list)

def scramble_word(word):
    """Scrambles the given word by shuffling its characters"""
    return ''.join(random.sample(word, len(word)))

def check_descramble(scrambled_word, original_word):
    """Checks if the given scrambled word matches the original word"""
    return scrambled_word == original_word

def calculate_points(word):
    """Calculates points based on word length (Difficulty Rating)"""
    # Example logic: 3-4 letters = 10pts, 5-6 = 20pts, 7+ = 30pts
    length = len(word)
    if length <= 4:
        return 10
    elif length <= 6:
        return 20
    else:
        return 30

def calculate_average_time(round_times):
    """Calculates the average time taken to answer each question"""
    if not round_times:
        return 0
    return sum(round_times) / len(round_times)

def track_score():
    """Initializes the score tracking structure"""
    return {"total_points": 0, "rounds_played": 0}

def get_highest_scoring_word(word_list, scores):
    """Placeholder to maintain structure, returns None in new system"""
    return None

def get_total_correct_answers(word_list, scores):
    """Returns the total number of correct answers from the given word list"""
    return scores["total_points"]

def play_game(rounds):
    """Plays a specified number of rounds of the word descrambling game"""
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi",
                "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry",
                "tangerine", "watermelon"]
    overall_score = track_score()
    round_times = []

    # Welcome Screen
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.YELLOW + Style.BRIGHT + "    WELCOME TO THE WORD UNSCRAMBLER!    ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.WHITE + f"Can you unscramble {rounds} words before time runs out?\n")
    time.sleep(1)
    for i in range(rounds):
        print(Fore.BLUE + f"--- Round {i + 1} of {rounds} ---")
        original_word = get_random_word(word_list)
        scrambled_word = scramble_word(original_word)
        difficulty = "Easy" if len(original_word) <= 4 else "Medium" if len(original_word) <= 6 else "Hard"

        print(Fore.MAGENTA + Style.BRIGHT + f"Unscramble the word: {scrambled_word} ({difficulty} mode)")

        start_time = time.time()
        user_answer = input(Fore.WHITE + "Enter your answer: ").strip().lower()
        end_time = time.time()
        duration = end_time - start_time
        round_times.append(duration)

        if check_descramble(user_answer, original_word):
            points_earned = calculate_points(original_word)
            overall_score["total_points"] += points_earned
            print(Fore.GREEN + Style.BRIGHT + f"✔ Correct! +{points_earned} points")
        else:
            print(Fore.RED + Style.BRIGHT + f"✘ Sorry, the correct answer was: {original_word}")

        overall_score["rounds_played"] += 1

        print(Fore.CYAN + "\n--- Quick Stats ---")
        print(f"Time for this round: {Fore.YELLOW}{duration:.2f}s")
        print(f"Current Total Score: {Fore.GREEN}{overall_score['total_points']}")

        average_time = calculate_average_time(round_times)
        print(f"Avg Time: {Fore.YELLOW}{average_time:.2f}s")
        print("-" * 20 + "\n")

    # Final Summary
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.YELLOW + Style.BRIGHT + "          GAME OVER! FINAL RESULTS          ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(f"Total Points Accumulated: {Fore.GREEN}{overall_score['total_points']}")
    print(f"Total Rounds Completed: {Fore.WHITE}{overall_score['rounds_played']}")

    average_time = calculate_average_time(round_times)
    print(f"Average Speed: {Fore.YELLOW}{average_time:.2f}s per word")
    print(Fore.CYAN + "=" * 40)

if __name__ == "__main__":
    play_game(5)