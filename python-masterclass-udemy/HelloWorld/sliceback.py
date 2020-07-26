letters = "abcdefghijklmnopqrstuvwxyz"

# for slicing always make sure that the start value should always be greater than the stop value

backwards3 = letters[25:0:-1]
backwards1 = letters[25::-1]
backwards2 = letters[-1:-26:-1]
backwards = letters[::-1]
print(backwards3)
print(backwards1)
print(backwards2)
print(backwards)

# below is a mini challenge from video 33

print()

slice_qpo = letters[-10:-13:-1]
slice_same_as_above = letters[16:13:-1]
print(slice_qpo)
print(slice_same_as_above)

slice_edcba = letters[4::-1]
print(slice_edcba)


slice_last8_in_reverse_order = letters[:-9:-1]
print(slice_last8_in_reverse_order)

# below are important python idioms
print("\n\n\n")

print(letters[-4:])  # this is going forward
print(letters[-1:])  # this is going forward
print(letters[:1])   # this idiom will by pass the code to crash if the sequence is empty
print(letters[0])

