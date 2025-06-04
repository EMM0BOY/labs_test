s = 'Pyth1abc2hon'
first_h = s.find('h')
last_h = s.rfind('h')

substring = s[first_h + 1:last_h]
reversed_substring = substring[::-1]
new_string = s[:first_h + 1] + reversed_substring + s[last_h:]

print("Новая строка:", new_string)