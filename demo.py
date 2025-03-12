import sys

def main():
    print("Hello, Mahesh! This is a PyInstaller GitHub Actions demo.")
    if len(sys.argv) > 1:
        print(f"Arguments passed: {sys.argv[1:]}")
    else:
        print("No arguments provided.")
    input("\nPress Enter to exit...")  # This keeps the window open until you press Enter


if __name__ == "__main__":
    main()
