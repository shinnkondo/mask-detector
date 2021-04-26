# Mask Detector
Gentry reminds people to wear a mask when peason without a mask is detected.
It parses stdin, and make annnouncements based on that.

## Requirements
### Unix

- Python 3.* is needed.
- An audio library is needed.


```
sudo apt install sox
```

### Other requirements

- https://github.com/ultralytics/yolov5 : it does the actual detection part based on video input, and output logs for this script. Follow the link for requirements, etc.
- weight : a configuration file for yolov5. Please download it from [here](https://drive.google.com/file/d/12qNSd6LhdayQVg8pULacW-v4z9ICO3j-/view?usp=sharing)

## Installtaion/Setting

1. Install yolov5
2. Download a weight file
3. Clone this repo parallel to yolov5

├── yolov5
└── mask-detector


## Usage

```
<yolov5_command> | python detector.py <path_to_audio_file_for_without_mask> <path_to_audio_file_for_incorrectly_worn_mask>
```

e.g. in yolov5 folder,
```
python detect.py --weights ~/Downloads/best_2021-04-08.pt --source 0 --img 416 --iou 0.3 --name robo4_epoch300_s_3_labels | python ../mask-detector/detector.py ../mask-detector/resources/mask_reminder_EN.ogg ../mask-detector/resources/mask_reminder_incorrect_EN.ogg

```

or, for multiple files

```
python detect.py --weights ~/Downloads/best_2021-04-08.pt --source 0 --img 416 --iou 0.3 --name robo4_epoch300_s_3labels | python ../mask-detector/detector.py "../mask-detector/resources/without_mask_EN_F.ogg ../mask-detector/resources/without_mask_JP_F.ogg" "../mask-detector/resources/mask_worn_incorrectly_EN_F.ogg ../mask-detector/resources/mask_worn_incorrectly_JP_F.ogg"
```

or, adding a volume arguments

```
python ../mask-detector/detector.py "-v 2 ../mask-detector/resources/without_mask_EN_F.ogg -v 2 ../mask-detector/resources/without_mask_JP_F.ogg" "-v 2 ../mask-detector/resources/mask_worn_incorrectly_EN_F.ogg -v 2 ../mask-detector/resources/mask_worn_incorrectly_JP_F.ogg" 
```


Alternatively, executing `script.sh` would work assuming the location is correct.