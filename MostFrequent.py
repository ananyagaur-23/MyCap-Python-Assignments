def mf(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    sorted_chars = sorted(freq, key=freq.get, reverse=True)
    
    for char in sorted_chars:
        print(char, '=', freq[char], end=' ')

s=input("Please enter a string: ")
mf(s)

