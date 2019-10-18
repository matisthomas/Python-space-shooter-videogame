# Python-space-shooter-videogame
A videogame developed in python using pygame library.

-- INTRODUCTION --
Here is a space shooter I built with a friend of mine in our first year of computer sciences, in Liege University (Uliege, formerly known as ULG).
This was one of the very first program we made, and as we didn't have any python knowledge before, the code is quite a mess.
Anyway, i'm pretty proud of the final game, and we got a 19/20 mark which I assume is excellent.

-- THE GAME --
This is a simple 2d space shooter, you control a spaceship with Q for left and D for right. You can shoot by pressing the space bar on asteroid coming from above. 
You get 2 points by destroing it, and only one point by avoiding it.
if it hits you, you lose one of your three hearts.
Sometimes, a boss spawns and shoots lasers on you : you have to defeat him, but he will come back.

During the game, the asteroids and the boss' laser will go faster and faster and the boss will have increased health.

There are some bonuses and maluses, such as :

-BONUS :
1) A thunder bow increasing your attack speed for a limited amount of time.
2) A heart giving you back one of your three lifes.
3) A heart container, giving you a new stack of heart (there is only one container, so your don't end having 600 stacks).
4) A running boy, increasing your movement speed for a limited amount of time. //lost, I don't have that version anymore

-MALUS :
1) A snail, decreasing your movement speed for a limited amount of time.

All of them are showed either in the right top corner of the game, or in a little interface at the right bottom of the game, during their activation.


-- TO DO --
-Losing hearts from right to left makes no sense, it has to go from left to right.
-Make it playing again, I think we had to convert pictures in alpha or something, I'll have to look that up.
-I aim to make the code readable, having only one 800 lines of code file wasn't the best idea we had (we didn't know yet we could separate the code in multiple files ...).
