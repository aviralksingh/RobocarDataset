import sys

sys.path.append("../")
sys.path.append("../../../")
from sdk.robocar_dataset_sdk.python import camera_model
from sdk.robocar_dataset_sdk.python import image




if __name__ == '__main__':
    import sys
    import cv2
    import os
    img_prefix="/media/aviral/Barracuda_1/Robocar/RobocarDataset/2014-05-06-12-54-54/stereo/left/"
    model_path="../../../sdk/robocar_dataset_sdk/models/"
    for index,img in enumerate(os.listdir(img_prefix)):
        img_path=img_prefix+img
        model = camera_model.CameraModel(models_dir=model_path,images_dir=img_prefix)
        processed_img = image.load_image(img_path,model)
        processed_img=cv2.cvtColor(processed_img,cv2.COLOR_BGR2RGB)
        cv2.imshow("Processed",processed_img)
        cv2.waitKey(0) & 255