from PIL import Image
import glob

image_list = []
resized_images = []
i=0
for filename in glob.glob('C:\DartBoardHL\\*.jpg'):
    print(filename)
    img = Image.open(filename)
    img = img.rotate(270)
    img = img.resize((1280,720))
    img.save('{}{}{}'.format('C:/DartBoardHL/Resized\\', i, '.jpg'))
    i=i+1
