def kaprekarRoutine(len, lead):
    for i in range(int("1".ljust(len+1, "0"))):
        res = int("1".ljust(len+1, "0"))
        depth = 0
        asc, dsc = sortDigits(i, len, lead)
        while(res != dsc - asc):
            res = dsc - asc
            print(f"{res} = {dsc} - {asc}")
            asc, dsc = sortDigits(res, len, lead)
            depth += 1
        print(f"Start: {i}, End: {res}, Depth: {depth}", "\n")

def sortDigits(num, len, lead):
    if(lead):
        temp = str(num).zfill(len)
    else:
        temp = str(num)
    digits = [digit for digit in temp]
    return int("".join(sorted(digits))), int("".join(sorted(digits, reverse=True)))