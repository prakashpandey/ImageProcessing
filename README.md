# ImageProcessing
Various utility functions required in image processing

### crop
crop an image.

```
start = (200, 0)
end = (700, 600)
croped = crop(image, start, end)
```

### mask
Mask can be used to crop an image or remove parts of image which you are not intrested in.
Mask will keep the image of dimension start * end and remove other image content.

```
start = (200, 0)
end = (700, 600)
masked = mask(image, start, end)
```

### center
Find coordinate of center of an image

```
image = cv2.imread("my_image.jpg")
(x, y) = center(image)
```

### resize
Resize an image while keeping its aspect ratio. 

'height' is only considered for calculating resize factor if 'width' is None

```
image = cv2.imread("my_image.jpg")

#using width
resized = resize(image, width=200, inter=cv2.INTER_AREA)

#using height
resized = resize(image, height=200, inter=cv2.INTER_AREA)

```

### rotate
Rotate image to a given coordinate

```
image = cv2.imread("my_image.jpg")
rotated = rotate(image, 30)
```

### translate
Shift image in X,Y direction

```
image = cv2.imread("my_image.jpg")
shifted = imutils.translate(image, 0, -10)
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
