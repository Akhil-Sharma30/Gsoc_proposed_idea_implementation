import cv2
path=r'Experimenter_9110002_53.mp4'
cam=cv2.VideoCapture(path)
width=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=int(cam.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
scene_out = cv2.VideoWriter(r'frame_scene.avi', fourcc, fps, (width//2, height//2))
cam_top=cv2.VideoWriter(r'cam_top.avi', fourcc, fps, (width//2, height//2))
cam_bottom_left=cv2.VideoWriter(r'cam_bottom_left.avi', fourcc, fps, (width//2, height//2))
cam_bottom_right=cv2.VideoWriter(r'cam_bottom_right.avi', fourcc, fps, (width//2, height//2))

while cam.isOpened():
    ret,frame=cam.read()
    if not ret:
        print("End of Video")
        break
    frame_scene=frame[:height//2,:width//2]
    frame_cam_top=frame[:height//2,width//2:]
    frame_cam_bottom_left=frame[height//2:,:width//2]
    frame_cam_bottom_right=frame[height//2:,width//2:]

    scene_out.write(frame_scene)
    cam_top.write(frame_cam_top)
    cam_bottom_left.write(frame_cam_bottom_left)
    cam_bottom_right.write(frame_cam_bottom_right)

    # cv2.imshow('frame_scene',frame_cam_bottom_right)
    frame=cv2.resize(frame,(640,480))
    cv2.imshow('test',frame)
    if cv2.waitKey(1) & 0xFF==27:
        print("Quitting the program")
        break
cam.release()
scene_out.release()
cam_top.release()
cam_bottom_left.release()
cam_bottom_right.release()
cv2.destroyAllWindows()
