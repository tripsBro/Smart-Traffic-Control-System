import cv2
import imutils as im
import time


count = 1

def change(Time):
    if Time>5:

        return True
    else:
        return False


def inc():

    global count
    count +=1
    if count>3:
        count = 1
    return count


# #==========start the videos==================
cap1 = cv2.VideoCapture('/home/rahul/Videos/smartTraffic/video1.avi')
cap2 = cv2.VideoCapture('/home/rahul/Videos/smartTraffic/Bangalore Traffic.mp4')
cap3 = cv2.VideoCapture('/home/rahul/Videos/smartTraffic/video2.avi')

# #============== create cascade objects========
fgbg = cv2.createBackgroundSubtractorMOG2()
car_cascade = cv2.CascadeClassifier('cars.xml')

# #===========start timer=========
initTime = time.time()
initialTime = initTime
print "reference time value: ",initialTime

# #==============get continuous frames=============================
while True:

    ret1, lane1 = cap1.read()
    ret2, lane2 = cap2.read()
    ret3, lane3 = cap3.read()

    lane1 = im.resize(lane1, 360, 240, cv2.INTER_AREA)
    lane2 = im.resize(lane2, 360, 240, cv2.INTER_AREA)
    lane3 = im.resize(lane3, 360, 240, cv2.INTER_AREA)

    output1 = lane1.copy()
    output2 = lane2.copy()
    output3 = lane3.copy()

    lane1_gray = cv2.cvtColor(lane1, cv2.COLOR_BGR2GRAY)
    lane2_gray = cv2.cvtColor(lane2, cv2.COLOR_BGR2GRAY)
    lane3_gray = cv2.cvtColor(lane3, cv2.COLOR_BGR2GRAY)

    cars_lane1 = car_cascade.detectMultiScale(lane1_gray, 1.1, 1)
    cars_lane2 = car_cascade.detectMultiScale(lane2_gray, 1.1, 1)
    cars_lane3 = car_cascade.detectMultiScale(lane3_gray, 1.1, 1)

    # create list to count cars in each lane
    l1x = []
    l2x = []
    l3x = []
    # draw rectangle around cars
    for (x, y, w, h) in cars_lane1:
        cv2.rectangle(output1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        l1x.append(x)
    for (x, y, w, h) in cars_lane2:
        cv2.rectangle(output2, (x, y), (x + w, y + h), (0, 0, 255), 2)
        l2x.append(x)
    for (x, y, w, h) in cars_lane3:
        cv2.rectangle(output3, (x, y), (x + w, y + h), (0, 0, 255), 2)
        l3x.append(x)



    # ##--control flow code block---
    currentTime = time.time() - initialTime
    # print "current timer:", int(currentTime)
    if change(currentTime):

        initialTime= time.time()
        # print currentTime

        print "lane %d GO, rest stop"%(inc())
        print "lane1:", len(l1x), "lane2:", len(l2x), "lane3:", len(l3x)
    elif change(currentTime)==False:
        # -----check and compare the number of cars in next lane
        if count==1:
            if len(l2x)>len(l1x):
                dif = len(l2x) - len(l1x)
                if dif > 5:
                    initialTime = time.time()
                    # print currentTime

                    print "lane %d GO, rest stop" % (inc())
                    print "lane1:", len(l1x), "lane2:", len(l2x), "lane3:", len(l3x)



    cv2.imshow("lane1", output1)
    cv2.imshow("lane2", output2)
    cv2.imshow("lane3", output3)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()

# ---trying with contour detection---------

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
# ------------------------------------------------------------------------------------------------



