# Python Program to Copy One File to Another File and append the contents of destination file

# To copy the contents of one file to another file in Python and append the contents of the destination file, you can read the contents from both files, concatenate them, and then write the result into the destination file. Here's a Python program to achieve that:

def copy_file_and_append(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as source:
            source_content = source.read()
        
        # Open the destination file for reading
        with open(destination_file, 'r') as destination:
            destination_content = destination.read()
        
        # Concatenate the contents and write to the destination file
        with open(destination_file, 'a') as destination:
            destination.write('\n' + source_content + '\n')
        
        return "File copied and appended successfully."
    except FileNotFoundError:
        return "Source or destination file not found."
    except IOError:
        return "Error copying the file."

# Test the function
if __name__ == "__main__":
    source_file_path = "source.txt"          # Replace with the path of the source file
    destination_file_path = "destination.txt"  # Replace with the path of the destination file
    
    result = copy_file_and_append(source_file_path, destination_file_path)
    print(result)

# Replace `"source.txt"` and `"destination.txt"` with the paths of your source and destination files, respectively. The `copy_file_and_append()` function reads the contents from both the source file and the destination file, concatenates them with a newline in between (`'\n'`), and then writes the result into the destination file using the append mode (`'a'`).

# Please make sure to provide the correct file paths in `source_file_path` and `destination_file_path` for the program to copy and append the contents properly.


# Execution Output

# python3 15-append-contents-to-destination.py 
# File copied and appended successfully.