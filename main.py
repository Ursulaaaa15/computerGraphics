import numpy as np
import cv2

def draw_line_bresenham(image, x0, y0, x1, y1, color):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1

    if dx > dy:
        err = dx / 2
        while x0 != x1:
            image[y0, x0] = color
            err -= dy
            if err < 0:
                y0 += sy
                err += dx
            x0 += sx
    else:
        err = dy / 2
        while y0 != y1:
            image[y0, x0] = color
            err -= dx
            if err < 0:
                x0 += sx
                err += dy
            
            y0 += sy
    
    image[y0, x0] = color


width = 800
height = 600

image = np.zeros((height, width, 3), dtype=np.uint8)

x0, y0 = 100, 100
x1, y1 = 100, 400

color = (255, 192, 203)

draw_line_bresenham(image, x0, y0, x1, y1, color)

cv2.imshow('Bresenham Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()