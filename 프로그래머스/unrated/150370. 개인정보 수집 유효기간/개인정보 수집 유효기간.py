def solution(today, terms, privacies):
    answer = []

    ty,tm,td = map(int, today.split('.'))
    
    termlist = []
    for i in terms:
        termlist.append(list(map(str, i.split())))
        
    prvclist = []
    for i in privacies:
        day, term = map(str, i.split())
        y, m, d = map(int, day.split('.'))
        prvclist.append([y, m, d, term])
    
    for term in termlist:
        for idx, prvc in enumerate(prvclist, start=1):
            if term[0] == prvc[-1]:
                year = prvc[0] + ((int(term[1]) + prvc[1])//12)
                month = int((int(term[1]) + prvc[1])%12)
                print(year, month)
                if month == 0:
                    year -= 1
                    month = 12
                
                if year < ty:
                    answer.append(idx)
                elif year == ty and month < tm:
                    answer.append(idx)
                elif year == ty and month == tm and prvc[2] <= td:
                    answer.append(idx)
                    
                
    answer.sort()
    return answer