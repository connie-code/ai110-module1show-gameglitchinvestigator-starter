from logic_utils import check_guess, get_range_for_difficulty
from app import attempt_limit_map

#FIX: Updated tests using agent so that the functions that return tuples are accounted for in the return
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_guess_too_high_78_secret_41():
    outcome, _ = check_guess(78, 41)
    assert outcome == "Too High"

def test_easy_difficulty_instruction_range():
    low, high = get_range_for_difficulty("Easy")
    instruction = f"Guess a number between {low} and {high}."
    assert instruction == "Guess a number between 1 and 20."
