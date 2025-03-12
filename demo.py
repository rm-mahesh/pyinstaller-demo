import sys

def main():
    print("Hello, Mahesh! This is a PyInstaller GitHub Actions demo.")
    i = 0
    while i < 50000:
        print(i)
        i += 1
    if len(sys.argv) > 1:
        print(f"Arguments passed: {sys.argv[1:]}")
    else:
        print("No arguments provided.")
    


if __name__ == "__main__":
    main()
