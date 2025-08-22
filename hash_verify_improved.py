#!/usr/bin/env python3
"""
Hash Verify - A Python script for file integrity verification
Supports multiple hash algorithms: MD5, SHA1, SHA256, SHA3-256, SHA512, SHA3-512
"""

import os
import sys
import hashlib
import argparse
from pathlib import Path


class HashVerifier:
    """Main class for hash verification functionality"""
    
    SUPPORTED_ALGORITHMS = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha3_256': hashlib.sha3_256,
        'sha512': hashlib.sha512,
        'sha3_512': hashlib.sha3_512,
    }
    
    # Default chunk size for large files (1MB)
    DEFAULT_CHUNK_SIZE = 1024 * 1024
    # Threshold for using chunked reading (4GB)
    CHUNK_THRESHOLD = 4 * 1024 * 1024 * 1024
    
    def __init__(self, chunk_size=None):
        self.chunk_size = chunk_size or self.DEFAULT_CHUNK_SIZE
    
    def normalize_algorithm_name(self, algorithm):
        """Normalize algorithm name to match supported algorithms"""
        algorithm = algorithm.lower().strip().replace('-', '')
        
        # Handle common variations
        if algorithm in ['sha3256', 'sha3_256']:
            return 'sha3_256'
        elif algorithm in ['sha3512', 'sha3_512']:
            return 'sha3_512'
        elif algorithm in self.SUPPORTED_ALGORITHMS:
            return algorithm
        else:
            # Try to find a match for partial names
            for algo in self.SUPPORTED_ALGORITHMS:
                clean_algo = algo.replace('_', '')
                if algorithm == clean_algo or algorithm in clean_algo or clean_algo in algorithm:
                    return algo
            return None
    
    def calculate_hash(self, file_path, algorithm):
        """
        Calculate hash for a file using the specified algorithm
        
        Args:
            file_path (str): Path to the file
            algorithm (str): Hash algorithm to use
            
        Returns:
            str: Calculated hash in hexadecimal format
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If algorithm is not supported
            IOError: If file cannot be read
        """
        # Validate file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if not os.path.isfile(file_path):
            raise ValueError(f"Path is not a file: {file_path}")
        
        # Normalize and validate algorithm
        normalized_algo = self.normalize_algorithm_name(algorithm)
        if not normalized_algo:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        hash_function = self.SUPPORTED_ALGORITHMS[normalized_algo]
        file_size = os.path.getsize(file_path)
        
        print(f"Calculating {normalized_algo.upper()} hash for: {file_path}")
        print(f"File size: {self._format_file_size(file_size)}")
        
        try:
            if file_size < self.CHUNK_THRESHOLD:
                # Read entire file for smaller files
                print("Reading entire file...")
                with open(file_path, 'rb') as file:
                    data = file.read()
                    return hash_function(data).hexdigest()
            else:
                # Read in chunks for large files
                print(f"Reading file in chunks of {self._format_file_size(self.chunk_size)}...")
                hash_obj = hash_function()
                with open(file_path, 'rb') as file:
                    while chunk := file.read(self.chunk_size):
                        hash_obj.update(chunk)
                return hash_obj.hexdigest()
                
        except IOError as e:
            raise IOError(f"Error reading file {file_path}: {e}")
    
    def verify_hash(self, file_path, expected_hash, algorithm):
        """
        Verify file hash against expected hash
        
        Args:
            file_path (str): Path to the file
            expected_hash (str): Expected hash value
            algorithm (str): Hash algorithm to use
            
        Returns:
            bool: True if hashes match, False otherwise
        """
        # Normalize expected hash (remove whitespace, convert to lowercase)
        expected_hash = expected_hash.strip().lower()
        
        try:
            calculated_hash = self.calculate_hash(file_path, algorithm)
            calculated_hash = calculated_hash.lower()
            
            print(f"\nHash Verification Results:")
            print(f"Algorithm:  {self.normalize_algorithm_name(algorithm).upper()}")
            print(f"Expected:   {expected_hash}")
            print(f"Calculated: {calculated_hash}")
            
            if expected_hash == calculated_hash:
                print("✅ VERIFICATION SUCCESSFUL - Hashes match!")
                return True
            else:
                print("❌ VERIFICATION FAILED - Hashes do not match!")
                return False
                
        except Exception as e:
            print(f"❌ VERIFICATION ERROR: {e}")
            return False
    
    def _format_file_size(self, size_bytes):
        """Format file size in human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} PB"
    
    @classmethod
    def list_supported_algorithms(cls):
        """List all supported hash algorithms"""
        return list(cls.SUPPORTED_ALGORITHMS.keys())


def interactive_mode():
    """Run in interactive mode with user prompts"""
    verifier = HashVerifier()
    
    print("=== Hash Verify - Interactive Mode ===")
    print(f"Supported algorithms: {', '.join(verifier.list_supported_algorithms())}")
    print()
    
    try:
        # Get algorithm
        while True:
            algorithm = input("Which hash algorithm to use? : ").strip()
            if verifier.normalize_algorithm_name(algorithm):
                break
            print(f"❌ Unsupported algorithm: {algorithm}")
            print(f"Supported: {', '.join(verifier.list_supported_algorithms())}")
        
        # Get file path
        while True:
            file_path = input("Enter the full path to the file: ").strip().strip('"\'')
            if os.path.exists(file_path) and os.path.isfile(file_path):
                break
            print(f"❌ File not found or not a file: {file_path}")
        
        # Get expected hash
        expected_hash = input("Enter the expected hash: ").strip()
        
        print()
        # Perform verification
        success = verifier.verify_hash(file_path, expected_hash, algorithm)
        return 0 if success else 1
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return 1


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Verify file integrity using various hash algorithms",
        epilog="Examples:\n"
               "  %(prog)s -f file.txt -a sha256 -e abc123...\n"
               "  %(prog)s --interactive\n"
               "  %(prog)s --list-algorithms",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('-f', '--file', help='Path to the file to verify')
    parser.add_argument('-a', '--algorithm', help='Hash algorithm to use')
    parser.add_argument('-e', '--expected', help='Expected hash value')
    parser.add_argument('-c', '--chunk-size', type=int, 
                       help='Chunk size for large files (bytes)')
    parser.add_argument('-i', '--interactive', action='store_true',
                       help='Run in interactive mode')
    parser.add_argument('-l', '--list-algorithms', action='store_true',
                       help='List supported hash algorithms')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0.0')
    
    args = parser.parse_args()
    
    # Handle special modes
    if args.list_algorithms:
        print("Supported hash algorithms:")
        for algo in HashVerifier.list_supported_algorithms():
            print(f"  {algo}")
        return 0
    
    if args.interactive or (not args.file and not args.algorithm and not args.expected):
        return interactive_mode()
    
    # Command-line mode
    if not all([args.file, args.algorithm, args.expected]):
        parser.error("In non-interactive mode, --file, --algorithm, and --expected are required")
    
    try:
        verifier = HashVerifier(chunk_size=args.chunk_size)
        success = verifier.verify_hash(args.file, args.expected, args.algorithm)
        return 0 if success else 1
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())