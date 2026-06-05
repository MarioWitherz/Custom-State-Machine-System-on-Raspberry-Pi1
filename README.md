
# Custom-State-Machine-System-on-Raspberry-Pi1
A place to store my files

Project Overview

This project is a Raspberry Pi GPIO-based state machine programmed in Python using the RPi.GPIO library. It uses four push buttons as inputs and two LEDs as outputs to represent different system states. The program continuously monitors button presses and updates the system's status based on predefined rules.

The project demonstrates how physical inputs can be used to control a state-driven system, making it a useful example for learning GPIO programming, hardware interfacing, and event-based logic on the Raspberry Pi.

Features
Four push-button inputs connected to GPIO pins.
Two LED indicators that display the current state of the system.
State management using a simple finite state machine.
Edge detection logic to ensure actions only occur when a button is first pressed.
Continuous monitoring loop with debouncing through timed polling.
Safe program termination using exception handling.
How It Works

When the program starts, the system is placed in an idle state. In this state, both LEDs remain off.

Pressing Button 1 changes the system from idle to a hostile state. When this happens, the Hostile LED turns on to indicate the state change.

While the system is in the hostile state, pressing Button 2 or Button 3 transitions the system into the explode state. Once the explode state is reached, the Explode LED turns on to show that the state has changed.

Button 4 acts as a direct trigger and can immediately place the system into the explode state from either the idle or hostile state.

The program keeps track of each button's previous state, allowing it to detect new button presses rather than continuously triggering actions while a button is held down.

Technical Details

The code uses the Raspberry Pi's BCM GPIO numbering scheme and configures all buttons with internal pull-up resistors. Because of this configuration, buttons are normally read as HIGH and become LOW when pressed.

A dedicated set_state() function manages all state transitions and updates the LEDs automatically whenever the system state changes. This helps keep the code organized and makes it easier to add additional states or outputs in the future.

The main loop runs continuously, checking button inputs every 50 milliseconds. This provides responsive input handling while reducing unnecessary CPU usage.
<img width="3024" height="4032" alt="IMG_2399" src="https://github.com/user-attachments/assets/fd01d4c9-3438-4d64-8170-d11a88217b1e" />
