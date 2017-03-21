import cv2
import subprocess
camera = cv2.VideoCapture(0)
prevImage = None

def getImage():
	retval, image = camera.read()
	return image

def set(resolution=False, exposure=False, gain=False, contrast=False):
	settingStr = "/usr/bin/v4l2-ctl -d /dev/video0"
	if resolution:
		settingStr += " --set-fmt-video=width={},height={}".format(resolution[0], resolution[1])
	if exposure:
		settingStr += " -c exposure_auto=1 -c exposure_auto_priority=0 -c exposure_absolute={}".format(exposure)
	if gain:
		settingStr += " -c gain={}".format(gain)
	if contrast:
		settingStr += " -c contrast={}".format(contrast)
	subprocess.call(settingStr, shell=True)



def findXValue():
	image = getImage()
	height, width, depth = image.shape
	diffs = range(10)
	for i in range(height):
		for j in range(width):
			diff = 0
			for i in range(0, 3)
				diff += abs(image[i, j][i] - prevImage[i, j][i])
