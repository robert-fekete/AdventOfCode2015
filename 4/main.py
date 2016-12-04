import md5

prefix = "ckczppom"

def calc(prefix):

    suffix = 1
    key = prefix + str(suffix)
    m = md5.new()
    m.update(key)
    hash = m.digest()

    while not check2(hash):
        suffix += 1
        key = prefix + str(suffix)

        m = md5.new()
        m.update(key)
        hash = m.digest()

    return suffix

def check(hash):

    return ord(hash[0]) == 0 and ord(hash[1]) == 0 and ord(hash[2]) < 16

def check2(hash):

    return ord(hash[0]) == 0 and ord(hash[1]) == 0 and ord(hash[2]) == 0

print calc(prefix)