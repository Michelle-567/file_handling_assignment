def main():
    file_name = "my_file.txt"

    # File Creation and Writing
    try:
        with open(file_name, 'w') as file:
            file.write("This is the first line.\n")
            file.write("This is the second line.\n")
            file.write("This is the third line with a number: 12345.\n")
        print(f"{file_name} created and written to successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # File Reading and Display
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print("\nContents of the file after writing:")
        print(content)
    except FileNotFoundError:
        print("File not found: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # File Appending
    try:
        with open(file_name, 'a') as file:
            file.write("This is an appended line one.\n")
            file.write("This is an appended line two.\n")
            file.write("This is an appended line three with a number: 67890.\n")
        print(f"{file_name} appended successfully.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e
        print(f"An error occurred: {e}")

    # File Reading and Display after Appending
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print("\nContents of the file after appending:")
        print(content)
    except FileNotFoundError:
        print("File not found: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
