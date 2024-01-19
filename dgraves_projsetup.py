import pathlib

def create_project_directory(directory_name: str):
    # Get the current working directory as a Path object
    current_directory = pathlib.Path.cwd()

    # Create a Path object for the new directory
    new_directory = current_directory.joinpath(directory_name)

    # Check if the directory already exists
    if not new_directory.exists():
        # Create the directory
        new_directory.mkdir()
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")

# Creating directories - test
def main():
    create_project_directory('test')
    create_project_directory('docs')
    create_project_directory('employee_data')
    create_project_directory('')

# Call the main function
if __name__ == "__main__":
    main()
