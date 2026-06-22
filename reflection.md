# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The first time I ran the game, it looked like a guessing game where you enter numbers in attempt to guess the correct one. It would hint to us if we should go higher or lower based on our guessed number. As we enter our guess, the number on the Attempts left would decrease, informing us the number of attempts we had left before the game will reveal the answer.
- List at least two concrete bugs you noticed at the start (for example: "the hints were backwards").
  - The hints that were given were not correct. It was not helping us get closer to the answer.
  - It allowed us to guess numbers way past the guessing range which was from 1 to 100.
  - After clicking New Game , the game does not seem to work afterwards.
  - The game is over before all the attempts have been reached.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                                                 | Expected Behavior                                                                                                                                   | Actual Behavior                                                                    | Console Output / Error                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------ |
| Guess of 45                                                           | Go HIGHER hint                                                                                                                                      | Retrieved Go LOWER hint even when the answer was 71                                | Go LOWER!                                        |
| Guess the correct number<br />and click on "New Game"                 | Game restarts                                                                                                                                       | Received a messaged and<br />am unable to submit any guesses<br />for the new game | You already won. Start a new game to play again. |
| Guessed numbers until game is over                                    | Game over is reached after all<br />the attempts have been used up                                                                                  | With 1 more attempt left, the game is over and<br />says we are out of attempts    | Out of attempts! The secret was 20. Score: -5    |
| Game over after not guessing the correct<br />and clicked on New Game | New Game is loaded                                                                                                                                  | An error message to start a new game appears                                       | Game over. Start a new game to try again.        |
| Changed the Difficulty setting from Normal<br />to Hard               | The hint of the number range would<br />change from "Guess a new number <br />between 1 and 100" **to** "Guess a new number <br />between 1 and 50" | The hint message stayed the same: "Guess a new number<br />between 1 and 50"       | None                                             |
| Guessed 100 twice                                                     | Go LOWER hint twice                                                                                                                                 | It switched between Go LOWER and Go HIGHER hints                                   | Go LOWER! and Go HIGHER!                         |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
