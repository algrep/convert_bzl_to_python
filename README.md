# Convert .bzl to requirements.txt

This repository contains a Python script to convert Maven dependencies listed in a `.bzl` file into a `requirements.txt` format. This can be useful for managing dependencies in a format compatible with other tools or for sharing dependency lists.

## Prerequisites

- Python 3.x

## Script Usage

1. Ensure the `.bzl` file containing the dependencies is ready.
2. Run the script from the command line as follows:

   ```bash
   python3 convert_bzl_to_requirements.py <input.bzl> <output_requirements.txt>
