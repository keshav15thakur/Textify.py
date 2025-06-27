import string

def remove_punctuation(text):
    return ''.join(ch for ch in text if ch not in string.punctuation)

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def remove_extra_spaces(text):
    return ' '.join(text.split())

def count_characters(text):
    return len(text)

def count_words(text):
    return len(text.split())

def show_menu():
    print("\n--- TEXTIFY: Text Utilities Tool ---")
    print("1. Remove punctuation")
    print("2. Convert to UPPERCASE")
    print("3. Convert to lowercase")
    print("4. Remove extra spaces")
    print("5. Count characters")
    print("6. Count words")
    print("7. Exit")

def main():
    text = input("Enter your text:\n> ")
    
    while True:
        show_menu()
        choice = input("\nChoose an operation (1-7): ")

        if choice == '1':
            text = remove_punctuation(text)
            print("Updated Text:\n", text)
        elif choice == '2':
            text = to_uppercase(text)
            print("Updated Text:\n", text)
        elif choice == '3':
            text = to_lowercase(text)
            print("Updated Text:\n", text)
        elif choice == '4':
            text = remove_extra_spaces(text)
            print("Updated Text:\n", text)
        elif choice == '5':
            print("Character Count:", count_characters(text))
        elif choice == '6':
            print("Word Count:", count_words(text))
        elif choice == '7':
            print("Exiting... Thank you for using Textify!")
            break
        else:
            print("Invalid option! Please choose between 1-7.")

if __name__ == "__main__":
    main()