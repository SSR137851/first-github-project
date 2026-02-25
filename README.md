# REAL-ESRGAN Super Resolution (Inference)

This project demonstrates how to use a pretrained REAL-ESRGAN model
to enhance the resolution and quality of low-resolution images.

The focus of this project is **inference**, not training.

## Project Goals
- Apply image super-resolution using a pretrained model
- Improve image clarity and sharpness
- Run the pipeline locally without Google Colab

## Technology
- Python
- PyTorch
- REAL-ESRGAN (Xintao et al.)

## Status
Project setup and documentation in progress.

## Current Status

✅ Project structure initialized  
✅ Input directory scanning implemented  
✅ Image loading and validation using PIL  

📌 Current Stage: Pipeline Initialization & Input Validation
At the current stage, `main.py`:
- Scans the `input/` directory for images
- Loads the first available image using PIL
- Prints basic image properties (size and color mode)
