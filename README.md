# Breakout


This is my first Python Opengl game. 

### Game levels
The game has three levels. Each level has more tiles than the previous, the paddle gets smaller and faster and the ball travels faster as well.

### Player lives
The player has three lives throughout the three levels. The player loses a life if the ball goes below the paddle.

### Win or lose
If the player finishes all the levels, the game stops and a green box is displayed.
If the player loses all his lives, the game is lost and a red box is displayed.


### Known bugs
Paddle and ball physics are lacking, for example, if the ball is falling straight down dir(0, -1), the ball does not check its left and right outer bounds, meaning the ball can pass the paddle without hitting it. Same applies to tiles, the ball can go slightly passed the tile without colliding with it.


### Sources
https://gamedev.stackexchange.com/questions/4253/in-pong-how-do-you-calculate-the-balls-direction-when-it-bounces-off-the-paddl