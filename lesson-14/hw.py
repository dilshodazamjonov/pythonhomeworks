import numpy as np
from PIL import Image


# Task 1. Write a Python function that converts a temperature from Fahrenheit to Celsius. Use `numpy.vectorize` to apply this function to an array of temperatures: `[32, 68, 100, 212, 77]`. 
#    - Formula: $C = (F - 32) \times \frac{5}{9}$

def fahrenheit_to_celsius(f):
    return (f-32) * 5 / 9

to_celsius = np.vectorize(fahrenheit_to_celsius)

temps_f = np.array([32, 68, 100, 212, 77])
temps_c = to_celsius(temps_f)

print(temps_c)

# ---

# Task 2. Create a custom function that takes two arguments: a number and a power. Use `numpy.vectorize` to calculate the power for each pair of numbers in two arrays: `[2, 3, 4, 5]` and `[1, 2, 3, 4]`.

def power(num, power):
    return num ** power

to_power = np.vectorize(power)
nums = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])
ans = to_power(nums, powers)
print("Numbers raised to powers:", ans)


# ---

# Task 3. Solve the system of equations using `numpy`:

# $$
# \begin{cases}
# 4x + 5y + 6z = 7 \\
# 3x - y + z = 4 \\
# 2x + y - 2z = 5
# \end{cases}
# $$


matrix = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
values = np.array([7, 4, 5])
res = np.linalg.solve(matrix, values)
print(res)


# ---

# Task 4. Given the electrical circuit equations below, solve for $I_1, I_2, I_3$ (currents in the branches):

# $$
# \begin{cases}
# 10I_1 - 2I_2 + 3I_3 = 12 \\
# -2I_1 + 8I_2 - I_3 = -5 \\
# 3I_1 - I_2 + 6I_3 = 15
# \end{cases}
# $$


currents = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
equation = np.array([12, -5, 15])

result = np.linalg.solve(currents, equation)
print(result)


# ---


# **Image Manipulation with NumPy and PIL**

# Image file: `images/birds.jpg`. Your task is to perform the following image manipulations using the **NumPy** library while leveraging **PIL** for reading and saving the image.

# **Instructions:**

# 1. **Flip the Image**:
#    - Flip the image horizontally and vertically (left-to-right and up-to-down).

# 2. **Add Random Noise**:
#    - Add random noise to the image.

# 3. **Brighten Channels**:
#    - Increase the brightness of the channels (r.g. red channel) by a fixed value (e.g., 40). Clip the values to ensure they stay within the 0 to 255 range.

# 4. **Apply a Mask**:
#    - Mask a rectangular region in the image (e.g., a 100x100 area in the center) by setting all pixel values in this region to black (0, 0, 0).

# **Requirements:**
# - Use the **PIL** module onyl to:
#   - Read the image.
#   - Convert numpy array to image.
#   - Save the modified image back to a file.
# - Perform all manipulations using NumPy functions. Avoid using image editing functions from PIL or other libraries.


# **Bonus Challenge**:
# - Create a function for each manipulation (e.g., `flip_image`, `add_noise`, `brighten_channels`, `apply_mask`) to promote modularity and reusability of code.


def flip_image(img_array):
    """Flip image horizontally and vertically."""
    flipped_h = np.fliplr(img_array)  # horizontal flip
    flipped_v = np.flipud(img_array)  # vertical flip
    return flipped_h, flipped_v

def add_noise(img_array, noise_level=30):
    """Add random noise to image (0-255)."""
    noise = np.random.randint(-noise_level, noise_level+1, img_array.shape, dtype=np.int16)
    noisy_img = np.clip(img_array.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return noisy_img

def brighten_channels(img_array, value=40):
    """Brighten all color channels by a fixed value."""
    brightened = np.clip(img_array.astype(np.int16) + value, 0, 255).astype(np.uint8)
    return brightened

def apply_mask(img_array, mask_size=(100, 100)):
    """Apply a black mask in the center of the image."""
    h, w, _ = img_array.shape
    mask_h, mask_w = mask_size
    y1, y2 = (h - mask_h) // 2, (h + mask_h) // 2
    x1, x2 = (w - mask_w) // 2, (w + mask_w) // 2
    img_array[y1:y2, x1:x2] = [0, 0, 0]
    return img_array

img = Image.open("images/birds.jpg")
img_array = np.array(img)

# 2. Flip
flipped_h, flipped_v = flip_image(img_array)

# 3. Add noise
noisy_img = add_noise(img_array)

# 4. Brighten channels
bright_img = brighten_channels(img_array, 40)

# 5. Apply mask
masked_img = apply_mask(img_array.copy(), (100, 100))

# 6. Convert back to Image and save
Image.fromarray(flipped_h).save("flipped_horizontal.jpg")
Image.fromarray(flipped_v).save("flipped_vertical.jpg")
Image.fromarray(noisy_img).save("noisy.jpg")
Image.fromarray(bright_img).save("brightened.jpg")
Image.fromarray(masked_img).save("masked.jpg")


# ---