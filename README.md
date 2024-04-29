# space_detect
Object detection / tracking, collision avoidance for satellites.
___
#### Goals
- Detection of satellites, things that aren't stars or galaxies
- Mark identified objects
___
#### Dataset
Input images are obtained from Stellarium using the script `./stellarium/screenshots.ssc`
___
#### Setup/Requirements
**Stellarium**

1) Install Stellarium, information is available on their [README](https://github.com/Stellarium/stellarium) or their [FAQ](https://github.com/Stellarium/stellarium/wiki/FAQ#user-content-Installing_Stellarium)
2) Complete additional configuration and setup as described in `./stellarium/README`

**Python environment**

Using PIP (*recommended*)
1) Create a virtual environment: `python3 -m venv venv`
2) Activate the environment: `source venv/bin/activate`
3) Upgrade pip: `pip install --upgrade pip`
4) Install packages: `pip install opencv-python`

Using Anaconda
1) Install Anaconda or Miniconda, directions [here](https://www.anaconda.com/download/) or [here](https://docs.anaconda.com/free/anaconda/install/)
2) Create an environment: `conda create --name space_detect`
___
#### Scripts and Usage
**./stellarium/screenshots.ssc**: Stellarium script used to obtain input dataset
- See `./stellarium/README` for additional information

Run `python3 driver.py --stellarium` after installing and configuring Stellarium to obtain input images

**./driver.py**: driver script for repository functionalities
- Run `python3 driver.py --help` to see additional usage information

```bash
$ python3 driver.py --help
usage: driver.py [-h] [-s] [-d] [--show] [--dontsave] [--pause] [--split] [--truth]

driver.py - Space image CV

options:
  -h, --help        show this help message.
  -s, --stellarium  Run Stellarium to generate images
  -d, --detect      Run satellite detection on input
  --show            Show output images
  --dontsave        Don't save output images
  --pause           Pause and prompt to continue after each frame
  --split           Produce split image output showing image stages
  --truth           Produce truth image output and create csv output
```

- The stellarium option can be ran to produce the input dataset
- The show option will show images to the screen using cv2.imshow, press a key to close the image window
- The dontsave option will disable saving output images when processing input images
- The pause option will prompt to continue after each input image has been processed
- The split option will create a square image of 4 successive states of input processing
  - The top-left region is the input image
  - The top-right region is after the binary filter and open morph
  - The bottom-left region is after the background subtraction
  - The bottom-right region is the final marked image
- The truth option will create an artificial "ground truth" image for each input image
  - This command will output text suitable for creation of a .csv
  - The output images have 3 different colors for bounding boxes
    - Blue for TP, contours detected that indicate regions within the "ground truth"
    - Green for FP, contours detected that indicate regions not marked withing the "ground truth"
    - Red for missing (FN), contours not detected, leftover regions within the "ground truth"
  - The Green regions are also true-positive, but were not marked by template matching
  - The Red regions are found to be false negatives, these occur very infrequently
___
### [No License](https://choosealicense.com/no-permission/) at this time
___
