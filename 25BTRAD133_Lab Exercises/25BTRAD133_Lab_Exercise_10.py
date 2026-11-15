# USN: 25BTRAD133
# Lab Exercise 10: Frequency Counter Using Dictionaries
# Description: Count the frequency of words in a sentence or occurrences of elements in a list using dictionaries[cite: 12].

def frequency_counter():
    print("=" * 45)
    print("       DICTIONARY FREQUENCY COUNTER       ")
    print("=" * 45)
    print("1. Count word frequency in a sentence")
    print("2. Count element frequency in a list")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        sentence = input("\nEnter a sentence: ")
        # Split sentence into words and convert to lowercase for consistency
        words = sentence.split()
        freq = {}
        
        for word in words:
            word = word.lower().strip(".,!?")
            # Using dictionary get() to initialize and increment frequency[cite: 13]
            freq[word] = freq.get(word, 0) + 1
            
        print("\n--- Word Frequency Results ---")
        print(f"{'Word':<15} | {'Frequency':<10}")
        print("-" * 30)
        for word, count in freq.items():
            print(f"{word:<15} | {count:<10}")
        print("-" * 30)
        
    elif choice == '2':
        elements_input = input("\nEnter elements separated by spaces (e.g., apple banana apple): ")
        elements = elements_input.split()
        freq = {}
        
        for item in elements:
            freq[item] = freq.get(item, 0) + 1
            
        print("\n--- Element Frequency Results ---")
        print(f"{'Element':<15} | {'Frequency':<10}")
        print("-" * 30)
        for item, count in freq.items():
            print(f"{item:<15} | {count:<10}")
        print("-" * 30)
        
    else:
        print("Invalid selection! Please restart and select 1 or 2.")

if __name__ == "__main__":
    frequency_counter()