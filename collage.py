#24/05/25

import cv2, os
from PIL import Image

#changing the directory as per the image folder
os.chdir('C:\\Users\\Administrator\\Desktop\\open_cv\\images')

path = 'C:\\Users\\Administrator\\Desktop\\open_cv\\images'

totalwidth,totalheight = 0,0

for i in os.listdir('.'):
    image = Image.open(os.path.join(path,i))
    width,height = image.size
    totalwidth +=width 
    totalheight += height
#finding mean
meanwidth = totalwidth//len(os.listdir('.'))
meanheight = totalheight//len(os.listdir('.'))
print(meanwidth)
print(meanheight)

for i in os.listdir('.'):
    image = Image.open(os.path.join(path,i))
    width,height = image.size
    imgResized = image.resize((meanwidth,meanheight),Image.LANCZOS)
    imgResized.save(i)
    print('has been resized')

def vidGenerate():
    file = 'Collage_Player.avi'
    os.chdir('C:\\Users\\Administrator\\Desktop\\open_cv\\images')
    l = []
    for i in os.listdir('.'):
        l.append(i)
    frame = cv2.imread(os.path.join('.',l[0]))
    height,width,layers = frame.shape
    video = cv2.VideoWriter(file,0,1,(width,height))
    for i in l:
        video.write(cv2.imread(os.path.join('.',i)))
    cv2.destroyAllWindows()
    video.release()
vidGenerate()
