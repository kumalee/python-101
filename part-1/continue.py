a = 10

while True:
	s = int(raw_input('Enter an int:'))
	if s == a:
	    print 's == a'
            break
	elif s > a:
	    print 's > a, go on'
            continue
	print 's < a'
