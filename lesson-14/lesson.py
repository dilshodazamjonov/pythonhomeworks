from PIL import Image

img = Image.open('photo_2025-04-22_17-03-05.jpg')

print(img.size, img.format, img.mode)

img.show()

img.save("photo_2025-04-22_17-03-05.png") 



resized = img.resize((900, 400))

resized.save("resized.png")


cropped = img.crop((50, 50, 300, 300))
cropped.save("cropped.jpg")

