# pdf3j

**pdf3j** is a Python utility package designed to convert PDF files to Markdown (`.md`) and text (`.txt`) formats using the PyMuPDF and PyMuPDF4LLM libraries. This package provides command-line interface (CLI) tools to facilitate easy and efficient conversion of PDF documents for tasks such as training language models, creating documentation, or extracting plain text.

## Features

- **PDF to Markdown Conversion**: Extracts the content of a PDF file into a Markdown file using PyMuPDF4LLM's `to_markdown` method.
- **PDF to Text Conversion**: Extracts the content of a PDF file into a plain text file using PyMuPDF.

## Installation

You can install the package using `pip`:

```sh
pip install git+https://github.com/echoRedOx/pdf3j.git
```

## Usage

The package provides two CLI commands: `pdf-to-md` and `pdf-to-txt`.

### Converting PDF to Markdown

To convert a PDF file to Markdown format, use the following command:

```sh
pdf-to-md /path/to/your/file.pdf
```

This will create a `.md` file with the same name as the original PDF in the same directory.

### Converting PDF to Text

To convert a PDF file to plain text format, use the following command:

```sh
pdf-to-txt /path/to/your/file.pdf
```

This will create a `.txt` file with the same name as the original PDF in the same directory.

## Examples

### PDF to Markdown

```sh
pdf-to-md example.pdf
```

This command will generate a file named `example.md` with the content extracted from `example.pdf`.

### PDF to Text

```sh
pdf-to-txt example.pdf
```

This command will generate a file named `example.txt` with the content extracted from `example.pdf`.

## Dependencies

- `pymupdf4llm`
- `pymupdf`

Make sure to install these dependencies before running the scripts.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

Created by [echoRedOx](mailto:echodevs@proton.me).
