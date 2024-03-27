import os
import argparse
from PIL import Image
from rembg import new_session, remove

def process_image(input_path, output_path, session=None):
    input_image = Image.open(input_path)
    output_image = remove(input_image, session=session)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    output_image.save(output_path)

def process_directory(input_dir, output_dir, session=None):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                output_path = os.path.splitext(output_path)[0] + "_transparent.png"
                process_image(input_path, output_path, session)
                print(f"Processed: {input_path} -> {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Remove background from images and save with transparent background.")
    parser.add_argument("-i", "--input_dir", required=True, help="Input directory containing images.")
    parser.add_argument("-o", "--output_dir", required=True, help="Output directory to save processed images.")
    args = parser.parse_args()
    model_name = "u2net"
    rembg_session = new_session(model_name)
    process_directory(args.input_dir, args.output_dir, session=rembg_session)

if __name__ == "__main__":
    main()