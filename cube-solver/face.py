import cv2
from matplotlib import pyplot as plt
# cv2.imshow('image',img)
# cv2.waitKey(0) # wait indefinitely for keyboard event
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

face = [] # 3x3

while True:
    # ret, frame = cap.read() 
    frame = cv2.imread("cube.jpg", cv2.IMREAD_COLOR)
    cv2.imshow('frame', frame)

    edges = cv2.Canny(frame, 100, 200)
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows(0)