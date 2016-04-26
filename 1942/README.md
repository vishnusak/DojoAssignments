# 1942 - HTML / CSS / Javascript
  This is the shoot'em up game suggested as part of the optional assignments. I didn't use jQuery, just plain old javascript (as shown in the demo video). I used some of the ideas from the video and mixed them with concepts from the pacman game. 
  I call my hero GUY and the enemies are REDs. Nothing against communists. When I started building this, I was using RED colored helicopter gif for the bad guys. Hence REDs. In the final version now, they look like MIGs fighting an F35 or something. Purely unintentional and only a product of the images I was able to easily find. With that out of the way...
  
## What works:
- Controlling GUY
- Enemy aircraft (reds)
- Firing Missiles (use the space bar)
- Enemies crashing into GUY
- Missiles destroying REDs

## What is wonky:
- The crash doesn't show up as a ball of fire most of the times (though when it does show up, it looks great!). Instead the aircraft/missiles just disappear which is so bleh. I know this is because the refresh/redraw of the game area is happening so quickly that the gif doesn't get time to start and finish. Trying to figure out how to get the crash to show up though I haven't hit upon a good solution yet.
- Crash detection: Sometimes it is smooth. A lot of times it is so jumpy that the enemy plane disappears as the missile is approaching and then re-appears two spots ahead, right on GUYs nose!
- Scoring: Completely absent. I spent so much time trying to figure out how to iron out the above issues that I completely missed scoring. Should be easy to do.
- No Sound: Haven't even given this a thought yet!

### So take a look, give it a spin and let me know what you think. All reviews/comments are welcome.