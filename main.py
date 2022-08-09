OLED.init(128, 64)

def on_forever():
    OLED.clear()
    OLED.write_string_new_line("Dust (ug/m3)")
    OLED.write_num_new_line(Environment.read_dust(DigitalPin.P13, AnalogPin.P1))
    basic.pause(60000)
basic.forever(on_forever)
