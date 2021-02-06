numq = list(range(1,10))
put_sign = int
X = "X"
O = "O"

print("\nCross-Null\n")

def plate_game(numq):
    print("-" * 13)
    for i in range(3):
        print("|", numq[0 + i * 3], "|", numq[1 + i * 3], "|", numq[2 + i * 3], "|")
        print("-" * 13)

def check_end(setq):
    win_exampl = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (7,5,3))
    for i in win_exampl:
        if setq[i[0]] == setq[i[1]] == setq[i[2]]:
            return setq[i[0]]
    return False


def inp_sign(put_sign):
    count = 1
    while count < 10:
        if count % 2 == 0:
            setq = O
        else:
            setq = X

        put_sign = int(input("Input sign from 1 till 9:" + " " + setq + "\n"))
        if  1 <= put_sign <= 9:
            if(str(numq[put_sign-1]) not in "XO"):
                numq[put_sign-1] = setq
                plate_game(numq)
                if check_end(numq):
                    count = 10
                    print("Win!")
                else:
                    count += 1
                continue
                
            else:
                print(' place is busy ')

        else:
            count -= 0
            print('incorrect sign')

    return put_sign

plate_game(numq)

inp_sign(put_sign)




