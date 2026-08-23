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

def track_score():
    """Initializes the score tracking structure"""
    return {"correct": {}, "incorrect": {}}

def get_top_three(word_list, scores):
    """Returns the top three words from the given word list based on their scores"""
    word_scores = {}
    for word in word_list:
        word_scores[word] = scores["correct"].get(word, 0)
    sorted_word_scores = sorted(word_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_scores[:3]

def get_highest_scoring_word(word_list, scores):
    """Returns the word with the highest score from the given word list"""
    word_scores = {}
    for word in word_list:
        word_scores[word] = scores["correct"].get(word, 0)
    max_score = max(word_scores.values())
    return [word for word, score in word_scores.items() if score == max_score][0]

def get_total_correct_answers(word_list, scores):
    """Returns the total number of correct answers from the given word list"""
    return sum(scores["correct"].values())

def get_highest_scoring_word_percentage(word_list, scores, total_rounds):
    """Returns the percentage of the highest scoring word's score relative to the total rounds played"""
    highest_scoring_word = get_highest_scoring_word(word_list, scores)
    highest_scoring_word_score = scores["correct"].get(highest_scoring_word, 0)
    return (highest_scoring_word_score / total_rounds) * 100 if total_rounds > 0 else 0

def calculate_average_time(round_times):
    """Calculates the average time taken to answer each question"""
    if not round_times:
        return 0
    return sum(round_times) / len(round_times)

def display_highest_scoring_word_percentage(word_list, scores, total_rounds):
    """Displays the highest scoring word's score as a percentage of the total possible score"""
    percentage = get_highest_scoring_word_percentage(word_list, scores, total_rounds)
    print(f"Highest scoring word percentage: {percentage:.2f}%")

def play_game(rounds):
    """Plays a specified number of rounds of the word descrambling game"""
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
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
        print(Fore.MAGENTA + Style.BRIGHT + f"Unscramble the word: {scrambled_word}")

        start_time = time.time()
        user_answer = input(Fore.WHITE + "Enter your answer: ").strip().lower()
        end_time = time.time()
        duration = end_time - start_time
        round_times.append(duration)

        if check_descramble(user_answer, original_word):
            print(Fore.GREEN + Style.BRIGHT + "✔ Correct!")
            overall_score["correct"][original_word] = overall_score["correct"].get(original_word, 0) + 1
        else:
            print(Fore.RED + Style.BRIGHT + f"✘ Sorry, the correct answer was: {original_word}")
            overall_score["incorrect"][original_word] = overall_score["incorrect"].get(original_word, 0) + 1

        print(Fore.CYAN + "\n--- Quick Stats ---")
        print(f"Time for this round: {Fore.YELLOW}{duration:.2f}s")
        top_three_words = get_top_three(word_list, overall_score)
        print(f"Top 3 words: {Fore.GREEN}{top_three_words}")

        highest_scoring_word = get_highest_scoring_word(word_list, overall_score)
        print(f"Leader: {Fore.YELLOW}{highest_scoring_word} ({overall_score['correct'].get(highest_scoring_word, 0)})")

        total_correct_answers = get_total_correct_answers(word_list, overall_score)
        print(f"Total Correct: {Fore.GREEN}{total_correct_answers}")

        average_time = calculate_average_time(round_times)
        print(f"Avg Time: {Fore.YELLOW}{average_time:.2f}s")
        print("-" * 20 + "\n")

    # Final Summary
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.YELLOW + Style.BRIGHT + "          GAME OVER! FINAL RESULTS          ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(f"Final Score Details: {Fore.WHITE}{overall_score}")
    average_score = {
        "correct": sum(overall_score["correct"].values()) / rounds,
        "incorrect": sum(overall_score["incorrect"].values()) / rounds
    }
    print(f"Average Success Rate: {Fore.GREEN}{average_score['correct']} correct per round")
    print(Fore.CYAN + "=" * 40)
if __name__ == "__main__":
    play_game(5)

