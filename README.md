-- Rock Paper Scissors RPG game --
-- Written by c0mp7t3rk1d-- 

This is a dungeon crawler RPG game that uses Rock Paper Scissors as the combat system.

The game is still in Pre-Alpha, so I'll release it when I've programmed 10 rooms into the game.

Feel free to fork, I'd be happy to include some of your code and credit you!

I had ChatGPT clean up the code, and in the Rock Paper Scissors logic it uses the modulus operator to avoid having to write out all the possibilities! It's pretty smart.

How does the maths behind the Rock Paper scissors even work?
- The program uses the random library to generate 2 random numbers, both ranging from 1-3.
- It then subtracts the enemies' number from the player's number, and uses the modulo operator to find the remainder of the sum. (It makes way more sense as an equation)
- If the Modulo sum = 0, it's a draw, if the modulo sum = 1, player victory, if the modulo sum = 2, enemy victory.

Here's an example

**Player** || **Enemy** || **Modulo Sum** || **Result**

Rock (1) ||	Rock (1) ||	(1 - 1) % 3 = 0 ||	Draw
