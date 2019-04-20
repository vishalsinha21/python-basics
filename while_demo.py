s = 'tata consultancy services limited'

count = 0;
index = 0;
length = len(s)

while index < length:
    if (s[index] in ['a', 'e', 'i', 'o', 'u']):
        count += 1;
    index += 1;

print(count)
