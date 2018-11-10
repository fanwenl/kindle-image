import hashlib

f = open('file_path', 'rb')

sh = hashlib.sha256()
sh.update(f.read())
print(sh.hexdigest())

f.close()