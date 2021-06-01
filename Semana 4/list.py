def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        a = sentence.split()
        words = len(a)
        # Only proceed if n is not more than the number of words
        if words >= n > 0:
            c = a[n - 1]
            return (c)
    return ("")


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing
