# space_detect
Object detection / tracking, collision avoidance for satellites.
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
**./driver.py**: driver script for repository functionalities
- Run `python3 driver.py --help` to see additional usage information
- Run `python3 driver.py --stellarium` after installing and configuring Stellarium to obtain input images

**./stellarium/screenshots.ssc**: Stellarium script used to obtain input dataset
- See `./stellarium/README` for additional information
___
#### Potential Goals
- Detection of stars and galaxies, things that aren't satellites
- Detection of satellites, things that aren't stars or galaxies
- Label identified objects
- Track objects, e.g., determine relative speed and predict future location
___
### [No License](https://choosealicense.com/no-permission/) at this time
___
