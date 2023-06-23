# Wordle game with 5,6,7-letter word options

<p align="center">
  <img src="https://github.com/khoatran94/wordle_pygame/assets/39628780/626c5b36-13f2-404d-b0e8-41c3991ae403" width="400">
</p>

## Description
* Wordle is a word puzzle game where you have a maximum of 6 guesses to find a target word within a grid of letters.
* Keep in mind every guess must be completed and meaningful.
* The game is available with 3 modes, 5-, 6-, or 7-letter words.


## Gameplay
* A virtual keyboard is presented for you. You can use your own physical keyboard as well
* Three additional buttons ***Enter***, ***Space***, and ***Backspace*** are also available to guess the word, to start a new game, or to erase the current letter on the grid, respectively.
* For every letter in the guess word that is also in the target word, it will be highlighted as green on the grid if the position is matched, otherwise, it will be highlighted as yellow. (The game behavior exactly matches with [NYTimes's Wordle](https://www.nytimes.com/games/wordle/index.html)).


## Files
The game is run from **wordle_GUI.py** file. To start the game, input 5, 6, or 7 to choose the length of the generated target word.
  
## References:
 * The English words are randomly generated from [dwyl/english-words](https://github.com/dwyl/english-words).

