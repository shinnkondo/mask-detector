# Mask Detector
Gentry reminds people to wear a mask when peason without a mask is detected.

## Requirements
An audio library is needed.
```
sudo apt install sox
```

## Usage

```
<yolov5_command> | python detector.py <path_to_audio_file_for_without_mask> <path_to_audio_file_for_incorrectly_worn_mask>
```

e.g. in yolov5 folder,
```
python detect.py --weights ~/Downloads/best_2021-04-08.pt --source 0 --img 416 --iou 0.3 --name robo4_epoch300_s_3_labels | python ../mask-detector/detector.py ../mask-detector/resources/mask_reminder_EN.ogg ../mask-detector/resources/mask_reminder_incorrect_EN.ogg^C

```