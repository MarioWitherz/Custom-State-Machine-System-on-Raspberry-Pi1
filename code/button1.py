"""
button1.py - Handles BUTTON_1 input
AI-assisted code: Used AI to help structure this button input handler with debounce logic
"""

import RPi.GPIO as GPIO
import time

BUTTON_1 = 5
last1 = True

def init_button1():
    """Initialize BUTTON_1 pin"""
    GPIO.setup(BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_button1(current_state):
    """
    Check if BUTTON_1 was pressed with debounce logic
    Returns new state if transition should occur
    AI suggested this debounce logic; adapted for button input
    """
    global last1
    
    b1 = GPIO.input(BUTTON_1)
    
    # Button pressed (LOW) with debounce check
    if not b1 and last1:
        last1 = b1
        # BUTTON_1 transitions from any state to "hostile"
        if current_state != "hostile":
            return "hostile"
    
    last1 = b1
    return None

def cleanup_button1():
    """Clean up BUTTON_1 pin"""
    GPIO.cleanup(BUTTON_1)
