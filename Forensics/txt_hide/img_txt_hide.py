import argparse 
'''
In the digital world, data can be hidden anywhere—sometimes in plain sight, and other times, buried deep within files that seem ordinary.
You’ve recently stumbled upon a set of encrypted messages, each linked to a different image. 
These images are known to contain something much more valuable than what appears on the surface.
An encrypted note left by a mysterious figure reads: "When the image is complete, the message is hidden in the shadows, 
waiting for those with the right key to unveil its truth."
A strange detail arises from your investigation: one of the image files seems to be larger than usual, with extra, unexplained data at the end. 
Could this be where the secret is stored?
Your task is clear. Dive into the hidden layers of the image, find where the truth is buried, 
and retrieve the key that could lead to a much bigger discovery. 
But remember, this is just the beginning—there’s more lurking in the depths than you can imagine.

'''


def embed_key_in_image(image_path,  output_path , key):
    # Open the image file in binary mode
    with open(image_path, 'rb') as img_file:
        img_data = img_file.read()
    
    # Convert the key to binary
    binary_key = key.encode('utf-8')  # Convert key to binary (utf-8 encoding)
    
    # Append the binary key to the image data
    modified_img_data = img_data + binary_key

    # Write the modified data to a new image file
    with open(output_path, 'wb') as new_img_file:
        new_img_file.write(modified_img_data)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Embed a secret key into an image.")
    parser.add_argument("image_path", type=str, help="Path to the original image.")
    parser.add_argument("output_path", type=str, help="Path to save the new image with the embedded key.")
    parser.add_argument("key", type=str, help="The secret key to embed.")
    args = parser.parse_args()

    # Embed the key in the image
    embed_key_in_image(args.image_path, args.output_path , args.key)
