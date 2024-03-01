# File Organizer

This Python script organizes files from a source directory into respective destination directories based on file types.

## Prerequisites

- Python 3.x installed on your system.

## Installation

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:

    ```bash
    python __main__.py
    ```

## Usage

1. Open `__main__.py` in a text editor.
2. Set the `source_directory` and `destination_directory` variables to the paths of your source and destination directories, respectively.
3. Save the file.
4. Run the script as mentioned in the Installation section.

## Features

- Organizes files into directories based on their types.
- Supports various file types including images, documents, videos, audio, compressed files, installers, data files, web files, databases, and others.

## Example

Suppose you have files in your `Downloads` directory and you want to organize them:

```python
if __name__ == '__main__':
    source_directory = 'C:/Users/YourUsername/Downloads'
    destination_directory = 'C:/Users/YourUsername/Downloads/Organized'
    organize_files(source_directory, destination_directory)
```
## Contributing

Contributions are welcome! Please follow these guidelines:
- Fork the repository.
- Create your feature branch (`git checkout -b feature/YourFeature`).
- Commit your changes (`git commit -am 'Add some feature'`).
- Push to the branch (`git push origin feature/YourFeature`).
- Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
