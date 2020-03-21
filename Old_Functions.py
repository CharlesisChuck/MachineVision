

class Old_Functions:

    def display_images(image_list, image_name):
        list_size = len(image_list)
        columns = int(math.sqrt(list_size))
        row = math.ceil(list_size / columns)
        for i in range(list_size):
            plt.subplot(columns, row, i + 1), plt.imshow(image_list[i], 'gray')
            plt.title(image_name[i])
            plt.xticks([]), plt.yticks([])
        cv.waitKey(0)
######################################################################################
    def bead_data_create(self, key_points):
        # generate the list for the bead data to later decide upon
        bead_data = []
        for i in range(len(keypoints)):
            list = [round(keypoints[i].size, 2), round(keypoints[i].pt[0], 2), round(keypoints[i].pt[1], 2)]
            bead_data.append(list)
            # FORMAT: [size,x,y]
        return bead_data
######################################################################################

######################################################################################
    def sort_blobs(Bead_Data):
        BD = sorted(Bead_Data, key=lambda x: x[2], reverse=False)
        return BD
######################################################################################
    def Denoising(image, DS):
        filtered_image = image
        img_size = cv.resize(image, (image.shape[1] // DS, image.shape[0] // DS))
        filtered_image = cv.fastNlMeansDenoising(img_size, h=3, templateWindowSize=20 // DS + 1,
                                                 searchWindowSize=40 // DS + 1)
        return filtered_image

######################################################################################
    def Bit_And(image1, image2):
        img_and = cv.bitwise_and(image2, image1)
        return img_and

######################################################################################
    def Bit_Or(image1, image2):
        img_or = cv.bitwise_or(image2, image1)
        return img_or
######################################################################################

    def Hough_Circles(image,dp,minDist,param1,param2,minRadius,maxRadius):
        circles = []
        try:
            circles = cv.HoughCircles(image, cv.HOUGH_GRADIENT, dp, minDist,
                                    param1=param1,
                                    param2=param2,
                                    minRadius=minRadius,
                                    maxRadius=maxRadius)

            circles = np.uint16(np.around(circles))
        except:
            print("not read")
        return circles
######################################################################################
    def Data_Contours(contours):
        areas = []
        contours_list = []
        contours_location = []
        for contour in contours:
            if (cv.contourArea(contour) > 10 and cv.contourArea(contour) < 100):
                M = cv.moments(contour)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                contours_location.append([cX, cY])
                areas.append(cv.contourArea(contour))
                contours_list.append(cv.convexHull(contour))

        return [areas, contours_list, contours_location]
######################################################################################
    def Find_Contours(im, im_gray):
        ret, thresh = cv.threshold(im_gray, 150, 200, 0)
        contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        x, y = thresh.shape
        arr = np.zeros((x, y, 3), np.uint8)
        return contours
######################################################################################
    def Draw_Contours(contours,im):
        for contour in contours:
            if (cv.contourArea(contour) > 10 and cv.contourArea(contour) < 100):
                cv.drawContours(im, contour, -1, (0, 0, 255), 2)
        cv.drawContours(im, contours, -1, (0, 255, 0), 1)
        return im