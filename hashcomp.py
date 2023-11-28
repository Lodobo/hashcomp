import sys, argparse, hashlib

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("files", metavar="FILE", nargs="+", help="Path to file")
    args = parser.parse_args()

    checksums = set()
    
    for file in args.files:
        with open(file, "rb") as f: # "rb" for binary   
            hexdigest = hashlib.file_digest(f, "sha256").hexdigest()
            checksums.add(hexdigest)
            print(hexdigest, file)
    
    if len(checksums) == 1:
        print("All checksums are identical")
    else:
        print("The checksums are different")

if __name__ == "__main__":
    main()   
   
