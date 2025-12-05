#!/usr/bin/env python3
"""
Script to crop images to 1:1 (square) aspect ratio.
Crops from the center of the image.

Usage:
    python crop_images.py image1.jpg image2.png image3.webp

The script will:
1. Load each image
2. Crop it to a square (1:1 aspect ratio) from the center
3. Save it with '_square' suffix (e.g., image1_square.jpg)
4. Optionally, you can replace the original by renaming the output
"""

import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: PIL (Pillow) is not installed.")
    print("Please install it with: pip install Pillow")
    sys.exit(1)


def crop_to_square(image_path, output_path=None, replace_original=False):
    """
    Crop an image to square (1:1) aspect ratio from the center.

    Args:
        image_path: Path to the input image
        output_path: Path to save the cropped image (optional)
        replace_original: If True, replace the original file

    Returns:
        Path to the output file
    """
    # Load the image
    img = Image.open(image_path)
    width, height = img.size

    print(f"Processing {image_path.name}: {width}x{height}")

    # Calculate the size of the square (use the smaller dimension)
    square_size = min(width, height)

    # Calculate crop coordinates (centered)
    left = (width - square_size) // 2
    top = (height - square_size) // 2
    right = left + square_size
    bottom = top + square_size

    # Crop the image
    img_cropped = img.crop((left, top, right, bottom))

    # Determine output path
    if replace_original:
        output = image_path
    elif output_path:
        output = Path(output_path)
    else:
        # Create output filename with _square suffix
        output = image_path.parent / f"{image_path.stem}_square{image_path.suffix}"

    # Save the cropped image
    img_cropped.save(output, quality=95)
    print(f"  Saved as {output.name}: {square_size}x{square_size}")

    return output


def main():
    if len(sys.argv) < 2:
        print("Usage: python crop_images.py <image1> <image2> ...")
        print("\nOptions:")
        print("  --replace    Replace original files instead of creating new ones")
        print("\nExample:")
        print("  python crop_images.py images/diego.webp images/rocio.webp images/julian.webp")
        print("  python crop_images.py --replace images/diego.webp")
        sys.exit(1)

    # Check for --replace flag
    replace_original = False
    image_paths = []

    for arg in sys.argv[1:]:
        if arg == '--replace':
            replace_original = True
        else:
            image_paths.append(Path(arg))

    if not image_paths:
        print("Error: No image files specified")
        sys.exit(1)

    # Process each image
    print(f"Cropping {len(image_paths)} image(s) to square (1:1 aspect ratio)...")
    print()

    for image_path in image_paths:
        if not image_path.exists():
            print(f"Error: File not found: {image_path}")
            continue

        try:
            crop_to_square(image_path, replace_original=replace_original)
        except Exception as e:
            print(f"Error processing {image_path}: {e}")

    print("\nDone!")

    if not replace_original:
        print("\nNote: Original files were preserved. New files have '_square' suffix.")
        print("To replace originals, run with --replace flag or manually rename the files.")


if __name__ == "__main__":
    main()
