import cv2
import numpy as np
from ultralytics import YOLO
import uuid

path=r'Experimenter_9110002_53.mp4'
model_path=r'E:\tensorrt\Trip\pose_weights\yolov8x-pose.pt'
model_pose=YOLO(model_path)

cam=cv2.VideoCapture(path)

fileid=str(uuid.uuid4())
record_path=f'yolo_pose_{fileid}.avi'
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc=cv2.VideoWriter_fourcc(*'mp4v')
fps=int(cam.get(cv2.CAP_PROP_FPS))
resize_width=width//2
resize_height=height//2
video_write=cv2.VideoWriter(record_path, fourcc,fps, (resize_width,resize_height))

while cam.isOpened():
    ret,frame=cam.read()
    if not ret:
        print("End of Video")
        break

    frame_pose=frame[height//2:,:width//2]
    result_pose=model_pose.predict(frame_pose,conf=0.6)
    keypoints=result_pose[0].keypoints.xy[0]
    for keypoint in keypoints:
        point=keypoint.cpu().numpy()
        point=point.astype('int')
        if not np.array_equal(np.array([0,0]),point):
            cv2.circle(frame_pose, point, 3, (0,0,255), -1)
            # print(point)
    cv2.imshow('Pose',frame_pose)
    video_write.write(frame_pose)
    if cv2.waitKey(1) & 0xff== 27:
        print("Quitting the program")
        break
   
cv2.destroyAllWindows()
video_write.release()
cam.release()