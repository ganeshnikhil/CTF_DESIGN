from PIL import Image
import argparse
import piexif
import base64

def retrieve_key_from_exif(image_path):
    img = Image.open(image_path)
    exif_dict = piexif.load(img.info["exif"])

    # Extract the base64-encoded key from the "Artist" field
    encoded_key = exif_dict['0th'].get(piexif.ImageIFD.Artist, b'').decode('utf-8')

    if encoded_key:
        # Decode the base64 to get the original key
        key = base64.b64decode(encoded_key).decode('utf-8')
        return key
    else:
        return None

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Retrieve a hidden key from the EXIF data of an image.")
    parser.add_argument("image_path", type=str, help="Path to the image with hidden key.")
    args = parser.parse_args()
    
    try:
        # Retrieve the key
        key = retrieve_key_from_exif(args.image_path)
        print(f"Retrieved key: {key}")
    except Exception as e:
        print(f"Error: {e}")