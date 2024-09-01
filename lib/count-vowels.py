def count_vowels(text):
    vowels = "aeiouAEIOU"  
    count = 0  
    for char in text: 
        if char in vowels:  
            count += 1  # Increment the counter if it's a vowel
    return count  # Return the total count of vowels

if __name__ == "__main__":

    test_strings = [
        "Mambo",
        "Keith",
        "Programming",
        "abcdeionmjk",
        "xyz"
    ]

    # Apply the function to each test string and print the result
    for s in test_strings:
        print(f"Number of vowels in '{s}': {count_vowels(s)}")
