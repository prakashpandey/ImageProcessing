import cv2
import numpy as np

def translate(image, x, y):
    """Shift image in X,Y direction
    Args: 
        image:  the image we are going to translate
        x:  the number of pixels that we are going to shift along the x-axis
        y:  the number of pixels that we are going to shift along the y-axis
    Returns:
        (cv2 image): translated/shifted image    
    """
    #Shift matrix
    M = np.float32([[1, 0, x], [1, 0, y]])
    #Dimensions of shifted image
    shape = (image.shape[1], image.shape[0])
    shifted = cv2.warpAffine(image, M, shape)
    
    return shifted

def rotate(image, angle, center = None, scale = 1.0):
    """Rotate image to a given coordinate
    Args:
        image:  the image we are going to rotate
        angle:  the angle that we are going to rotate image
        center: the point which you want to rotate image 
        scale:  image zoom factor
    """
    (h, w) = image[0:2]
    
    if center is None:
        center = (h // 2, w // 2)    

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    
    return rotated

def resize(image, width = None, height = None, interpolation = cv2.INTER_AREA):
    """
    Resize an image. 
    'height' is only considered for calculating resize factor if 'width' is None
    Args: 
        image (cv2 image):  the image we are going to resize
        width (int):  define width of resized imaged
        height (int): define width of resized imaged
        interpolation (cv2.RESIZE_ALGO):  algorithm used for resizing image
    
    Returns:
        cv2 image: the resized image    
    """
    dim = None
    (h, w) = image.shape[0:2]
    
    if width is None and height is None:
        print("width and height parameter for resizing image is None. Hence returning origional image.")
        return image

    if width is None:
        #Calculate ratio
        r = height / float(h)
        #resized width
        r_w = int(w * r)
        dim = (r_w, height)
    else:
        #Calculate ratio
        r = width / float(w)
        #resized height
        r_h = int(h * r)
        dim = (width, r_h)   

    resized = cv2.resize(image, dim, interpolation = interpolation) 
    
    return resized     

def center(image):
    """
    Find coordinate of center of an image
    Args:
        image: numpy compatible matrix 
    Returns:
        int (cX, cY): int coordinates of center of an image        
    """
    cX = image.shape[1] // 2
    cY = image.shape[0] // 2
    return (cX, cY)   


def mask(image, start, end):
    """
    Mask can be used to crop an image or remove parts of image which you are not intrested in.
    Mask will keep the image of dimension start * end and remove other image content.

    Args:
        image: numpy compatible array
        start: start coordinate 
        end: end coordinate 

    Returns:
        image of same dimension as input image with content removed other than area under (start * end)         
    """
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mask, start, end, 255, -1)
    masked = cv2.bitwise_and(image, image, mask = mask)
    return masked  

def crop(image, start, end):
    """
    Crop an image.

    Args:
    image: the image to be cropped
    start : start coordinate of crop area e.g (x, y)
    end : end coordinate of crop area e.g (x, y)

    Returns:
        image of dimension area (start * end) 
    """
    (x, y) = start
    (x_, y_) = end
    croped = image[y:y_, x:x_]  
    return croped

def split(image):
    #RA: Review again
    #Confusion: it should be (b, g, r) or (r, g, b) 
    """
    Split image in component colors [Blue, Green, Red].

    Args:
    image: the image to be splited

    Returns:
        (r, g, b) : Blue, green and red component of an image
    """
    (r, g, b) = cv2.split(image)
    return (r, g, b)

def get_channel(image, channel):
    #RA: Review again
    #Confusion: it should be (b, g, r) or (r, g, b)
    """
    Get a given image channel component.

    Channels: ["blue", "green", "red"]

    Args:
    image: the image to be splited

    Returns:
        given channel component of an image
    """
    (r, g, b) = cv2.split(image)

    channel = channel.lower()
    if channel == "blue":
        return b
    elif channel == "green":
        return g
    elif channel == "red":
        return r
    else:
        return None   

def greyscale(image):
    """
    Convert the given image into greyscale.

    Args:
    image: the image to be greyscaled

    Returns:
        greyscaled image
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


if __name__ == "__main__":
    print("I am main")