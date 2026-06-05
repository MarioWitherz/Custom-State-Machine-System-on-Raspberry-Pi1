"""
button3.py - Handles BUTTON_3 input
AI-assisted code: Used AI to help structure this button input handler with debounce logic
"""

import RPi.GPIO as GPIO
import time

BUTTON_3 = 13
last3 = True

def init_button3():
    """Initialize BUTTON_3 pin"""
    GPIO.setup(BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_button3(current_state):
    """
    Check if BUTTON_3 was pressed with debounce logic
    Returns new state if transition should occur
    AI suggested this debounce logic; adapted for button input
    """
    global last3
    
    b3 = GPIO.input(BUTTON_3)
    
    # Button pressed (LOW) with debounce check
    if not b3 and last3:
        last3 = b3
        # BUTTON_3 transitions from "hostile" to "explode"
        if current_state == "hostile":
            return "explode"
    
    last3 = b3
    return None

def cleanup_button3():
    """Clean up BUTTON_3 pin"""
    GPIO.cleanup(BUTTON_3)
