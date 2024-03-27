import cv2
import mediapipe as mp
import numpy as np
import uuid
from functions_utils import draw_facial_landmarks_on_image

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

model_path=r'E:\tensorrt\Trip\models\face_landmarker_v2_with_blendshapes.task'

# Create a face landmarker instance with the video mode:
options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.VIDEO,
    num_faces=1,
    min_face_detection_confidence=0.1,
    )

detector = FaceLandmarker.create_from_options(options)


path=r'E:\tensorrt\TRIP\Experimenter_9110002_53.mp4'
cam=cv2.VideoCapture(path)
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
fps=int(cam.get(cv2.CAP_PROP_FPS))
fileid=str(uuid.uuid4())

record_path=f'facial_landmarks_{fileid}.avi'
fourcc=cv2.VideoWriter_fourcc(*'mp4v')
resize_width=width//2
resize_height=height//2
video_write=cv2.VideoWriter(record_path, fourcc,fps, (resize_width,resize_height))

while cam.isOpened():
    ret,frame=cam.read()
    if not ret:
        print("End of Video")
        break
    cam_bottom_left=frame[height//2:,:width//2]

    timestamp = int(cam.get(cv2.CAP_PROP_POS_MSEC))   #Get the timestamp of the current frame for mediapipe
    cam_bottom_left=cv2.cvtColor(cam_bottom_left,cv2.COLOR_BGR2RGB)
    rgb_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=cam_bottom_left)
    detection_result = detector.detect_for_video(rgb_frame,timestamp)
    
    cam_bottom_left = draw_facial_landmarks_on_image(cam_bottom_left, detection_result)
    cam_bottom_left=cv2.cvtColor(cam_bottom_left,cv2.COLOR_RGB2BGR)
    cv2.imshow('cam_bottom_left',cam_bottom_left)
    video_write.write(cam_bottom_left)

    if cv2.waitKey(1) & 0xFF==27:
        print("Quitting the program")
        break

cam.release()
video_write.release()
cv2.destroyAllWindows()

