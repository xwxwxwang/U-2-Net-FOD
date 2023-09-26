import cv2
import os
import glob
import shutil

img_dir = "DUTS-TR/DUTS-TR-Image"
mask_dir = "DUTS-TR/DUTS-TR-Mask"

# for filen in os.listdir(img_dir):
#     imgp = os.path.join(img_dir, filen)
#     maskp = os.path.join(mask_dir, filen)
#     img = cv2.imread(imgp)
#     mask = cv2.imread(maskp.split(".")[0] + ".png")
#     print(mask)
#     print(imgp.split(".")[0]+"_flip.jpg")
#     cv2.imwrite(imgp.split(".")[0]+"_flip.jpg", cv2.flip(img, 1))
#     cv2.imwrite(maskp.split(".")[0]+"_flip.png", cv2.flip(mask, 1))

fod = "test_synth"
fmask = "synth_masks"

fod_lst = glob.glob(os.path.join(fod, "*.jpg"))

fmask_lst = glob.glob(os.path.join(fmask, "*.png"))

for maskp in fmask_lst:
    fname = maskp.split("/")[-1]
    shutil.copy(maskp, os.path.join(mask_dir, fname))

# for imgp in fod_lst:
#     fname = imgp.split("/")[-1]
#     shutil.copy(imgp, os.path.join(img_dir, fname))
