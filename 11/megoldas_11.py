def kasszahoz_rendel_01(s):
	s = s.split(';')
	ret = [[], []]
	for n in s:
		if int(n)%2:
			ret[1].append(int(n))
		else:
			ret[0].append(int(n))
	ret[0].sort()
	ret[1].sort()
	return ret




def kasszahoz_rendel_02(s):
	s = s.split(';')
	
	parosak = []
	paratlanok = []

	for n in s:
		n = int(n)
		if n % 2 == 0:
			parosak.append(n)
		else:
			paratlanok.append(n)

	parosak.sort()
	paratlanok.sort()

	ret = [parosak, paratlanok]

	return ret


print(kasszahoz_rendel_01('42;38;45;40;41;39;44;43;46'))
print(kasszahoz_rendel_02('42;38;45;40;41;39;44;43;46'))

print(kasszahoz_rendel_01('12;16;14'))
print(kasszahoz_rendel_02('12;16;14'))