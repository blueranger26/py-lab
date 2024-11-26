def process_file(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Check if the file is empty
        if not content.strip():
            print("The input file is empty. Please enter some text.")
            user_input = input("Enter text to save to the file: ")
            with open(input_file, 'w') as infile:
                infile.write(user_input)
            content = user_input

        # Process the content
        lines = content.splitlines()
        words = content.split()
        characters = len(content)

        line_count = len(lines)
        word_count = len(words)

        # Write the results to the output file
        with open(output_file, 'w') as outfile:
            outfile.write("File Processing Results:\n")
            outfile.write(f"Number of lines: {line_count}\n")
            outfile.write(f"Number of words: {word_count}\n")
            outfile.write(f"Number of characters: {characters}\n")

        print(f"Data has been processed and saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for the file '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main Program
input_file = "input.txt"  # Replace with your input file path
output_file = "output.txt"  # Replace with your output file path

process_file(input_file, output_file)
