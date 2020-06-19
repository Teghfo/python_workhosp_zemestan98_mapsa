# f = open('mapsa.txt', 'w')  # w (write) r (read) a (append)   type(t, b)
# # f.seek(8)

# f.write('kheili goshnamuneh')

# f.close()

f = open('mapsa.txt', 'r+')  # w (write) r (read) a (append)   type(t, b)

res = f.read()

f.write('lkglewjghb')

print(res)