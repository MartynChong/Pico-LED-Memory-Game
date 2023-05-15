from machine import Pin
from time import sleep
import neopixel
import random

#Set up LED colours and pin
led = neopixel.NeoPixel(machine.Pin(28), 1)
clear = (0,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 100, 0)
orange = (255, 50, 0)

# Assign buttons
button_pins = [20, 21, 22]  # Pins for buttons 1, 2, and 3 respectively

# Set up buttons as inputs with pull-down resistors
for pin in button_pins:
    machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN)

#Displays a colour on the LED
def display(i):
    if i == 0:
        led[0] = yellow
        led.write()
    elif i == 1:
        led[0] = orange
        led.write()
    elif i == 2:
        led[0] = blue
        led.write()
    elif i == 3:
        led[0] = green
        led.write()
    elif i == 4:
        led[0] = red
        led.write()
    else:
        led[0] = clear
        led.write()
        
#Generate a random sequence of numbers 
def generateSequence(x):
    #write code to generate a random sequence of numbers [0,1,2] of length x

while True:
    print("Welcome to the Memory Game!")
    print("======== Instructions ========")
    print("The goal of the game is to mimic the order of colours that appear.")
    print("After every mimic attempt, a red/green indicator will reveal if you are correct.")
    print("The number of colours increases every round")
    print("LEFT - YELLOW, MIDDLE - ORANGE, RIGHT - BLUE")
    print("=============================")
    print("")
    print("Learn the button colours by tapping them")
    print("Tap the LEFT button three consecutive times to start")
    
    #Starts when user is ready
    button_presses = []
    start = 0
    while start < 3:
        # Write code to count for 3 consecutive left button clicks
    
    print("GAME START")
    sleep(2)
    alive = True
    round = 1
    game = []
    #Runs while user has not lost yet
    while alive:
        print("Round " + str(round))
        
        #Write code to generates colours and displays them

        print("Input your colours")
        input = []
        
        #Write code to let users input their colour options
        
        #Displays success or failure depending on match
        if input == game:
            print("Correct!")
            display(3)
            sleep(0.3)
            display(-1)
            sleep(0.3)
            display(3)
            sleep(0.-1)
            display(-1)
            display(3)
            sleep(0.3)
            display(-1)
            sleep(3)
            round += 1
        else:
            print("Incorrect!")
            display(4)
            sleep(0.3)
            display(-1)
            sleep(0.3)
            display(4)
            sleep(0.3)
            display(-1)
            display(4)
            sleep(0.3)
            display(-1)
            print("======= GAME OVER =======")
            print("You have survived "+str(round)+ " round(s)!")
            alive = False
    break