
from gpiozero import LED
from gpiozero import Button
from time import sleep
from threading import Thread

# define physical connections on GPIO
button = Button(6)
led_y = LED(21)
led_b = LED(26)

# define global
mode = 0


def flash_led():
    global mode
    while True:
        if mode == 0:
            led_b.off()
        else:
            period = 1 / mode
            led_b.on()
            sleep(period)
            led_b.off()
            sleep(period)


def detect_button():
    global mode
    while True:
        button.wait_for_press()
        mode = (mode + 1) % 7
        print(f'Button is pushed. Now mode = {mode}.')
        sleep(0.2) # This delay is added for debouncing.


# when button pressed, toggle LED at specified Hz.
worker1 = Thread(target=detect_button, args=())
worker2 = Thread(target=flash_led, args=())
worker1.start()
worker2.start()

