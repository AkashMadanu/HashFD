import hashlib
import os
import argparse
from rich.console import Console

console = Console()

def compute_directory_hash(directory_path, algorithm="sha256"):
    
    hash_func = getattr(hashlib, algorithm)()
    console.print(f"[bold cyan]Hashing entire directory:[/bold cyan] {directory_path}")

    for root, _, files in sorted(os.walk(directory_path)):
        for file in sorted(files):  
            file_path = os.path.join(root, file)
            file_hash = compute_file_hash(file_path, algorithm)
            if file_hash:
                
                hash_func.update(file_path.encode())  
                hash_func.update(file_hash.encode())  

    return hash_func.hexdigest()

def compute_file_hash(file_path, algorithm="sha256"):
    """
    Compute the hash of a single file.
    Reads the file in chunks to handle large files efficiently.
    """
    hash_func = getattr(hashlib, algorithm)()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192): 
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        console.print(f"[bold red]Error: File not found - {file_path}[/bold red]")
        return None
    except Exception as e:
        console.print(f"[bold red]Error reading file {file_path}: {e}[/bold red]")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Directory and File Hasher")
    parser.add_argument("path", help="Path to the file or directory to hash")
    parser.add_argument("--algorithm", choices=hashlib.algorithms_guaranteed, default="sha256", help="Hash algorithm to use")

    args = parser.parse_args()

    if os.path.isfile(args.path):
        
        file_hash = compute_file_hash(args.path, args.algorithm)
        if file_hash:
            console.print(f"[bold green]{args.algorithm.upper()} Hash:[/bold green] {file_hash}")
    elif os.path.isdir(args.path):
        
        dir_hash = compute_directory_hash(args.path, args.algorithm)
        console.print(f"[bold green]{args.algorithm.upper()} Hash for directory:[/bold green] {dir_hash}")
    else:
        console.print("[bold red]Error: Invalid path provided. Please specify a file or directory.[/bold red]")
