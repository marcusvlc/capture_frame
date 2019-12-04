# Capture Images From Streaming


## How to install

To run this python script, you will need python3.5 or above and pip. To install the dependencies, just run:

```
pip install -r requirements.txt
```

## How to run

Script parameters:
- --stream Url connection to your streaming. Can be RTSP urls, 0 (for webcam) or a path to a video.
- --n-frames Frame interval before saving an image.
- --save-dir Path of the folder where the images will be stored.

```
python capture.py --stream <url> --save-dir <path> --n-frames <frame number>
```