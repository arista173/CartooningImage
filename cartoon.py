import cv2

filename = input("Input the file name (ex: image.jpg): ")

img = cv2.imread(filename)
if img is None:
    print(f"Image '{filename}' not found or cannot be read")
    exit()

g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
g = cv2.medianBlur(g, 5)

e = cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

c = cv2.bilateralFilter(img, 9, 250, 250)

cartoon = cv2.bitwise_and(c, c, mask = e)

output_name = input("Input the file name for the result (ex: result.jpg): ")

success = cv2.imwrite(output_name, cartoon)

if success:
    print(f"Picture has been saved as {output_name}")
else:
    print(f"Failed to save {output_name}")

cv2.imshow("Cartoon - Press any key to close", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Program finished.")