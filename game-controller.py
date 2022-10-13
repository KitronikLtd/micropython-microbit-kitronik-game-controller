# microbit-module: KitronikGameController@1.0.0
# Copyright (c) Kitronik Ltd 2022. 
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from microbit import *
import music
# Class to drive Kitronik :GAME Controller
class KitronikGameController:
    musicPin = 0
    Up = 0
    Down = 0
    Left = 0
    Right = 0
    Fire_1 = 0
    Fire_2 = 0
    
    # This function will be called when a class instance is created
    def __init__(self):
        self.musicPin = pin2
        self.Up = pin8
        self.Down = pin14
        self.Left = pin12
        self.Right = pin13
        self.Fire_1 = pin15
        self.Fire_2 = pin16
    
    # Determines whether a particular button has been pressed (returns True or False)
    def onButtonPress(self, button):
        if button.read_digital() == 0:
            return True
        else:
            return False

    # Buzzer
    # Play a single frequency tone on the buzzer for a specified length in ms
    def playTone(self, frequency, toneLength):
        music.pitch(frequency, toneLength, self.musicPin, True)
    
    # Play a tune from the standard list on the buzzer (once or forever until stopMusic() is called)
    def playMelody(self, tune, repeat):
        music.play(tune, self.musicPin, False, repeat)
    
    # Stop all music from the buzzer
    def stopMusic(self):
        music.stop(self.musicPin)
    
    # Run Motor for length of time specified in ms
    def runMotor(self, length):
        pin1.write_digital(1)
        sleep(length)
        pin1.write_digital(0)

# Example program to test all :GAME Controller functions
controller = KitronikGameController()
while True:
    
    if controller.onButtonPress(controller.Up) is True:
        display.show(Image.ARROW_N)
    if controller.onButtonPress(controller.Down) is True:
        display.show(Image.ARROW_S)
    if controller.onButtonPress(controller.Left) is True:
        display.show(Image.ARROW_W)
    if controller.onButtonPress(controller.Right) is True:
        display.show(Image.ARROW_E)
    if controller.onButtonPress(controller.Fire_1) is True:
        controller.playTone(440, 500)
    if controller.onButtonPress(controller.Fire_2) is True:
        controller.runMotor(500)
    if button_a.is_pressed():
        controller.playMelody(music.ENTERTAINER, True)
    if button_b.is_pressed():
        controller.stopMusic()
