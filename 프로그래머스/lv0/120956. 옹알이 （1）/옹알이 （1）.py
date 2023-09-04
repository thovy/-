def solution(babbling):
    answer = 0
    can_word = ['aya', 'ye', 'woo', 'ma']
    
    def replace_word(bab):
        new_bab = bab
        for word in can_word:
            if len(new_bab) >= len(word) and new_bab[:len(word)] == word:
                # print('bab1', new_bab)
                new_bab = new_bab[len(word):]
                # print(new_bab)
        
#         if new_bab in can_word:
#             new_bab = replace_word(new_bab)

        return new_bab
            
    
    for bab in babbling:
        bab = replace_word(bab)
        bab = replace_word(bab)
        bab = replace_word(bab)
        bab = replace_word(bab)
        bab = replace_word(bab)
        bab = replace_word(bab)
        
        # print()
        
        if len(bab) < 1:
            # print(bab)
            answer += 1
            
    return answer