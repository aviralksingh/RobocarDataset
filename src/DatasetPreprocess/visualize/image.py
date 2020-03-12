import sys

sys.path.append("../")
sys.path.append("../../../")
sys.path.append("../../../../sdk/robotcar-dataset-sdk/")
from sdk import



if __name__ == '__main__':
    import sys
    import cv2
    import camera_model
    import os
    img_prefix="../../../RobocarDataset/2014-05-06-12-54-54/stereo/left/"
    for index,img in enumerate(os.listdir(img_prefix)):
        Img=img_prefix+img
        model = camera_model.CameraModel(models_dir="../models/",images_dir="../../../RobocarDataset/2014-05-06-12-54-54/stereo/left/")