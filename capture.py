import cv2
import argparse
import os
import time

def capture_images(args):
    capture = cv2.VideoCapture(args.stream)
    count = 0

    while(capture.isOpened()):
        ret, frame = capture.read()
        if(ret):


            key = cv2.waitKey(1) & 0xFF

            if(count == args.n_frames):
                time_now = int(time.time())
                img_name = "img_" + str(time_now) + ".jpg"
                print("Saving image... Folder saved: " + args.save_dir)
                if(args.save_dir[-1] == "/"):
                    cv2.imwrite(args.save_dir  + img_name ,frame)
                else:
                    cv2.imwrite(args.save_dir + "/" + img_name ,frame)

                count = 0

            if key == ord("q"):
                break
        
        count+=1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Saving Frames from Streaming')
    parser.add_argument('--stream', default=0, type=str,
                        help='The url stream for live couting')
    parser.add_argument('--n-frames', default=30, type=int,
                        help='The interval to save the frames. In seconds')
    parser.add_argument('--save-dir', default='./images', type=str,
                    help='The directory where images will be saved')



    args = parser.parse_args()

    if(not os.path.exists(args.save_dir)):
        raise ValueError("Save Directory not found")

    capture_images(args)

