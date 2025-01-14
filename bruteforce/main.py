import PyPDF2
import sys 


## Usage: python script.py <path_to_pdf> <path_passsword_file>

def check_pdf_password(input_pdf, list_password):
    try:
        with open(input_pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # to Check if the PDF is encrypted
            if reader.is_encrypted:
                # Attempt to decrypt with the provided password
                for password in list_password:
                    if reader.decrypt(password.strip()):
                        print(f"hurry , The correct password is : {password}")
                        return True 
            else:
                print("This PDF is not encrypted.")
                return None 
            
            print("Password not found...!")
            return False 
        
    except Exception as e:
        print(f"Error: {e}")
        return None 

def load_password(file_path):
    try:
        with open(file_path , 'r') as file:
            return file.readlines()
    except Exception as e:
        print(f"ERROR:{e}")
    return None 

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_pdf> <path_passsword_file>")
        sys.exit(1)
    
    input_pdf = sys.argv[1]  # Path to the PDF
    file_path = sys.argv[2]   # Password to unlock the PDF

    input_password = load_password(file_path)
    if input_password:
        check_pdf_password(input_pdf , input_password)

if __name__ == "__main__":
    main()
