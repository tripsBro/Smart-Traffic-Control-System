import cv2
import numpy as np
import imutils as im

# #==========start the video==================
cap = cv2.VideoCapture('/home/rahul/Videos/smartTraffic/Autonomous Car Driving through heavy City Traffic.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
car_cascade = cv2.CascadeClassifier('cars.xml')
# #==============start the video=============================
while True:
    ret, frame = cap.read()
    frame = im.resize(frame,360,240,cv2.INTER_AREA)
    output = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    # To draw a rectangle in each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 2)


    # _,thresh = cv2.threshold(gray,115,255,cv2.THRESH_BINARY)
    # fgmask = fgbg.apply(thresh)
    # cnts = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,
    #                         cv2.CHAIN_APPROX_SIMPLE)[-2]
    # center = None
    # if len(cnts) > 0:
    #     # find the largest contour in the mask, then use
    #     # it to compute the minimum enclosing circle and
    #     # centroid
    #     c = max(cnts, key=cv2.contourArea)
    #     print "c: ", c, "sh: ", c.shape
    #     ((x, y), radius) = cv2.minEnclosingCircle(c)
    #     M = cv2.moments(c)
    #     if M["m00"]>0:
    #         center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    #         area = cv2.contourArea(c)
    #         print("area", area)
    #
    #         # only proceed if the radius meets a minimum size
    #         if radius > 5:
    #         # draw the circle and centroid on the frame,
    #             cv2.drawContours(output, [c], 0, (0, 0, 255), 1)

    cv2.imshow("lane1", output)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

