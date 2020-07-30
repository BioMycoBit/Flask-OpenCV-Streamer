from flask_opencv_streamer.streamer import Streamer
import cv2

# args = {'ip': "127.0.0.1",
#             'port': 5000,
#             'frame_count': 32}

# port = 3030

cam1_port = 5000
cam1_host = "127.0.0.1"
cam1_reqlogin = False
cam1_vidcap = cv2.VideoCapture(0)

# port = 5000
# host = "127.0.0.1"
# require_login = False
# streamer = Streamer(port, require_login)
# streamer = Streamer(port, require_login, host)

# streamer = Streamer(cam1_port, cam1_reqlogin, cam1_host)

stream1 = Streamer(cam1_port, cam1_reqlogin, cam1_host)

# Open video device
# video_capture = cv2.VideoCapture(0)
# video_capture = cv2.VideoCapture(1)

while True:
    # _, frame = video_capture.read()
    _, frame = cam1_vidcap.read()

    stream1.update_frame(frame)

    if not stream1.is_streaming:
        stream1.start_streaming()

    cv2.waitKey(30)