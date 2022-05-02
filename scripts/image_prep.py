import cv2

def image_prep(filename, blur_factor=4, canny_1=100, canny_2=200):    
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)      
    k = (blur_factor,blur_factor)
    img_blur = cv2.blur(img, k)
    edges = cv2.Canny(img_blur, canny_1, canny_2)
    cv2.imwrite("../saved_imgs/blurred_edges.png", edges)    
