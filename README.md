# DL_Project2

1. Run the model.py
2. pip install requirements.txt
3. After that CD into yolov5
4. Run the below command for training 

python3 train.py --img 640 --batch 16 --epochs 5 --data coco128.yaml --freeze 10 11 12 13 14 15  16 17 18 19 20 21 22 23 --weights yolov5m.pt --cfg ./models/yolov5m.yaml

5. Run the below command for testing

python3 detect.py --weights ./runs/train/exp_number/weights/best.pt --save-conf --save-txt --source ../dataset/test/images/

6. We get all the label files individually, running `python results.py` will give us a single text file. In the results.py file, instead of exp_number, a number for the tested labels we want to combine should be given. If running for the first time, it should usually be 1.
