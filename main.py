# GiHub code implementation on Google Colab
# Author: SSR137851

print("Project initialized successfully")
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def main():
    print("✅ REAL-ESRGAN inference placeholder")
    print(f"📂 Input folder: {INPUT_DIR}")
    print(f"📂 Output folder: {OUTPUT_DIR}")

    inputs = os.listdir(INPUT_DIR)
    if not inputs:
        print("⚠️ No images found in input folder.")
    else:
        print(f"🖼 Found {len(inputs)} file(s):")
        for f in inputs:
            print(" -", f)

    print("✅ Ready for super-resolution pipeline.")

if __name__ == "__main__":
    main()

from PIL import Image

def main():
    print("✅ REAL-ESRGAN inference pipeline initialized")
    print(f"📂 Input folder: {INPUT_DIR}")
    print(f"📂 Output folder: {OUTPUT_DIR}")

    inputs = os.listdir(INPUT_DIR)

    if not inputs:
        print("⚠️ No images found in input folder")
        return

    print(f"🖼️ Found {len(inputs)} image(s):")
    for f in inputs:
        print(" -", f)

    # 🔹 NEW STEP: open first image
    first_image_path = os.path.join(INPUT_DIR, inputs[0])
    img = Image.open(first_image_path)

    print(f"✅ Image loaded successfully")
    print(f"📐 Image size: {img.size}")
    print(f"🎨 Image mode: {img.mode}")

    print("✅ Ready for super-resolution")
