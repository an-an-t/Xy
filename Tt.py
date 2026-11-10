
import cv2
import os
import time
import shutil
import subprocess

filename = "Barsaat - Banjaare .mp4"

# Start original audio
audio = subprocess.Popen([
    "ffplay", "-nodisp", "-autoexit",
    "-loglevel", "quiet", filename
])

video = cv2.VideoCapture(filename)

chars = " .:-=+*#%@"

if not video.isOpened():
    print("Video not found!")
    audio.terminate()
    quit()

fps = video.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 24

cols, rows = shutil.get_terminal_size()
width = max(40, cols - 1)
height = min(rows - 2, int(width * 9 / 32))

print("\033[2J\033[H")

try:
    while True:
        start = time.time()

        ret, frame = video.read()
        if not ret:
            break

        frame = cv2.resize(frame, (width, height))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        output = []

        for row in gray:
            line = ""
            for pixel in row:
                index = int(pixel / 255 * (len(chars) - 1))
                line += chars[index]
            output.append(line)

        print("\033[H\033[92m" + "\n".join(output) + "\033[0m",
              end="", flush=True)

        delay = max(0, (1 / fps) - (time.time() - start))
        time.sleep(delay)

except KeyboardInterrupt:
    pass

finally:
    video.release()
    audio.terminate()
    print("\033[0m\033[?25h")
  
