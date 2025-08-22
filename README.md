
# Hash-Verify

Hash-Verify is a powerful and user-friendly Python script designed to verify file integrity using various hash algorithms. It supports both interactive and command-line modes, making it versatile for different use cases.

## ✨ Features

- **Multiple Hash Algorithms**: Supports MD5, SHA1, SHA256, SHA3-256, SHA512, and SHA3-512
- **Two Usage Modes**: Interactive mode for beginners, command-line mode for automation
- **Smart File Handling**: Automatically handles large files with chunked reading for memory efficiency
- **Robust Error Handling**: Clear error messages and validation for files and algorithms
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **User-Friendly**: Clear output with progress indicators and colored status messages
- **Easy Installation**: Can be installed as a package or used as a standalone script

## 🚀 Installation

### Option 1: Install as Package (Recommended)
```bash
# Clone the repository
git clone https://github.com/buggymaytricks/Hash-Verify.git
cd Hash-Verify

# Install as a package
pip install .

# Now you can use it from anywhere
hash-verify --help
```

### Option 2: Use as Standalone Script
```bash
# Clone the repository
git clone https://github.com/buggymaytricks/Hash-Verify.git
cd Hash-Verify

# Run directly
python3 hash_verify_improved.py --help
```

### Option 3: Legacy Version
The original version is still available as `hash-verify.py` for backward compatibility.

## 📖 Usage

### Interactive Mode (Recommended for beginners)

Simply run the script without arguments to enter interactive mode:

```bash
hash-verify
# or
python3 hash_verify_improved.py
```

The script will guide you through:
1. Selecting a hash algorithm
2. Choosing the file to verify  
3. Entering the expected hash value

### Command-Line Mode (Great for automation)

```bash
hash-verify -f <file_path> -a <algorithm> -e <expected_hash>
```

**Examples:**
```bash
# Verify a file with SHA256
hash-verify -f document.pdf -a sha256 -e abc123...

# Verify with SHA512
hash-verify -f image.jpg -a sha512 -e def456...

# Use different chunk size for very large files
hash-verify -f large_file.zip -a sha256 -e 789xyz... --chunk-size 2097152
```

### Available Options

```bash
hash-verify --help
```

- `-f, --file`: Path to the file to verify
- `-a, --algorithm`: Hash algorithm (md5, sha1, sha256, sha3_256, sha512, sha3_512)
- `-e, --expected`: Expected hash value
- `-c, --chunk-size`: Custom chunk size for large files (bytes)
- `-i, --interactive`: Force interactive mode
- `-l, --list-algorithms`: Show supported algorithms
- `-v, --version`: Show version information

## 🔧 Supported Algorithms

- **MD5** - For legacy compatibility (not recommended for security)
- **SHA1** - For legacy compatibility (not recommended for security)  
- **SHA256** - Recommended for most use cases
- **SHA3-256** - Latest standard, very secure
- **SHA512** - For maximum security
- **SHA3-512** - Latest standard with maximum security

## 📋 Examples

### Example 1: Verify a Downloaded File

Let's say you downloaded a Linux ISO and want to verify its integrity:

```bash
# Interactive mode
hash-verify

# Follow the prompts:
# Which hash algorithm to use? : sha256
# Enter the full path to the file: /home/user/ubuntu-22.04.iso  
# Enter the expected hash: d5b537c69...
```

### Example 2: Automated Verification Script

```bash
#!/bin/bash
# Verify multiple files automatically
hash-verify -f file1.zip -a sha256 -e hash1... && \
hash-verify -f file2.tar -a sha512 -e hash2... && \
echo "All files verified successfully!"
```

### Example 3: Handle Large Files

For files larger than 4GB, the script automatically uses chunked reading:

```bash
hash-verify -f very_large_file.img -a sha256 -e expected_hash...
# The script will show: "Reading file in chunks of 1.0 MB..."
```

## 🆚 What's New in Version 2.0

### ✅ Improvements Over Original Version

1. **Fixed Critical Bugs**: SHA512 and SHA3-512 now work correctly
2. **Eliminated Code Duplication**: Single generic function handles all algorithms
3. **Better User Experience**: Clear prompts, progress indicators, colored output
4. **Command-Line Support**: Can be automated with scripts
5. **Proper Error Handling**: Validates files, algorithms, and handles edge cases
6. **Easy Installation**: Can be installed as a Python package
7. **Memory Efficient**: Smart chunking for large files
8. **Cross-Platform**: Better path handling for Windows, macOS, Linux

### 🔧 Technical Improvements

- Object-oriented design with `HashVerifier` class
- Comprehensive input validation and normalization
- Configurable chunk sizes for different use cases
- Proper exit codes for script automation
- Type hints and documentation strings
- Follows Python best practices

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues & Fixes

- **Fixed**: SHA512 and SHA3-512 functions now use correct hash algorithms
- **Fixed**: Typos in variable names ("orignal" → "original")
- **Improved**: Better algorithm name parsing and validation
- **Enhanced**: Memory usage for large files through smart chunking

## 🔮 Future Enhancements

- GUI version for non-technical users
- Batch processing for multiple files
- Configuration file support
- Additional hash algorithms (BLAKE2, etc.)
- Progress bars for very large files
- Integration with cloud storage services