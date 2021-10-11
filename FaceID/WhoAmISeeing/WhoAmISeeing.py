import cv2
import pyfiglet

fig = pyfiglet.Figlet(font='standard')
print(fig.renderText('I am seeing you'))

camera = cv2.VideoCapture(0)
for i in range(5):
    return_value, image = camera.read()
    cv2.imwrite('WhoAmISeeing'+str(i)+'.png', image)
del(camera)