# Gsoc_proposed_idea_implementation 

To look at the results you can click [*here*](https://drive.google.com/drive/folders/1_J6WhITqH4kxma0pcPcwxHaVzcXlAK3f?usp=sharing):

# Installation Guide for Gsoc Project

Welcome to the installation guide for the `this` project. This project is designed to analyze driving behavior using various data analysis and machine learning techniques. Follow the steps below to get started with this project on your local machine

> To install SPIGA and the L2CS net look at the following repositories<br>
> [**SPIGA**](https://github.com/andresprados/SPIGA) <br>
> **else clone this repo and use the spiga folder provided above**.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.6 or later
- Git
- pip (Python package installer)

## Cloning the Repository

To get started with the `this` project, clone the repository to your local machine using the following command:

```
git clone https://github.com/Akhil-Sharma30/Gsoc_proposed_idea_implementation.git
```

This command creates a copy of the repository in your local directory.

## Setting Up a Virtual Environment

It's recommended to use a virtual environment for Python projects. This keeps your dependencies organized and separate from other projects. Use the following commands to set up a virtual environment:

For Windows:
```
python -m venv venv
.\venv\Scripts\activate
```

For macOS and Linux:
```
python3 -m venv venv
source venv/bin/activate
```

## Installing Dependencies

With your virtual environment activated, install the project dependencies using `pip`:

```
pip install -r requirements.txt
```

This command reads the `requirements.txt` file from the cloned repository and installs all the necessary Python packages.

## Running the Project

After installing the dependencies, you're ready to run the project. Navigate to the project directory and use the appropriate command to start the analysis or application.

> Run *crash_detect.py* to get the when the car is at risk of collision with objects. The ROI which is selected can be made more or less aggressive by choice.
```

## Conclusion

You've now successfully set up the `this` project on your local machine. Explore the repository and its documentation to understand more about the project's capabilities and how to utilize them.

# Results Analysis and discussion:
# Results from dataframe analysis
1) Dataframes obtained from above scripts were used to categorize drowsy and distracted behaviour of the driver. The code for that can be found in `drowsy_frames_clustering_analysis.py` [*results*](https://drive.google.com/drive/folders/1fJyUjCxueTuBRm7DA7FaK66bicnaczWI?usp=sharing).
2) Code for Gaze attention during drowsiness can be found in `gaze_detection_clustering_analysis.py`.Some graphs related to it can be found [*here*](https://drive.google.com/drive/folders/1fJyUjCxueTuBRm7DA7FaK66bicnaczWI?usp=sharing).
3) Code for overall clustering analysis during data analysis can be found in `overall_clustering_analysis.py`.

## Drowsiness detection
1) The analysis focused on assessing driver drowsiness by tracking the Eye Aspect Ratio (EAR) across each video frame. Utilizing K-means clustering, the video was segmented into two distinct groups. Drowsiness was then evaluated based on instances where the eyes remained closed for a duration exceeding 5 frames. The findings were documented in the file under dataframe_cluster/drowsy_frames.csv, and excerpts from the video illustrating these moments were compiled in the ear_cluster directory.

2) Drowsiness gaze attention: Applied a gaze detection script on the video and saved the results in [this](https://github.com/Akhil-Sharma30/Gsoc_proposed_idea_implementation/blob/main/gaze_detection_20_03.csv) csv file also you can run `gaze_detection_clustering_analysis.py` python file to see the analysis. Then after seperating the drowsy frames by headpose values ,it was noticed that when the driver was drowsy she was not focused on the road and was looking at the steering of the vehicle for a portion of the time.

## Annotation of Objects of interest
1) Firstly the pretarined YOLOv8 model with SAHI was used to test the video in objectDetectionSAHI.py. Then OCSort tracking was used alongwith YOLOv8_SAHI with 70 percent effectively track the objects of interest. The results can be found [*here*](https://drive.google.com/file/d/1sTMq1Qb0iifQkidksBZXiRd701cQL9q-/view?usp=sharing)

2) A custom object detection model was trained on the [alabama ATI dataset](https://universe.roboflow.com/alabama-transport-insititue-tbwq8/ati-yolov8). An arificial class for trash can was added to detect it in the video.

3) Using these two models we can identify all the objects of interest in the frame like in Collision_detection.avi
*Note*: This video does not use SAHI and just uses plain object detection.

## Risky Scenario and Agressive driver
1) The script `crash_detect.py` houses the code for recognizing sudden appearances of objects, such as a trash can, within a predefined Region of Interest (ROI). These objects, upon entering the ROI, trigger a visual alert by changing their bounding box color to red, signaling their detection. While the current implementation does not distinguish between objects like cars or trucks, resulting in occasional false alarms, this mechanism lays the groundwork for applications such as tailgating detection by analyzing the proximity of vehicles. The results can be seen in this [video](https://drive.google.com/file/d/1Xjh429_AsTdgvxbpx8O93iUmc6KPcQkP/view?usp=sharing)

# How to Get results:
1) Run *crash_detect.py* to get the when the car is at risk of collision with objects. The ROI which is selected can be made more or less aggressive by choice.<br>
To look directly at the results click [*here*](https://drive.google.com/file/d/1Xjh429_AsTdgvxbpx8O93iUmc6KPcQkP/view?usp=sharing)

2) Run head position_df to get a dataframe of the head orientation at ech frame and a video. Then with the dataframe you get with this you can run head-pose_cluster.py to get the cluster of videos for head pose. Results can be found [*here*](https://drive.google.com/drive/folders/1g5kCxpOjYAiP0i7Msy1uxVQ74lX1awxK?usp=drive_link)

5) For running the emotion detection results run emotion_recog_df.py. The reults can be found [*here*](https://drive.google.com/file/d/1hYsPhUCFP2DpgTDHyibHaQGBW3xikItA/view?usp=drive_link)

6) For object detection and tracking using yolov8 run track_yolov8.py. Can change between the pretained model and the custom alabama model
   
7) For running object detection and tracking with YOLOv8+SAHI+OCSORT tracking algorithm run trackOC.py. [(*result for pretained model*)](https://drive.google.com/file/d/1sTMq1Qb0iifQkidksBZXiRd701cQL9q-/view?usp=drive_link)

8) Run data_cleaning.py to make the number of frames and the readings equal. It also drops the empty columns and columns with only one unique value. Some reults related to it can be found in *crash.ipynb*

9) Run `gaze.py` inside the GAZE_detection folder to get a dataframe of the gaze of the driver at every timestep. Result can be found [*here*](https://drive.google.com/file/d/1SRltQSQ72dzWWwX9ydYQNTwOqZk_MFy7/view?usp=sharing)


   



   

