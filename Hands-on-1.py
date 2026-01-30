word = input("Please enter a word: ")

word_length = len(word)

numbers = []

for i in range(word_length):
    num = int(input(f"\nEnter number {i + 1}: "))
    numbers.append(num)
    
def get_average(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        total += num
    return total / len(list_of_numbers)
    
def compare(word_len, avg, word):
    if word_len < avg:
        print(f"\nThe length of the word '{word}' is less than the average.")
    elif word_len > avg:
        print(f"\nThe length of the word '{word}' is greater than the average.")
    else:
            print(f"\nThe length of the word '{word}' is equal to the average.")
        
average = get_average(numbers)

print(f"\n{numbers}")
print(f"\nThe length of the word is {word_length}")
print(f"\nThe Average of the numbers is {average}")


compare(word_length, average, word)
