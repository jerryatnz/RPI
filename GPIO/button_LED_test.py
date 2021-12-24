
from gpiozero import LED
from gpiozero import Button
from time import sleep

button = Button(6)
led_y = LED(21)
led_b = LED(26)

while True:
    button.wait_for_press()
    led_y.on()
    led_b.off()
    sleep(0.5)
    led_y.off()
    led_b.on()
    sleep(0.5)

