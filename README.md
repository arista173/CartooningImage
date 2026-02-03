# Cartooning Image

## Overview
A simple Python program that converts regular images into cartoon-style images using OpenCV.

## Features
- Converts any image to cartoon style with black outlines and flat colors
- Interactive command-line interface
- Supports common image formats (JPG, PNG, BMP, etc.)
- Saves output with user-defined filename
- Clean, single-execution program

## Prerequisites
- Python 3.x installed
- OpenCV library

## Installation
1) Clone or download this repository
2) Install the required libary
   ```bash
   python -m pip install opencv-python
   ```

## Usage
1) Place your image file in the same directory as the script (or use full path)
2) Run the program
3) Follow the prompts:
   - Enter input image filename (ex. image.jpg)
   - Enter output filename (ex. result.jpg)
4) View the cartoon image in the popup window
5) Press any key to close the window and end the program

## How It Works
The program uses a combination of computer vision techniques:
1) Grayscale Conversion - Converts the image to black and white
2) Median Blur - Reduces noise while preserving edges
3) Adaptive Thresholding - Creates a binary edge mask
4) Bilateral Filter - Smooths colors while maintaining edges
5) Bitwise AND Operation - Combines edge mask with smoothed colors

## Tech Stack
- Python

## File Structure
```text
CartooningImage/
├── cartoon.py       # Main Python script
├── test1.jpg        # Your input image (example)
├── res1.jpg         # Generated cartoon image (example)
```
