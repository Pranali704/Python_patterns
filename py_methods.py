text = " Welocme to IMCC! "

print("Upper case:",text.upper())
print(text.lower())

text = text.strip()
print("Capitalize First letters :" , text.capitalize())


print(text.title())


print("Remove spaces",text.strip())

#6 count occurence of a substring
print(" Letter C occurs ",text.count("C"), "times in text")

#7 poition
print(text.find("IMCC"))

#replace a substring
print(text.replace("IMCC", "Python Magic"))

#check that a substring starts or end with certain substring
print(text.startswith(" We"))
print(text.endswith("! "))

#split string
print("Simple split: ",text.split())

#join words
word = ["Python","is","fun"]
print(" ".join(word))



