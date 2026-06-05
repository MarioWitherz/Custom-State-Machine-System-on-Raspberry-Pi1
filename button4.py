"""
button4.py - Handles BUTTON_4 input
AI-assisted code: Used AI to help structure this button input handler with debounce logic
"""

import RPi.GPIO as GPIO
import time

BUTTON_4 = 19
last4 = True

def init_button4():
    """Initialize BUTTON_4 pin"""
    GPIO.setup(BUTTON_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_button4(current_state):
    """
    Check if BUTTON_4 was pressed with debounce logic
    Returns new state if transition should occur
    AI suggested this debounce logic; adapted for button input
    """
    global last4
    
    b4 = GPIO.input(BUTTON_4)
    
    # Button pressed (LOW) with debounce check
    if not b4 and last4:
        last4 = b4
        # BUTTON_4 transitions from "idle" or "hostile" to "explode"
        if current_state in ("idle", "hostile"):
            return "explode"
    
    last4 = b4
    return None

def cleanup_button4():
    """Clean up BUTTON_4 pin"""
    GPIO.cleanup(BUTTON_4)
