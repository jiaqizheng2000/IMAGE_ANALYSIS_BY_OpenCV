import cv2
import numpy as np
import pandas as pd
h_coefficient = 0.25
height_all_for_all=[]
height_all_for_one = []
height_full=[1541,1502,1527,1526,1523,1500,1527,1511,1556,1568,1547,1517]
counts=0

def drawMyContours(winName, image, contours, draw_on_blank):
    #    return image after plotting contours
    if draw_on_blank: # white as base color
        temp = np.ones(image.shape, dtype=np.uint8) * 255
        cv2.drawContours(temp, contours, -1, (0, 0, 0), 2)
    else:
        temp = image.copy()
        cv2.drawContours(temp, contours, -1, (0, 0, 255), 2)
    # cv2.imshow(winName, temp)
    # cv2.waitKey()

def get_height_for_single_tube(contours):
    global counts
    if len(contours)>1:
        h=[]
        for i in range(len(contours)):
            rect= cv2.minAreaRect(contours[i])
            box= cv2.boxPoints(rect)
            box = np.int0(box)
            h0=(1 / h_coefficient) * (abs(box[0][1] - box[2][1]))
            h.append(round(h0/height_full[i],4))
            print(box)
        height_all_for_one.append(max(h))
    elif len(contours)==0:
        print("this pipe is empty")
        height_all_for_one.append("0")
    else:
        rect = cv2.minAreaRect(contours[0])
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        print(box)
        h=(1/h_coefficient)*(abs(box[0][1]-box[2][1]))
        height_all_for_one.append(round(h/height_full[counts],4))

    counts+=1
    counts%=11

def img_height_get(image):
    # resize image
    print(image.shape)
    height, width, channel = image.shape
    image = cv2.resize(image, (int(1 * width), int(h_coefficient * height)), interpolation=cv2.INTER_CUBIC)
    # cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    # cv2.imshow("original", image)
    # cv2.waitKey()

    #extract red part
    lower_red = np.array([160, 60, 60])
    upper_red = np.array([180, 255, 255])

    lower_red2 = np.array([0, 60, 60])
    upper_red2 = np.array([10, 255, 255])  # thers is two ranges of red

    # change to hsv model
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask_r = cv2.inRange(hsv, lower_red, upper_red)
    mask_r2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask_r + mask_r2
    # cv2.imshow("red_part", mask)
    # cv2.waitKey()

    #image processing
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 3))
    mask = cv2.erode(mask, kernel, 17)
    mask = cv2.dilate(mask, kernel)
    mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    mask  = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask = cv2.GaussianBlur(mask, (9, 3), 0)
    mask = cv2.medianBlur(mask,5)
    # cv2.imshow("image_process", mask)
    # cv2.waitKey()

    #find coutours
    # contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    print("find", len(contours), "contours")
    final=cv2.drawContours(image,contours,0,255,cv2.FILLED)
    # cv2.imshow("final",final)
    # cv2.waitKey()

    #draw contour
    drawMyContours("countours",image,contours,True)
    #get_height of one tube
    get_height_for_single_tube(contours)

def one_image_processing_Evap(filename):
    img = cv2.imread(filename)
    height,width=img.shape[:2]
    center=(width/2,height/2)
    rotate_matrix=cv2.getRotationMatrix2D(center=center,angle=5,scale=1)
    rotated_image= cv2.warpAffine(img,M=rotate_matrix,dsize=(width,height))

    cropped_image =[
        img[397:1938, 1292:1343],
        img[403:1905, 1493:1543],
        img[376:1903, 1609:1684],
        img[403:1929, 1708:1809],
        img[397:1923, 1817:1937],
        img[473:1973, 1942:2030],
        img[411:1938, 2060:2173],
        rotated_image[414:1970, 2206:2266],
        rotated_image[417:1985, 2302:2369],
        rotated_image[391:1938, 2414:2482],
        rotated_image[403:1920, 2527:2583],
    ]
    for i in range(11):
        img_height_get(cropped_image[i])

    global height_all_for_one
    height_all_for_all.append(height_all_for_one)
    height_all_for_one=[]

def to_csv_Evap(store_path):
    df=pd.DataFrame(height_all_for_all)
    df.to_csv(store_path)