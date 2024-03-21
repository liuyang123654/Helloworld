import cv2
import numpy as np
import os
from config import Config

# 绘图展示
def cv_show(img1, img2, img3, img4, img5, img6, img7):
    cv2.imshow("原图片", img_wh(img1))
    cv2.imshow("分割后", img_wh(img2))
    cv2.imshow("区域选择", img_wh(img3))
    cv2.namedWindow('分割区域', cv2.WINDOW_NORMAL)
    cv2.imshow("分割区域", img_wh(img4, 50))
    cv2.imshow("定位高度", img_wh(img5))
    cv2.imshow("刻度位置", img_wh(img6))
    cv2.imshow("刻度识别", img_wh(img7))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 绘图展示
def cv_show1(img1):
    cv2.imshow("image", img_wh(img1))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 绘图展示
def cv_show2(img1, img2):
    cv2.imshow("原图片", img_wh(img1))
    cv2.imshow("分割后", img_wh(img2))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def img_wh(image, width=400):
    height = int(image.shape[0] * width / image.shape[1])
    return cv2.resize(image, (width, height))


## 图像裁切函数
def image_resize(image, crop='bottom'):
    height, width = image.shape[:2]  # 获取图像的高度和宽度
    if crop == 'top':
        # 将图像的上半部分剪切出来
        cropped_image = image[:height // 2, :]
    elif crop == 'bottom':
        # 将图像的下半部分剪切出来
        cropped_image = image[height // 2:height, :]
    else:
        raise ValueError("Invalid value for 'crop' parameter. Use 'top' or 'bottom'.")
    return cropped_image


def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    boundingBoxes = [cv2.boundingRect(c) for c in cnts] #用一个最小的矩形，把找到的形状包起来x,y,h,w
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    return cnts, boundingBoxes


config = Config()
# 读取一个模板图像
img = cv2.imread("C:\\Users\\liuyang\\Desktop\\demo\\moban.png")
#img = cv2.imread(r"./moban.png")
# cv_show('img', img)
# 灰度图
ref = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv_show('ref', ref)
# 二值图像
ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY_INV)[1]
# cv_show('ref', ref)

# 计算轮廓
# cv2.findContours()函数接受的参数为二值图，即黑白的（不是灰度图）,cv2.RETR_EXTERNAL只检测外轮廓，cv2.CHAIN_APPROX_SIMPLE只保留终点坐标
# 返回的list中每个元素都是图像中的一个轮廓

refCnts, hierarchy = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, refCnts, -1, (0, 0, 255), 3)
refCnts = sort_contours(refCnts, method="left-to-right")[0]  # 排序，从左到右，从上到下
digits = {}

# 遍历每一个轮廓
for (i, c) in enumerate(refCnts):
    # 计算外接矩形并且resize成合适大小
    (x, y, w, h) = cv2.boundingRect(c)
    roi = ref[y:y + h, x:x + w]
    roi = cv2.resize(roi, (57, 88))
    # 每一个数字对应每一个模板
    digits[i] = roi



image_file = f"C:\\Users\\liuyang\\Desktop\\{config.image}"
#image_file = f"./{config.image}"
img = cv2.imread(image_file)
imgs = image_resize(img)
ref = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值图像
ref = cv2.threshold(ref, 60, 255, cv2.THRESH_BINARY)[1]
# 图像裁剪：将图像裁剪为原始高度的一半（默认裁剪下半部分）
img_cut = image_resize(ref)
kernel = np.ones((45, 45), np.uint8)
img_cut1 = img_cut.copy()
for i in range(4):
    img_cut1 = cv2.erode(img_cut1, kernel, iterations=1)
for i in range(2):
    img_cut1 = cv2.dilate(img_cut1, kernel, iterations=1)
