def zipper(input1, input2):
    if len(input1) == len(input2):
        output = ""
        for i in range(len(input1)):
            output += input1[i]+input2[i]
        return output
    else:
        return "These strings will not work. Try again."

print(zipper("Cat","Dog"))
print(zipper("Test","tseT"))
print(zipper("Timber","Fellow"))
print(zipper("Yes","No"))