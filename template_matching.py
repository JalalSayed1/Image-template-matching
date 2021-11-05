import numpy as np
import cv2

#* add the relevant arguments bellow:
FULL_IMAGE_PATH = "" # "PATH OF THE FULL IMAGE"
TEMPLATE_PATH = "" # "PATH OF THE OBJECT TO SEARCH FOR IN IMAGE"

img = cv2.imread(FULL_IMAGE_PATH, 0) # 0 to load as gray scale
template = cv2.imread(TEMPLATE_PATH, 0) # 0 to load as gray scale

img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
template = cv2.resize(template, (0,0), fx=0.3, fy=0.3)
h, w = template.shape # returns (height, width)

# all the methods to detect the template.
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, 
            cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    # matchTemplate(img2, template) returns (w1 - w2 + 1, h1 - h2 +1) where w1 and h1 are the width and height to img2
    result = cv2.matchTemplate(img2, template, method)

    # to return the max/min values (match) and location of that match
    min_value, max_value, min_location, max_location = cv2.minMaxLoc(result)
    print(min_location, max_location)

    # if method is one of these, we need to use the min location. otherwise, max location is better
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_location
    else:
        location = max_location

    bottom_right_location = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right_location, 255, 2)




    cv2.imshow("img", img2)


cv2.waitKey(0)
cv2.destroyAllWindows()

