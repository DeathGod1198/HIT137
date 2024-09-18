import time
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(generated_number)

from PIL import Image
import numpy as np

# Load the image
image = Image.open('chapter1.jpg')

# Convert the image to a NumPy array
image_array = np.array(image)

# The value you want to add to each RGB channel
add_value = generated_number

# Add the value to each channel (R, G, B), ensuring we stay within valid bounds (0-255)
modified_image_array = np.clip(image_array + add_value, 0, 255)

# Convert back to an image
modified_image = Image.fromarray(modified_image_array.astype('uint8'))

# Save or show the modified image
modified_image.save('chapter1out.jpg')
modified_image.show()

from PIL import Image
import numpy as np

# Load the image
image = Image.open('chapter1out.jpg')

# Convert the image to a NumPy array
image_array = np.array(image)

# Extract the red channel
red_channel = image_array[:, :, 0]

# Create a new image array where only the red channel is retained
# Set green and blue channels to 0
new_image_array = np.zeros_like(image_array)
new_image_array[:, :, 0] = red_channel

# Convert back to an image
new_image = Image.fromarray(new_image_array)

# Save or show the new image
new_image.save('new_imager.jpg')
new_image.show()

# Calculate the sum of all red pixel values
red_sum = np.sum(red_channel)

print(f"Sum of all red pixel values: {red_sum}")

