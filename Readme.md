# Mask Detector
Gentry reminds people to wear a mask when peason without a mask is detected.

## Requirements
An audio library is needed.
```
sudo apt install sox
```

## Usage

```
<yolov5_command> | python detector.py <path_to_audio_file>
```

e.g.
```
yolov5$ python detect.py --device cpu --weights ~/Downloads/best.pt --source 0 --img 416 --iou 0.3 --name robo4_epoch300_s_skipped | python ../mask-detector/detector.py ../mask-detector/resources/mask_reminder_EN.ogg 
```