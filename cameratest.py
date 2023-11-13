from picamera2 import Picamera2
#test to capture an image and save it as a test jpg
picam2 = Picamera2()
picam2.start_and_capture_file("test.jpg")