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