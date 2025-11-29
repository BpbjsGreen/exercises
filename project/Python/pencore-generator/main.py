import cv2
import numpy


def img_resize(image, width_new, height_new):
    height, width = image.shape[0], image.shape[1]
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
    return img_new


# Prepare: Generate input1.jpg with varying brightness levels
img = img_resize(cv2.imread("input1.jpg"), 60, 60)
for beta in range(0, 256, 1):
    img2 = (img * (beta / 256)).clip(0, 255).astype(numpy.uint8)
    cv2.imwrite("img/" + str(beta) + ".jpg", img2)

# Generate
tar = img_resize(cv2.imread("input2.jpg"), 60, 60)
w = tar.shape[1]
h = tar.shape[0]
for xi in range(0, h):
    for xj in range(0, w):
        # Calculate brightness
        brightness = int(
            (int(tar[xi, xj, 0]) + int(tar[xi, xj, 1]) + int(tar[xi, xj, 2])) // 3
        )

        # Merge
        if xj == 0:
            img_now = cv2.imread("img/" + str(brightness) + ".jpg")
        else:
            img_now = numpy.concatenate(
                [img_now, cv2.imread("img/" + str(brightness) + ".jpg")], axis=1
            )

    if xi == 0:
        img_now2 = img_now
    else:
        img_now2 = numpy.concatenate([img_now2, img_now], axis=0)

# Save
cv2.imwrite("output.jpg", img_now2)
