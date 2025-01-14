from PIL import Image
import argparse 

def seek_key(data):
    # Retrieve the binary key from the alpha channel
    retrieved_binary_key = ''
    for pixel in data:
        # Get the alpha value
        alpha = pixel[3]
        
        # Extract the LSB of the alpha value
        lsb = alpha & 0b00000001  # Get the LSB (0 or 1)
        
        # Append the LSB to the binary key string
        retrieved_binary_key += str(lsb)
    return retrieved_binary_key

def ascii_conv(retrieved_binary_key):
    # Convert the binary string back to the original key
    key = ''
    for i in range(0, len(retrieved_binary_key), 8):
        byte = retrieved_binary_key[i:i+8]
        key_byte = chr(int(byte, 2))
        if key_byte.isprintable():
            key += chr(int(byte, 2))
    return key 
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Reveal a hidden key from the alpha channel of an image.")
    parser.add_argument("image_path", type=str, help="Path to the image with the hidden key.")
    args = parser.parse_args()

    # Open the input image
    img = Image.open(args.image_path).convert("RGBA")
    data = img.getdata()

    # Retrieve the binary key and convert it to ASCII
    retrieved_binary_key = seek_key(data)
    key = ascii_conv(retrieved_binary_key)

    # Print the retrieved key
    print("Retrieved key:", key)