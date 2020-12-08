def string_test(word_input):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for letters in word_input:
        if letters.isupper():
           d["UPPER_CASE"]+=1
        elif letters.islower():
           d["LOWER_CASE"]+=1
    print ("Original String : ", word_input)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

print(string_test('Hello world!'))