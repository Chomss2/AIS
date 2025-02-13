data = b'L|k\x80y+*^\x7f*zo\x7f\x82*\x80kvsno|*k\x80om*vo*zk}}*cyvksr\x7f\x14\n'
out = ""
for d in data.decode('latin-1'):
    out += chr(ord(d)-10)
print(out)