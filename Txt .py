
cat > matrix_video.py <<'PY'
import cv2
import os
import time

video = cv2.VideoCapture("Barsaat - Banjaare .mp4")
chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&"

if not video.isOpened():
    print("Video file not found!")
    quit()

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.resize(frame, (80, 30))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    os.system("clear")

    for row in gray:
        line = ""
        for pixel in row:
            index = int(pixel / 255 * (len(chars) - 1))
            line += chars[index]
        print("\033[92m" + line + "\033[0m")

    time.sleep(0.04)

video.release()
PY
