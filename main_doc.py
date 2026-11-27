from sense_hat import SenseHat
sense = SenseHat()
from random import choice

replies =  [("Y", (0, 255, 0)), ("N", (255, 0, 0)), ("M", (0, 0, 255))]

sense.show_message('Hi beautiful!', text_colour = (255, 0, 0), scroll_speed=0.67)

while True:
    x,y,z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2:
        reply, colour = choice(replies)
        sense.show_message(reply, text_colour=colour, scroll_speed=0.05)
    else:
        sense.clear()


# #Red for no, green for yes, blue maybe
# "No" == (255, 0, 0)
# "Yes" == (0, 255, 0)
# "Maybe" == (0, 0, 255)

# while True: 
#     acceleration = sense.get_accelerometer_raw()
#     y = abs(acceleration["y"].values)
#     z = abs(acceleration["z"].values)
#     x = abs(acceleration["x"].values)

#     if y > 2 or x > 2 or z > 2:
#         sense.show_message("Hi beautiful!")
#         reply, colour = choice(replies)
#         sense.show_message(reply, text_colour = colour)

#     else:
#         sense.set_pixel(0, 0, 255, 0, 0)
#         sense.clear() 
 