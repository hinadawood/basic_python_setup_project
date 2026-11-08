import platform
import sys

def main():
    name = input("Enter your name: ")
    print("Hello, World!")
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.system()} {platform.release()}")   

if __name__ == "__main__":
    main() 