import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    # Works on Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)

# Reading Videos and Resizing

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow(' Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)