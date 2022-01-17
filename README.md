# open-imagilib

This package is an implementation of the `imagilib` library originally developed by [ImagiLabs](https://imagilabs.com/).

It can be used as an emulation environment to develop Python programs for [imagiCharm](https://imagilabs.com/products/imagicharm) devices.

## Features 
- Implements the API used to control the LED matrix of **ImagiCharm** devices.
- Renders the LED matrix on an OpenCV image window, both static and animation.
- Saves the matrix of non-animated programs as PNG image.
- Renders animations as GIF or a sequence of PNG images.
- Runs on a full Python deployment, while still remains reasonably compatible.

Please visit the [imagi Learning Center](https://www.notion.so/imagilabs/imagi-Learning-Center-5afe3d51d30645849f2738c9b5eb1154) to find out more about imagiCharm devices and the imagilib API.

![HSV Spiral](/programs/hsv_spiral.gif)
![Tunnel Vision](/programs/tunnel_vision.gif)
![Gradient](/programs/gradient.gif)
![Chessboard](/programs/chessboard.gif)
![Olympics](/programs/olympics.gif)
![Olympics 2](/programs/olympics2.gif)

## Intended use case

This module is intended to provide a reasonably good imagiCharm "emulator" for parents with 
Python development skills. It allows for using a proper Python IDE (like JetBrains PyCharm) 
while helping the children in their first steps in programming.

## Remarks
 
Great care has been taken to ensure maximum compatibility, but there can be subtle differences.

There is a comprehensive test suite covering most of the functionality. Please see the `tests` and `programs` subdirectories for examples. 

Please report any bugs or discrepancies on GitHub by creating a new issue. PRs to fix problems or add new functionality are always welcome.

Developed and tested on Python 3.9.7 (64 bit, Windows)

Please see the `requirements.txt` file for dependencies. 

To install dependencies: `pip install -r requirements.txt`

## Troubleshooting

### Uploading to imageCharm

The best way to upload your code from the desktop Python IDE to a physical imagiCharm device is through the [imagiLabs Web App](https://imagilabs.com/app) (currently in beta).

Create a new program on the Web App, copy-paste the code from PyCharm (or other Python IDE) into the browser, then save the project.

The program can be uploaded directly to an imageCharm device if your PC has bluetooth connectivity.

The Android and iOS imagiLabs apps can upload the program to an imagiCharm, since they have access to the saved project in the cloud. 

### Color mismatch

The lack of color calibration of the real imagiCharm devices is not accounted for, 
so the exact colors on screen will differ from what's shown on the real devices.
Always test your program on a real device and correct the colors as needed.

Currently, the colors differ based on where the program is uploaded from to imagiCharm. 
Uploading from Android seems to work slightly better than from the Web UI. For dark 
color components there is a huge difference.

Hopefully this aspect will improve in the future.

### Available libraries

The mobile app applies more validation on the code before execution and the range of Python libraries
available is narrower than on a full Python installation. Try to stick with the libraries and functions
listed on ImagiLabs' Documentation pages, otherwise your program may not work. Also make sure the data
types are always the expected ones, for example convert to an int when an int is expected.

### Characters look differently

The 6x8 bitmap font used in this library is based on an ASCII table rendered using 
[int10h.org](https://int10h.org/oldschool-pc-fonts/fontlist/font?portfolio_6x8).
This character set was used by the Atari Portfolio palmtop computers originally.

It differs from the font the imagiCharm is using. This may be fixed later, but no promises.

## Legal

[imagiCharm](https://imagilabs.com/products/imagicharm) is trademark of [ImagiLabs](https://imagilabs.com/).

I cannot guarantee keeping this package up to date to match future API changes.

Please see the `LICENSE` file for the legal text.
