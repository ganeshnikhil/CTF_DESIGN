from PIL import Image
import piexif
import argparse
import base64


'''
You’ve been working in the shadows of the digital world, investigating a series of strange cyber events. In your latest assignment, 
a mysterious image has come your way. It's nothing out of the ordinary at first glance—just a regular picture. 
But something about it feels off. 
The file size seems too specific, and the details feel... layered.
A cryptic message from an anonymous source reads: 
"True artists leave more than just their mark. 
The secrets they hold aren’t always visible to the naked eye."
Your investigation uncovers a curious detail: this image has something hidden deep inside. 
Something more than just pixels and colors. As you dig deeper, 
you realize that this image is part of a larger puzzle—a trail left behind by someone who knows how to hide things in plain sight.
In the face of this new challenge, the question remains: Can you uncover the hidden truth beneath the surface, 
or will the image reveal its secrets only to those who know where to look?

'''


import base64
from PIL import Image
import piexif

def hide_key_in_exif(image_path, output_path , key):
    img = Image.open(image_path)
    
    # Check if the image has EXIF data; if not, use an empty dictionary
    exif_data = img.info.get("exif")
    exif_dict = piexif.load(exif_data) if exif_data else {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}, "thumbnail": None}
    print(exif_dict)
    # Encode the key in base64 to make it less obvious
    encoded_key = base64.b64encode(key.encode('utf-8')).decode('utf-8')
    
    # Store the base64-encoded key in the "Artist" tag of EXIF
    exif_dict["0th"][piexif.ImageIFD.Artist] = encoded_key.encode('utf-8')
    print(exif_dict)
    # Save the image with the hidden key in EXIF data
    exif_bytes = piexif.dump(exif_dict)
    img.save(output_path, "jpeg", exif=exif_bytes)
    print(f"Hidden key in EXIF 'Artist' tag successfully.")

if __name__ == "__main__":
    #hide_key_in_exif("test.png", "ctf{YourSecretKey}", "image_with_hidden_key.jpg")
    parser = argparse.ArgumentParser(description="Hide a key in the EXIF data of an image.")
    parser.add_argument("image_path", type=str, help="Path to the input image.")
    parser.add_argument("output_path", type=str, help="Path to save the output image with hidden key.")
    parser.add_argument("key", type=str, help="The key to hide in the image.")

    args = parser.parse_args()
    
    hide_key_in_exif(args.image_path, args.output_path , args.key)
