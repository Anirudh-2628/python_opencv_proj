#YOU NEED TO PLACE YOUR IMAGE IN THE FOLDER WHERE THE PYTHON FILE IS PLACED AND RENAME THE IMAGE IS sample.png



import cv2
import numpy as np


circles = np.zeros((4,2), np.int0)

counter = 0



def mousePoints(events,x,y,flags,params):
    global counter
    if events==cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter + 1
        print(circles)


img = cv2.imread("sample.png")


while True:
    if counter == 4:
        width, height = 250,350

        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

        matrix = cv2.getPerspectiveTransform(pts1, pts2)

        output = cv2.warpPerspective(img, matrix, (width, height))

        cv2.imshow("output image", output)

    for x in range(0, 4):
        cv2.circle(img, (int(circles[x][0]), int(circles[x][1])),3, (0, 0, 255), cv2.FILLED)
    cv2.imshow("output", img)
    cv2.setMouseCallback("output", mousePoints)
    cv2.waitKey(1)








    
