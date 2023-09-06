def solution(id_pw, db):
    answer = ''
    
    db_dict = dict()
    for d in db:
        db_dict[d[0]] = d[1]
    
    inid, inpw = id_pw[0], id_pw[1]
    
    if inid in db_dict.keys():
        if db_dict[inid] == inpw:
            return 'login'
        else:
            return 'wrong pw'
    else:
        return 'fail'