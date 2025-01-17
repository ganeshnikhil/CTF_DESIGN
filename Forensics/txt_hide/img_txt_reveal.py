import argparse 
def retrieve_key_from_image(image_path, key_format):
    """
    Retrieves the CTF key in the specified format (e.g., CSCTF{}) hidden in the binary data of an image.

    Args:
        image_path (str): The path to the image file.
        key_format (str): The format of the key to search for (e.g., 'CSCTF').

    Returns:
        str: The found CTF key, or a message indicating no key was found.
    """
    try:
        # Open the image file in binary read mode
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
        
        # Decode the binary data into a string for regex search
        # Use errors='ignore' to skip non-text binary content
        img_text = img_data.decode('utf-8', errors='ignore')

        # Search for the CTF key using regex
        match = re.search(fr'{re.escape(key_format)}\{{.*?\}}', img_text)

        if match:
            return match.group(0)  # Return the found key
        else:
            return "No CTF key found in the image binary data."
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Retrieve a hidden key from an image.")
    parser.add_argument("image_path", type=str, help="Path to the image with the hidden key.")
    args = parser.parse_args()

    # Retrieve the hidden key
    retrieved_key = retrieve_key_from_image(args.image_path)
    print(f"Retrieved Key: {retrieved_key}")
