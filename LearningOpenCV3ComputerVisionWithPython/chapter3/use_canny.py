# -*- coding: utf-8 -*-

import cv2
import numpy as np


img = cv2.imread('../beauty.jpg', 0)
cv2.imwrite('canny.jpg', cv2.Canny(img, 200, 300))
cv2.waitKey()
cv2.destroyAllWindows()