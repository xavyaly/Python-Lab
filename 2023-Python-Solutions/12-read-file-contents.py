# Write a Python Program to read the contents of a file

# To read the contents of a file in Python, you can use the built-in `open()` function to open the file and then read its contents using different methods. Here's a Python program to read the contents of a file:

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except IOError:
        return "Error reading the file."

# Test the function
if __name__ == "__main__":
    file_path = "example.txt"  # Replace with the path to your file
    file_contents = read_file(file_path)
    print(file_contents)

# Replace `"example.txt"` with the path to your file that you want to read. The `read_file()` function opens the file in read mode (`'r'`) and reads its contents using `file.read()`. It returns the contents of the file as a string.

# Note that the program handles two possible exceptions: `FileNotFoundError` and `IOError`. These exceptions can occur if the file is not found or if there is an error while reading the file. In both cases, the program will return an appropriate error message.

# Make sure to provide the correct file path in the `file_path` variable for the program to read the contents of your desired file.

# ---------------------------------------------------------------------------------------------------------------------

# Execution Output

# python3 13-read-file-contents.py 
# hello pytho, can you please write a complex problem for me ??

# python3 13-read-file-contents.py 
# hello pytho, can you please write a complex problem for me ??
# hello pytho, can you please write a complex problem for me ??
# hello pytho, can you please write a complex problem for me ??
# hello pytho, can you please write a complex problem for me ??
# hello pytho, can you please write a complex problem for me ??
# hello pytho, can you please write a complex problem for me ??
# hello pytho, can you please write a complex problem for me ??