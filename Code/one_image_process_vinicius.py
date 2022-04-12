import cv2
import numpy as np
import pandas as pd
h_coefficient = 0.25
height_all_for_all=[]
height_all_for_one = []
height_average=2226.0

def drawMyContours(winName, image, contours, draw_on_blank):
    # cv2.drawContours(image, contours, index, color, line_width)
    # 输入参数：
    # image:与原始图像大小相同的画布图像（也可以为原始图像）
    # contours：轮廓（python列表）
    # index：轮廓的索引（当设置为-1时，绘制所有轮廓）
    # color：线条颜色，
    # line_width：线条粗细
    # 返回绘制了轮廓的图像image
    if draw_on_blank: # 在白底上绘制轮廓
        temp = np.ones(image.shape, dtype=np.uint8) * 255
        cv2.drawContours(temp, contours, -1, (0, 0, 0), 2)
    else:
        temp = image.copy()
        cv2.drawContours(temp, contours, -1, (0, 0, 255), 2)
    # cv2.imshow(winName, temp)
    # cv2.waitKey()

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

    # get x,y
    if len(contours)>1:
        h=[]
        for i in range(len(contours)):
            rect= cv2.minAreaRect(contours[i])
            box= cv2.boxPoints(rect)
            box = np.int0(box)
            h0=(1 / h_coefficient) * (abs(box[0][1] - box[2][1]))
            h.append(h0/height_average)
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
        height_all_for_one.append(h/height_average)


def one_image_processing_vincius(filename):
    img = cv2.imread(filename)
    cropped_image1 = img[379:2675, 1202:1311]
    cropped_image2 = img[368:2594, 1533:1654]
    cropped_image3 = img[379:2579, 1706:1829]
    cropped_image4 = img[383:2590, 1868:1970]
    cropped_image5 = img[391:2606, 2027:2130]
    cropped_image6 = img[490:2671, 2243:2340]
    cropped_image7 = img[387:2602, 2372:2483]
    cropped_image8 = img[617:2870, 2504:2621]
    cropped_image9 = img[418:2671, 2716:2779]
    cropped_image10 = img[414:2632, 2897:2958]
    cropped_image11 = img[410:2632, 3049:3096]

    img_height_get(cropped_image1)
    img_height_get(cropped_image2)
    img_height_get(cropped_image3)
    img_height_get(cropped_image4)
    img_height_get(cropped_image5)
    img_height_get(cropped_image6)
    img_height_get(cropped_image7)
    img_height_get(cropped_image8)
    img_height_get(cropped_image9)
    img_height_get(cropped_image10)
    img_height_get(cropped_image11)

    global height_all_for_one
    height_all_for_all.append(height_all_for_one)
    height_all_for_one=[]

def to_csv_vinicius(store_path):
    df=pd.DataFrame(height_all_for_all)
    df.to_csv(store_path)