contours, hierarchy = cv2.findContours(img_cut1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
a = []
for i in range(len(contours)):
    a1 = cv2.contourArea(contours[i])
    a.append(a1)
mya = max(a)
d = []
for i in range(len(contours)):
    if cv2.contourArea(contours[i]) > mya / 10:
        d.append(contours[i])
mask = np.zeros(img_cut.shape, np.uint8)
im1 = cv2.drawContours(mask, d, -1, 255, -1)
points = cv2.findNonZero(im1)
zuo, you = int(min(points[:, :, 0])), int(max(points[:, :, 0]))
mytop = image_resize(img, crop='top')
height, _ = mytop.shape[:2]
im1 = cv2.rectangle(mytop.copy(), (zuo, 0), (you, height), (0, 255, 0), 30)
im1 = im1[:, zuo:you, :]



im2 = im1[-200:-40, zuo:you-1200, :]
im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
# 二值图像
im2_binary = cv2.threshold(im2_gray, 90, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((5, 5), np.uint8)
closeing = cv2.morphologyEx(im2_binary, cv2.MORPH_CLOSE, kernel, iterations=8)
# 查找轮廓
contours, _ = cv2.findContours(closeing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    area = cv2.contourArea(contour)
    x,y,w,h = cv2.boundingRect(contour)
    rect_area = w*h
    extent = float(area)/rect_area
    if extent >= 0.9:
        mycontour = contour
        break
im3 = cv2.drawContours(im2.copy(), [mycontour], 0, (255,0,0), 8)
leftmost = tuple(mycontour[mycontour[:,:,0].argmin()][0])
rightmost = tuple(mycontour[mycontour[:,:,0].argmax()][0])
cv2.rectangle(im3, leftmost, rightmost, (0, 255, 0), 100)
x1, x2 = leftmost[0], rightmost[0]
im4 = im1[:, x1+zuo-10:x2+zuo+10]

im5 = im1.copy()
im6 = im5.copy()
im5[:, x1+zuo-10:x2+zuo+5] = 255
im5_gray = cv2.cvtColor(im5, cv2.COLOR_BGR2GRAY)
im5_binary = cv2.threshold(im5_gray, 90, 255, cv2.THRESH_BINARY_INV)[1]
pixelpoints = cv2.findNonZero(im5_binary)
myheighter = int(min(pixelpoints[:, :, 1]))
cv2.line(im6, (0, myheighter), (im5.shape[1], myheighter), (0, 0, 255), 20)

im7 = im4.copy()
im8 = im7.copy()[myheighter-1:myheighter+80, :]
cv2.line(im7, (0, myheighter), (im7.shape[1], myheighter), (0, 0, 255), 20)

im8_gray = cv2.cvtColor(im8, cv2.COLOR_BGR2GRAY)
im8_binary = cv2.threshold(im8_gray, 120, 255, cv2.THRESH_BINARY_INV)[1]

im8_contours, _ = cv2.findContours(im8_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
a = []
for i in range(len(im8_contours)):
    a1 = cv2.contourArea(im8_contours[i])
    a.append(a1)
mya = max(a)
d = []
for i in range(len(im8_contours)):
    if cv2.contourArea(im8_contours[i]) < mya / 4:
        d.append(im8_contours[i])
im8_mask = np.zeros(im8_binary.shape, np.uint8)
im8_mask = cv2.drawContours(im8_mask, d, -1, 255, -1)

rectkernel = np.ones((3, 3), np.uint8)
im8_mask1 = cv2.morphologyEx(im8_mask, cv2.MORPH_CLOSE, rectkernel, iterations=5)

im8_mask1_contours, _ = cv2.findContours(im8_mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
a = []
for i in range(len(im8_mask1_contours)):
    a1 = cv2.contourArea(im8_mask1_contours[i])
    a.append(a1)
mya = max(a)
d = []
for i in range(len(im8_mask1_contours)):
    if cv2.contourArea(im8_mask1_contours[i]) == mya:
        d.append(im8_mask1_contours[i])
im8_mask2 = np.zeros(im8_mask1.shape, np.uint8)
im8_mask2 = cv2.drawContours(im8_mask2, d, -1, 255, -1)
pixelpoints = cv2.findNonZero(im8_mask2)
x1 = int(min(pixelpoints[:, :, 0]))
y1 = int(min(pixelpoints[:, :, 1]))
x2 = int(max(pixelpoints[:, :, 0]))
y2 = int(max(pixelpoints[:, :, 1]))
cv2.rectangle(im8, (x1, y1), (x2, y2), (0, 0, 255), 2)

im9 = im8[y1+5:y2-1, x1+5:x2-1]
im9_gray = cv2.cvtColor(im9, cv2.COLOR_BGR2GRAY)
im9_binary = cv2.threshold(im9_gray, 120, 255, cv2.THRESH_BINARY_INV)[1]

im9_binary_contours, _ = cv2.findContours(im9_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(len(im9_binary_contours))
groupOutput = []
im9_binary_contours = sort_contours(im9_binary_contours, method="left-to-right")[0]  # 排序，从左到右，从上到下
for c in im9_binary_contours:
    # 找到当前数值的轮廓，resize成合适的的大小
    (x, y, w, h) = cv2.boundingRect(c)
    roi = im9_binary[y:y + h, x:x + w]
    roi = cv2.resize(roi, (57, 88))
    # cv_show1(roi)

    # 计算匹配得分
    scores = []
    # 在模板中计算每一个得分
    for (digit, digitROI) in digits.items():
        # 模板匹配
        result = cv2.matchTemplate(roi, digitROI, cv2.TM_CCOEFF)
        (_, score, _, _) = cv2.minMaxLoc(result)
        scores.append(score)
    # 得到最合适的数字
    groupOutput.append(str(np.argmax(scores)))
print("".join(groupOutput))
cv2.putText(img, "".join(groupOutput), (500, 500),
            cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 255), 20)
# cv_show2(im9, im9_binary)
# cv_show(img, im1, im3, im4, im6, im8, im8_mask)