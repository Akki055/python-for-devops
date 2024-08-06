# if want to read the valur first have to store the value by using command export

import os

print(os.getenv("password"))

print(os.getenv("apitoken"))

# The better way to write this is

password = (os.getenv("password"))
