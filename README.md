# HashFD
Directory and File hasher

# ⚙️Storage Media Hasher

A Python-based utility to compute cryptographic hashes for files and directories.  
Supports popular hashing algorithms like `MD5`, `SHA1`, `SHA256`, and more.

---

## Features

- Compute the hash of a single file.
- Generate a consistent hash for an entire directory (includes file paths and contents).
- Support for multiple hashing algorithms (`md5`, `sha1`, `sha256`, `sha512`, etc.).
- Easy-to-use command-line interface with rich console output.

---

## Requirements

- Python 3.7 or later
- Libraries: `rich`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AkashMadanu/HashFD.git

   cd HashFD
   ```

Note: If you are using Linux, skip the next step.

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the script from the command line to hash files or directories.

### Hash a Single File
```bash
python hasher.py path/to/file.txt --algorithm sha256
```

### Hash an Entire Directory
```bash
python hasher.py path/to/directory --algorithm sha256
```

### Example Output
Hashing a file:
```
SHA256 Hash: 3a7bd3e2360a3d2a3ddc3c4c3e9e9b7c3b7ddc9c7d8e3a6b3c4a3e6b3d7e9f
```

Hashing a directory:
```
Hashing entire directory: ./example_directory
SHA256 Hash for directory: 6a8b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a
```

### Supported Algorithms
Use the `--algorithm` flag to specify the hashing algorithm:
- `md5`
- `sha1`
- `sha256` 
- `sha512`
  

---

## Project Structure

```
storage-media-hasher/
├── hasher.py            # Main script
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
```

---

## Contributing

Contributions are welcome! 
## License

This project is licensed under the [MIT License](LICENSE).
