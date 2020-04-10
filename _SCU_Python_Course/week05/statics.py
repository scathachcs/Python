def juege(string, percent):
    if (percent > 0.01):
        print(string + ' %{}\n'.format(int(percent * 100)))
    elif (percent == 0):
        pass
    else:
        print(string + ' <%1\n')


a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0
filename = input("请输入文件名：")
with open(filename, 'r') as file:
    for line in file:
        a += line.count('a')
        a += line.count('A')
        b += line.count('b')
        b += line.count('B')
        c += line.count('c')
        c += line.count('C')
        d += line.count('d')
        d += line.count('D')
        e += line.count('e')
        e += line.count('E')
        f += line.count('f')
        f += line.count('F')
        g += line.count('g')
        g += line.count('G')
        h += line.count('h')
        h += line.count('H')
        i += line.count('i')
        i += line.count('I')
        j += line.count('j')
        j += line.count('J')
        k += line.count('k')
        k += line.count('K')
        l += line.count('l')
        l += line.count('L')
        m += line.count('m')
        m += line.count('M')
        n += line.count('n')
        n += line.count('N')
        o += line.count('o')
        o += line.count('O')
        p += line.count('p')
        p += line.count('P')
        q += line.count('q')
        q += line.count('Q')
        r += line.count('r')
        r += line.count('R')
        s += line.count('s')
        s += line.count('S')
        t += line.count('t')
        t += line.count('T')
        u += line.count('u')
        u += line.count('U')
        v += line.count('v')
        v += line.count('V')
        w += line.count('w')
        w += line.count('W')
        x += line.count('x')
        x += line.count('X')
        y += line.count('y')
        y += line.count('Y')
        z += line.count('z')
        z += line.count('Z')
num = a + b + c + d + e + f + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z

juege('A', a / num)
juege('B', b / num)
juege('C', c / num)
juege('D', d / num)
juege('E', e / num)
juege('F', f / num)
juege('G', g / num)
juege('H', h / num)
juege('I', i / num)
juege('J', j / num)
juege('K', k / num)
juege('L', l / num)
juege('M', m / num)
juege('N', n / num)
juege('O', o / num)
juege('P', p / num)
juege('Q', q / num)
juege('R', r / num)
juege('S', s / num)
juege('T', t / num)
juege('U', u / num)
juege('V', v / num)
juege('W', w / num)
juege('X', x / num)
juege('Y', y / num)
juege('Z', z / num)
