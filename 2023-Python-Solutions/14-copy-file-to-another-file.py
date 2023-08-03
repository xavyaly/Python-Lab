# Python Program to Copy One File to Another File without removing the contents of another file

# To copy the contents of one file to another file in Python without removing the contents of the destination file, you can read the contents from the source file and then write them into the destination file. Here's a Python program to achieve that:

def copy_file(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as source:
            content = source.read()
        
        # Open the destination file for writing
        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        return "File copied successfully."
    except FileNotFoundError:
        return "Source file not found."
    except IOError:
        return "Error copying the file."

# Test the function
if __name__ == "__main__":
    source_file_path = "source.txt"          # Replace with the path of the source file
    destination_file_path = "destination.txt"  # Replace with the path of the destination file
    
    result = copy_file(source_file_path, destination_file_path)
    print(result)

# Replace `"source.txt"` and `"destination.txt"` with the paths of your source and destination files, respectively. The `copy_file()` function reads the contents from the source file using `source.read()` and then writes the contents into the destination file using `destination.write(content)`.

# Please make sure to provide the correct file paths in `source_file_path` and `destination_file_path` for the program to copy the contents properly.