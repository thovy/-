def solution(id_list, report, k):
    answer = []
    
    # 신고받은 횟수
    spts = {id:set() for id in id_list}
    
    for i in report:
        rpt, spt = map(str, i.split())
        spts[spt].add(rpt)
    
    mail = {id:0 for id in id_list}
    for id in id_list:
        if len(spts[id]) >= k:
            for rpt in spts[id]:
                mail[rpt] += 1
    for i, v in mail.items():
        answer.append(v)
    
    
    return answer
