# Image-template-matching
## About the project:
- Takes 2 images: Original image and a sub instance of it (Line 5 and 6).
- Its purpose is to find where the sub image is located in its original one.
- It Loads images in gray scale for analysis.
- It uses multiple analysis methods to find the best one that founds a match.

## Image analysis algorithms (methods):
- `cv2.TM_CCOEFF`, `cv2.TM_CCOEFF_NORMED`, `cv2.TM_CCORR`, `cv2.TM_CCORR_NORMED`, `cv2.TM_SQDIFF` and `cv2.TM_SQDIFF_NORMED`
- For `cv2.TM_SQDIFF` and `cv2.TM_SQDIFF_NORMED`, we use the min location values as starting point for the analysis.
- Every other method uses the max location value to do its job.

## What did I learn from this:
- Difference between different image processing algorithms in OpenCV.
- .matchTemplete() and .minMaxLoc().
- Exiting the program when pressing a certain key on the keyboard.
