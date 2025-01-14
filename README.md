# CTF_DESIGN

# CTF_DESIGN

Welcome to the **CTF_DESIGN** repository! This repository is a collection of challenges designed for Capture the Flag (CTF) competitions. These challenges are themed around the TV series *Mr. Robot* and currently focus on brute force and forensic techniques. Below is a detailed description of the structure and content of this repository.

---

## Repository Structure

### 1. **Bruteforce**
- **Purpose**: Contains a script to brute force a password-protected PDF.
- **Contents**:
  - `pdf_bf.py`: A Python script that takes a PDF file as input and attempts to brute force its password using a dictionary attack.
  - `requirements.txt`: Lists the necessary Python libraries required to run the script.
- **Usage**: Run the script via command-line arguments. Ensure you install the required libraries using `pip install -r requirements.txt`.

### 2. **Forensics**
This directory is divided into three subfolders, each focusing on different forensic techniques.

#### **a. Bit_hide**
- **Purpose**: Contains scripts to hide and reveal data using bit manipulation.
- **Contents**:
  - `hide_bit.py`: Hides data within an image at the bit level.
  - `reveal_bit.py`: Extracts hidden data from an image.
  - Sample files: Images with hidden data for testing.
- **Usage**: Execute the scripts via command-line arguments. Install dependencies beforehand.

#### **b. Exif_hide**
- **Purpose**: Contains scripts to hide and reveal data in the EXIF metadata of images.
- **Contents**:
  - `hide_exif.py`: Embeds data into the EXIF metadata of an image.
  - `exif_retrive.py`: Retrieves the embedded data from EXIF metadata.
  - Sample files: Images with modified EXIF metadata.
- **Usage**: Use command-line arguments to run the scripts. Install dependencies before use.

#### **c. Txt_hide**
- **Purpose**: Contains scripts to append and retrieve text data from image files.
- **Contents**:
  - `hide_txt.py`: Appends a secret key or data to an image file as text.
  - `retrieve_text.py`: Extracts the appended text from an image file.
  - Sample files: Images with appended text for testing.
- **Usage**: Run the scripts via command-line arguments after installing dependencies.
  
- `requirements.txt`: Lists the necessary libraries to run the scripts.
---

## Themes
The challenges in this repository are inspired by the *Mr. Robot* TV series, with sample images and PDFs reflecting themes from the show. Future challenges will continue to explore similar themes.

---

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/ganeshnikhil/CTF_DESIGN
   ```
2. Navigate to the respective directories to explore the challenges.
3. Install the required libraries for each challenge using the provided `requirements.txt` files.
4. Use the command-line interface to run the scripts with appropriate arguments.

---

## Future Plans
This repository will continue to expand with:
- Additional challenge folders.
- More scripts implementing creative hiding and revealing techniques.
- Sample files tailored to new challenges.
- Improved usability and features based on user feedback.

---

## Contribution
Contributions to this repository are welcome! If you have ideas for new challenges or improvements to existing scripts, feel free to create a pull request or open an issue.

---

## Disclaimer
This repository is for educational purposes only. The techniques and scripts provided are intended to help users understand cybersecurity concepts and are not to be used maliciously.

---

Enjoy solving the challenges and exploring the world of *Mr. Robot*-themed CTFs!

