# ImageProcessing
Various utilities useful in image processing and computer vision projects

### crop
crop an image.

```
start = (200, 0)
end = (700, 600)
croped = utils.crop(image, start, end)
```

### mask
Mask can be used to crop an image or remove parts of image which you are not intrested in.
Mask will keep the image of dimension start * end and remove other image content.

```
start = (200, 0)
end = (700, 600)
masked = utils.mask(image, start, end)
```

### center
Find coordinate of center of an image

```
image = cv2.imread("my_image.jpg")
(x, y) = utils.center(image)
```

### resize
Resize an image while keeping its aspect ratio. 

'height' is only considered for calculating resize factor if 'width' is None

```
image = cv2.imread("my_image.jpg")

#using width
resized = utils.resize(image, width=200, inter=cv2.INTER_AREA)

#using height
resized = utils.resize(image, height=200, inter=cv2.INTER_AREA)

```

### rotate
Rotate image to a given coordinate

```
image = cv2.imread("my_image.jpg")
rotated = utils.rotate(image, 30)
```

### translate
Shift image in X,Y direction

```
image = cv2.imread("my_image.jpg")
shifted = utils.translate(image, 0, -10)
```

### split
Split image in component colors [Blue, Green, Red]

```
image = cv2.imread("my_image.jpg")
(r, g, b) = utils.split(image)
```

### get_channel
Get a given image channel component.

```
image = cv2.imread("my_image.jpg")

b = utils.get_channel(image, "blue")
g = utils.get_channel(image, "green")
r = utils.get_channel(image, "red")
``` 

### greyscale
Convert the given image into greyscale.

```
image = cv2.imread("my_image.jpg")
greyscaled = utils.greyscale(image)
```

# Library used
```cv2```
```numpy```

### License
You can use this software for commercial as well as non-commercial purpose/purposes, the way you want and without conditions of any kind.

Please visit [LICENSE.md](LICENSE.md) for more details.

### How to contribute
Please feel free to contribute to this project. You can contact me using below details.

### Contact author
- E-Mail : pcpandey@mail.com.
- Twitter : [Prakash Pandey](http://www.twitter.com/pandaypc)
