def solution(babbling):
    answer = 0
    
    for bab in babbling:
        can_bab = ['aya', 'ye', 'woo', 'ma']
        spare_bab = []
        while can_bab:
            inbab=bab
            outbab=inbab
            for cb in can_bab:
                if len(bab) >= len(cb) and bab[:len(cb)] == cb:
                    can_bab.remove(cb)
                    spare_bab.append(cb)
                    if len(spare_bab) >=2:
                        can_bab.append(spare_bab[0])
                        spare_bab.remove(spare_bab[0])
                    bab = bab[len(cb):]
                    outbab = bab
            if inbab == outbab:
                break
        
        if len(bab) == 0:
            answer += 1
            
    return answer