
text = open("input2.txt").read().strip()

lines = text.count("\n")
quotes = text.count(r'\"')
slashes = text.count(r'\\')
hexas = text.count(r'\x')
fake_hexas = text.count(r'\\x')
fake_fake_hexas = text.count(r'\\\x')
fake_quotes = text.count(r'\\"')
fake_fake_quotes = text.count(r'\\\"')


n_quotes = text.count('\"')
n_slashes = text.count('\\')

code = len(text) - lines
string = len(text) - lines - 2 * (lines + 1) - quotes - slashes - 3 * hexas \
     + fake_quotes - fake_fake_quotes + 3 * fake_hexas - 3 * fake_fake_hexas

string2 = len(text) - lines + 2 * (lines + 1) + n_slashes + n_quotes

print string2 - code
print n_quotes
print n_slashes
