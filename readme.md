# OpenDownloader
OpenDownloader is a command-line tool for downloading files from URLs.

<img width="1200" alt="Facebook post - 3" src="https://github.com/uppriezdev/OpenDownloader/assets/99713905/1a6ccba9-0463-4d34-a80b-56f188bbacda">

## Features

- Concurrent downloads with configurable maximum connections
- Progress visualization using tqdm
- Support for specifying output directory and force download option
- Show information about the application using `about` command

## Installation

Clone the repository:

```
git clone https://github.com/uppriezdev/OpenDownloader.git
```

Install the dependencies:

```
pip install -r requirements.txt
```

## Usage

To download files, use the following command:

```
python opendownloader.py --max-connections <num_connections> <URL1> <URL2> ... --output-dir <output_directory> --force-download
```

To see information about the application, use the `about` command:

```
python opendownloader.py about
```

## Example

Download a file with 8 maximum connections:

```
python opendownloader.py --max-connections 8 https://example.com/file.zip --output-dir downloads
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## Inspiration

This project drew inspiration from [Aria2c](https://aria2.github.io/), a lightweight multi-protocol & multi-source command-line download utility.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
