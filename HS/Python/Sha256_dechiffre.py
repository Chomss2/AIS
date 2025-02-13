import hashlib
from typing import Optional

def find_matching_word(target_hash: str, wordlist_path: str) -> Optional[str]:
    """
    Attempts to find a word that matches a given SHA-256 hash by checking against a wordlist.
    
    Args:
        target_hash: The SHA-256 hash to match (hexadecimal string)
        wordlist_path: Path to the wordlist file
        
    Returns:
        The matching word if found, None otherwise
    """
    # Convert target hash to lowercase for consistent comparison
    target_hash = target_hash.lower()
    
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                # Remove whitespace and newlines
                word = line.strip()
                
                # Calculate SHA-256 hash of the current word
                word_hash = hashlib.sha256(word.encode('utf-8')).hexdigest()
                
                # Check if hashes match
                if word_hash == target_hash:
                    return word
                    
        return None
        
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_path}' not found.")
        return None
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

def main():
    # Example usage
    target_hash = input("Enter the SHA-256 hash to match: ")
    wordlist_path = input("Enter the path to your wordlist file: ")
    
    print("\nSearching for matching word...")
    result = find_matching_word(target_hash, wordlist_path)
    
    if result:
        print(f"\nMatch found! The word is: {result}")
    else:
        print("\nNo match found in the wordlist.")

if __name__ == "__main__":
    main()