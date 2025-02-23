from PIL import Image
import glob

image_list = []
resized_images = []

for filename in glob.glob('C:\\ProjectsFolder\\RocketOpenCv\\opencv\\build\\x64\\vc15\\bin\\Rocket\\PiData3\\*.jpg'):
    print(filename)
    img = Image.open(filename)
    #img = img.rotate(270)
    image_list.append(img)

for image in image_list:
    image = image.resize((1728,972))
    resized_images.append(image)
    

for (i, new) in enumerate(resized_images):
    new.save('{}{}{}'.format('C:\\ProjectsFolder\\RocketOpenCv\\opencv\\build\\x64\\vc15\\bin\\Rocket\\PiData3\\Resized\\', i+1, '.jpg'))

