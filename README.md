# micropython-microbit-kitronik-game-controller
Example MicroPython (for BBC micro:bit) code for the Kitronik :GAME Controller ( www.kitronik.co.uk/5644 )

## Overview

This package contains a functions to use the input buttons and audio and haptic feedback devices on the :GAME Controller.

## Buttons

The function to check which button has been pressed takes a single argument, the button name, which is one of:
* Up
* Down
* Left
* Right
* Fire_1
* Fire_2
```
KitronikGameController.onButtonPress(KitronikGameController.Up)
```
The function returns a True or False output, so is ideal for use in 'if' statements or 'while' loops.

## Buzzer (Audio Feedback)

There are three functions relating to the buzzer on the :GAME Controller.

* playTone:
	This function enables a single frequency note to be played for a specified time period.
	The first argument is the frequency, the second is the length to play in ms:
```
KitronikGameController.playTone(440, 500)
```
* playMelody:
	This function enables a melody from the standard list to be played, either once, or repeated forever (or until the stopMusic function is called).
	The first function is the tune to play, the second (either True or False) is whether to repeat or not:
```
KitronikGameController.playMelody(music.ENTERTAINER, True)
```
* stopMusic:
	This function immediately stops all music output from the specified music pin (Pin 2 for the :GAME Controller):
```
KitronikGameController.stopMusic()
```

## Motor (Haptic Feedback)

The runMotor function will turn the motor on for a period of time specified in ms (the only argument to the function):
```
KitronikGameController.runMotor(500)
```

## License

MIT

## Supported Targets

BBC micro:bit
