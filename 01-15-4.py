s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'

s3 = """
hello,
world!
"""

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'

print(s1, s2, s3, end='')

a, b = 5, 12
print(f'{a}*{b} = {a * b}')