import cv2

img_path = 'D:/College/Fall2023/DeepLearning/yolo-g8/data/test_image.jpg'
image = cv2.imread(img_path)
if image is None:
    print("Error loading image")
else:
    cv2.imshow('Test Window', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
