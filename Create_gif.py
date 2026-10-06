from PIL import Image
import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png']

first_image = Image.open(filenames[0]).convert("RGB")
size = first_image.size

images = [first_image]

for filename in filenames[1:]:
    image = Image.open(filename).convert("RGB")
    image = image.resize(size)
    images.append(image)

iio.imwrite('team.gif', images, duration=500, loop=0)