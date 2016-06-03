def guess_num(target_num, counts):
    b = 0
    while True:
        b += 1
        if b == counts:
            return "Coutn limit"
        s = int(input("enter a number:"))
        if s == target_num:
            return "You guess right!"
        elif s > target_num:
            print "s>target_num, guess again"
        else:
            print "s<target_num, guess again"

#result = guess_num(3,4)
#print result
