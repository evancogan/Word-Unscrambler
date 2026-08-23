import random

def get_random_word(word_list):
    """Returns a random word from the given word list"""
    return random.choice(word_list)

def scramble_word(word):
    """Scrambles the given word by shuffling its characters"""
    return ''.join(random.sample(word, len(word)))

def check_descramble(scrambled_word, original_word):
    """Checks if the given scrambled word matches the original word"""
    return scrambled_word == original_word

def track_score(correct_answers, incorrect_answers):
    """Tracks the user's score"""
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

def get_highest_scoring_word_percentage(word_list, scores):
    """Returns the percentage of the highest scoring word's score relative to the total possible score"""
    highest_scoring_word = get_highest_scoring_word(word_list, scores)
    total_possible_score = len(word_list) * len(word_list)
    highest_scoring_word_score = scores["correct"].get(highest_scoring_word, 0)
    return (highest_scoring_word_score / total_possible_score) * 100

def calculate_average_time(word_list, scores):
    """Calculates the average time taken to answer each question"""
    if not scores["correct"]:
        return 0
    total_time = 0
    for word in word_list:
        total_time += scores["correct"].get(word, 0) * 10
    return total_time / len(word_list)

def display_highest_scoring_word_percentage(word_list, scores):
    """Displays the highest scoring word's score as a percentage of the total possible score"""
    highest_scoring_word_percentage = get_highest_scoring_word_percentage(word_list, scores)
    print(f"Highest scoring word percentage: {highest_scoring_word_percentage}%")

def play_game(rounds):
    """Plays a specified number of rounds of the word descrambling game"""
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    overall_score = track_score(0, 0)
    top_three_words = []
    highest_scoring_word = None
    total_correct_answers = 0
    highest_scoring_word_percentage = None
    average_time = None
    for _ in range(rounds):
        original_word = get_random_word(word_list)
        scrambled_word = scramble_word(original_word)
        print(f"Unscramble the word: {scrambled_word}")
        user_answer = input("Enter your answer: ")
        score = track_score(0, 0)
        if check_descramble(user_answer, original_word):
            print("Correct!")
            score["correct"][original_word] = score["correct"].get(original_word, 0) + 1
        else:
            print(f"Sorry, the correct answer was: {original_word}")
            score["incorrect"][original_word] = score["incorrect"].get(original_word, 0) + 1
        print("Current score:", score)
        top_three_words = get_top_three(word_list, score)
        print("Top 3 words:", top_three_words)
        highest_scoring_word = get_highest_scoring_word(word_list, score)
        print(f"Highest scoring word: {highest_scoring_word} with score {score['correct'].get(highest_scoring_word, 0)}")
        total_correct_answers = get_total_correct_answers(word_list, score)
        print(f"Total correct answers: {total_correct_answers}")
        highest_scoring_word_percentage = get_highest_scoring_word_percentage(word_list, score)
        print(f"Highest scoring word percentage: {highest_scoring_word_percentage}%")
        average_time = calculate_average_time(word_list, score)
        print(f"Average time taken: {average_time} seconds")
        display_highest_scoring_word_percentage(word_list, score)
        overall_score = track_score(0, 0)
    rounds = 0
    # game loop
    while True:
        word = input("Enter a word: ")
        is_correct = input("Is the word correct? (yes/no): ").lower() == "yes"
        if is_correct:
            overall_score["correct"][word] = overall_score["correct"].get(word, 0) + 1
        else:
            overall_score["incorrect"][word] = overall_score["incorrect"].get(word, 0) + 1
        rounds += 1
        if input("Do you want to continue? (yes/no): ").lower() != "yes":
            break

    average_score = {
        "correct": sum(overall_score["correct"].values()) / rounds,
        "incorrect": sum(overall_score["incorrect"].values()) / rounds
    }
    print("Final score:", overall_score)
    print("Average score:", average_score)

if __name__ == "__main__":
    play_game(5)

