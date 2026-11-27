from sense_hat import SenseHat
sense = SenseHat()
from random import choice

acceleration = sense.get_accelerometer_raw()
y = acceleration["y"]
z = acceleration["z"]
x = acceleration["x"]
if y > 2 or x > 2 or z > 2:
 sense.show_message("Hi beautiful!")
 sense.show_letter("Y", (0, 255, 0), scroll_speed = 0.5)
 sense.show_letter("N", (255, 0, 0), scroll_speed = 1.0)
 sense.show_letter("M", (0, 0, 255), scroll_speed = 0.05)

else:
 sense.set_pixel(0, 0, 255, 0, 0)
 sense.clear() 

#Red for no, green for yes, blue maybe
"No" == (255, 0, 0)
"Yes" == (0, 255, 0)
"Maybe" == (0, 0, 255)