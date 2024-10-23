def all_variants(text):
    for number in range(len(text)):
        for i in range(len(text)-number):
            result = text[i:i+number+1]
            yield result

a = all_variants("abc")
for i in a:
    print(i)