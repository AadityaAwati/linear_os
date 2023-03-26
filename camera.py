import cv2
import datetime

camera = cv2.VideoCapture(0)

closed = False
while True:

    return_value, image = camera.read()
    cv2.imshow('image', image)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        time_stamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        cv2.imwrite(f'{time_stamp}.jpg', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        closed = True
        break


camera.release()
cv2.destroyAllWindows()
