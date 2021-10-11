import cv2
import pyfiglet

fig = pyfiglet.Figlet(font='standard')
print(fig.renderText('Turn Face All Around'))

camera = cv2.VideoCapture(0)
for i in range(200):
    return_value, image = camera.read()
    cv2.imwrite('AutoEnrolledFace\\Face'+str(i)+'.png', image)
del(camera)