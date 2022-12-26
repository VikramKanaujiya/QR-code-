import pyzbar.pyzbar as pyzbar
import cv2

# Read the image file
image = cv2.imread("D:/DATA/Desktop/New folder/qr_code.png")

# Decode the QR code
decoded = pyzbar.decode(image)

# Print the data contained in the QR code
print(decoded[0].data.decode("utf-8"))
