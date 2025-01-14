import argparse 
def retrieve_key_from_image(image_path , key_length = -12):
    # Open the modified image file in binary mode
    with open(image_path, 'rb') as img_file:
        img_data = img_file.read()

    # Assuming the key is appended at the end, find the key's length and extract the key
    # For example, let's assume the key has a fixed length of 12 bytes (adjust as needed)
    key_length = 12  # You must know the length of the key or how to identify it
    
    # Extract the key (last N bytes)
    key_binary = img_data[-key_length:]
    
    # Convert the binary data back to a string (utf-8 decoding)
    key = key_binary.decode('utf-8')

    return key

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Retrieve a hidden key from an image.")
    parser.add_argument("image_path", type=str, help="Path to the image with the hidden key.")
    args = parser.parse_args()

    # Retrieve the hidden key
    retrieved_key = retrieve_key_from_image(args.image_path)
    print(f"Retrieved Key: {retrieved_key}")