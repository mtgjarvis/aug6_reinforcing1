

def ordinal(num):
    numstr = str(num)
    if num > 9:
        if int(numstr[-2:]) >= 10 and int(numstr[-2:]) <= 20:
            return(numstr + 'th')
        else:
            if numstr[-1] == '1':
                return(numstr + 'st')
            elif numstr[-1] == '2':
                return(numstr + 'nd')
            elif numstr[-1] == '3':
                return(numstr + 'rd')
            else:
                return(numstr + 'th')


print(ordinal(20))