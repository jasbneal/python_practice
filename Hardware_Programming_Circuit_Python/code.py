from adafruit_circuitplayground.express import cpx
import time

# cpx stands for Circuit Playground Express

def show_all_red_LED():
    cpx.pixels.fill( (255, 0, 0))
    # the cpx.pixels.fill() function changes the colors of the LED lights
    # (the values are (red, green, blue) stored as a tuple meaning that the
    # order is important)

def turn_off_LED():
    cpx.pixels.fill( (0, 0, 0) )

def show_5_white_LED():
    for i in range(10):
        if (i % 2) == 0:
            cpx.pixels[i] = (255, 255, 255)

def show_rainbow_LED():
    cpx.pixels[0] = (255, 0, 0)
    cpx.pixels[1] = (255, 85, 0)
    cpx.pixels[2] = (255, 255, 0)
    cpx.pixels[3] = (0, 255, 0)
    cpx.pixels[4] = (34, 139, 34)
    cpx.pixels[5] = (0, 255, 255)
    cpx.pixels[6] = (0, 0, 255)
    cpx.pixels[7] = (0, 0, 139)
    cpx.pixels[8] = (255, 0, 255)
    cpx.pixels[9] = (75, 0, 130)

def switch_control_D13():
# controls the red D13 LED light by the switch (left=true and right=false)    
    if cpx.switch:
        cpx.red_led = True
    else:
        cpx.red_led = False

def button_control_LED():
    if cpx.button_a:
        cpx.pixels[2] = (255, 255, 255)
    elif cpx.button_b:
        cpx.pixels[7] = (0, 255, 0)
    else:
        cpx.pixels.fill( (0, 0, 0))

def bike_light():
    if cpx.switch:
        show_rainbow_LED()
        time.sleep(0.5)
        turn_off_LED()
        time.sleep(0.5)
    else:
        turn_off_LED()



while True:
    # run desired function(s) indefinitely
    bike_light()
    