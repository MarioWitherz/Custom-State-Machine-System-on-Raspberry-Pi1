"""
button2.py - Handles BUTTON_2 input
AI-assisted code: Used AI to help structure this button input handler with debounce logic
"""

import RPi.GPIO as GPIO
import time

BUTTON_2 = 6
last2 = True

def init_button2():
    """Initialize BUTTON_2 pin"""
    GPIO.setup(BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_button2(current_state):
    """
    Check if BUTTON_2 was pressed with debounce logic
    Returns new state if transition should occur
    AI suggested this debounce logic; adapted for button input
    """
    global last2
    
    b2 = GPIO.input(BUTTON_2)
    
    # Button pressed (LOW) with debounce check
    if not b2 and last2:
        last2 = b2
        # BUTTON_2 transitions from "hostile" to "explode"
        if current_state == "hostile":
            return "explode"
    
    last2 = b2
    return None

def cleanup_button2():
    """Clean up BUTTON_2 pin"""
    GPIO.cleanup(BUTTON_2)
