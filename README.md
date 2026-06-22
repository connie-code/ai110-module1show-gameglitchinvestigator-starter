# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose:
  - [ ] The game's purpose is to guess the secret number. Depending on the difficulty level that is selected, the range of numbers will increase. The glitchy part of the game is where the scoring happens, based on the guess, the score will be reflected.

- [ ] Detail which bugs you found.
  - [ ] The hints were in reverse. When it should tell the player to guess lower, it tells them to guess higher.
  - [ ] The game would not let player restart the game when clicking on New Game.
  - [ ] The difficulty level ranges for Normal and Hard were swapped
  - [ ] The instructions will tell the player to guess from range 1 to 100 for all difficulties

- [ ] Explain what fixes you applied.
  - [ ] The hint that was reverse is fixed - when the guess is higher than the secret, the hint will tell the player to go lower and vise versa.
  - [ ] The difficulty level ranges for Normal and Hard were changed to be 1 to 50 and 1 to 100, respectively.
  - [ ] The instructions for the player is more dynamic in displaying that range players will need to guess depending on the difficulty select.
  - [ ] Players are able to start a new game by clicking on New Game after a failed or successfuly attempt.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Player enters a guess of 54
2. Game returns "Go LOWER!" as a hint
3. Player enter another guess of 15
4. Game returns "Go HIGHER! as a hint"
5. Player enters a guess of 35
6. Game returns "Go LOWER!"
7. Player enters a guess of 30
8. Game returns "Go LOWER!"
9. Player enters a guess of 20
10. Game returns "Go HIGHER!" as a hint
11. Player continues to guess until all 8 attempts have been reached
12. The game ends after the all attempts have ran out

**Screenshot** _(optional)_: `<!-- Insert a screenshot of your fixed, winning game here -->`

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
collected 5 items

tests/test_game_logic.py .....                                                                                                                            [100%]

======================================================================= 5 passed in 0.85s =======================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
