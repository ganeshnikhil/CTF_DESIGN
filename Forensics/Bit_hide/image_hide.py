from PIL import Image
import argparse
# '''
# In the world of cybersecurity, there's a rumor that a notorious hacker group has hidden critical information within an image file. 
# These hackers have always been one step ahead, using advanced encryption and steganography techniques to hide their tracks.
# Your mission begins when a mysterious image is sent to your team. 
# This image is believed to hold a key to accessing a highly secure database, 
# but it's been encrypted in such a way that no traditional methods of analysis can reveal its secrets.
# The only clue you have is a hint dropped by an informant: 
# "The key is hidden beneath the surface, where the lightest of touches can expose the truth.
# " Now, you need to figure out how to extract the hidden message before it falls into the wrong hands.
# As the clock ticks, can you uncover the hidden key, decode the information, and secure the database before it's too late?

# '''

def format_key(key):
    # Convert the key to binary
    binary_key = ''.join(format(ord(c), '08b') for c in key)
    return binary_key


def hide_key(data , binary_key):
    new_data = []
    key_index = 0

    for pixel in data:
        if key_index < len(binary_key):
            # Get the current alpha value
            alpha = pixel[3]
            
            # Clear the LSB of the alpha value
            new_alpha = alpha & 0b11111110  # Set LSB to 0
            
            # Set the LSB of the alpha value to the current bit of the binary key
            new_alpha = new_alpha | int(binary_key[key_index])  # Set LSB to the bit of the key
            new_data.append((pixel[0], pixel[1], pixel[2], new_alpha))
            
            # Move to the next bit of the key
            key_index += 1
        else:
            # If the key has been fully embedded, keep the pixel unchanged
            new_alpha = alpha & 0b11111110  # Set LSB to 0
            new_data.append((pixel[0], pixel[1], pixel[2], new_alpha))
    return new_data

def save_image(img , new_data , output_path):
    # Save the modified image
    img.putdata(new_data)
    img.save(output_path)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Hide a secret key in the alpha channel of an image.")
    parser.add_argument("image_path", type=str, help="Path to the input image (RGBA).")
    parser.add_argument("output_path", type=str, help="Path to save the image with the hidden key.")
    parser.add_argument("key", type=str, help="Secret key to hide in the image.")
    args = parser.parse_args()

    # Open the input image
    img = Image.open(args.image_path).convert("RGBA")
    data = img.getdata()

    # Process the key and hide it in the image
    binary_key = format_key(args.key)
    new_data = hide_key(data, binary_key)

    # Save the modified image
    save_image(img, new_data, args.output_path)
    print(f"Key successfully hidden in {args.output_path}")