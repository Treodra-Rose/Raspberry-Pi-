from sense_hat import SenseHat
sense = SenseHat()
from random import choice

acceleration = sense.get_accelerometer_raw()
y = acceleration["y"].values
z = acceleration["z"].values
x = acceleration["x"].values

replies =  [("Y", (0, 255, 0)), ("N", (255, 0, 0)), ("M", (0, 0, 255))]

if y > 2 or x > 2 or z > 2:
 sense.show_message("Hi beautiful!")
 reply, colour = choice(replies)
 sense.show_message(reply)

else:
 sense.set_pixel(0, 0, 255, 0, 0)
 sense.clear() 
 
#Red for no, green for yes, blue maybe
"No" == (255, 0, 0)
"Yes" == (0, 255, 0)
"Maybe" == (0, 0, 255)