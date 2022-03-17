with open('a.txt', 'r') as f1, open('b.txt', 'w') as f2:
    for i in f1:
        f2.write(i)