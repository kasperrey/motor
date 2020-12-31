def on_button_pressed_a():
    global snelheid
    snelheid += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global snelheid
    snelheid = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global snelheid
    snelheid += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: Image = None
plaatje: Image = None
snelheid = 0
snelheid = 0

def on_forever():
    powerfunctions.connect_ir_led(AnalogPin.P0)
    powerfunctions.set_speed(PowerFunctionsMotor.RED1, snelheid)
    
basic.forever(on_forever)

def on_forever2():
    global sprite, snelheid
    if snelheid >= 4:
        sprite = images.create_big_image("""
            . . . . . . . # . .
            . . . . . . . # # .
            # # # # # # # # # #
            . . . . . . . # # .
            . . . . . . . # . .
            """)
        snelheid += -1
basic.forever(on_forever2)

def on_forever3():
    global plaatje, snelheid
    if snelheid <= 0:
        plaatje = images.create_big_image("""
            . . # . . . . . . .
            . # # . . . . . . .
            # # # # # # # # # #
            . # # . . . . . . .
            . . # . . . . . . .
            """)
        snelheid += 1
basic.forever(on_forever3)
