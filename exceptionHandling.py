def handle_exceptions():
    try:
        # Ask the user to enter a number to simulate ValueError
        number = input("Enter a number: ")  # User input as a string
        number = int(number)  # Try to convert the input to an integer (may raise ValueError)
        print(f"You entered the number: {number}")

        # Ask the user for the second input
        second_input = input("Enter something to add to the number (it can be a number or a string): ")

        # Try to add number and second_input if it's a number
        try:
            second_number = float(second_input)  # Try to convert to a number (may raise ValueError)
            result = number + second_number
            print(f"Result: {result}")
        except ValueError:
            # If second_input can't be converted to a number, raise TypeError
            result = number + second_input  # This should raise TypeError if second_input is a string
            print(f"Result: {result}")

        # Ask the user to input the file name to simulate FileNotFoundError
        filename = input("Enter the name of the file to open (e.g., 'nonexistent.txt'): ")
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except ValueError:
        print("Error: You entered an invalid number. Please enter a valid integer.")
    
    except TypeError:
        print("Error: You tried to perform an invalid operation (e.g., adding a number to a string).")
    
    except FileNotFoundError:
        print("Error: The specified file was not found. Please check the file name and try again.")
    
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Program execution completed.")

# Main Program
handle_exceptions()
