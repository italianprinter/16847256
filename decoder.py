from PIL import Image
import stepic

image = Image.open("encrypted.png")

hidden_text = stepic.decode(image)

print("Encrypter text:", hidden_text)

input("Press enter to exit...")
