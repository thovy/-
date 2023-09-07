def solution(lines):
    answer = 0
    
    # 여기선 필요없지만 정렬
    lines = sorted(lines, reverse=True)
    
    # 겹치는 부분
    overlaps = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            # 앞선 첫 끝점이([i][1]) 뒤이어오는 시작점([j][0])보다 크고 - 겹칠 때
            # 앞선 시작점([i][0])이 뒤어어오는 끝점([j][1])보다 작을 때 - 나는 sorted 를 해서 상관 없음.
            if lines[i][1] >= lines[j][0] and lines[i][0] <= lines[j][1]:
                # 겹치는 부분의 시작점은 앞선 시작점이나 뒤이어오는 것의 시작점 중에 큰 것
                overlap_start = max(lines[i][0], lines[j][0])
                # 겹치는 부분의 끝점은 두 끝 점 중에 작은 것
                overlap_end = min(lines[i][1], lines[j][1])
                # 겹치는 구간 길이 계산
                overlap_length = overlap_end - overlap_start
                
                # 중복 계산 방지
                # overlaps 를 차례로 꺼내면서 현재 계산 된 overlap_start, overlap_end와 비교
                for start, end in overlaps:
                    # 새로운 시작점이 기존 끝점보다 작을 때
                    # 새로운 끝점이 기존 시작점 보다 클 때 - 중복되어 겹쳐진다고 본다(이어지는 걸로 볼 수 있겠지).
                    if overlap_start <= end and overlap_end >= start:
                        # 겹쳐지고 있다면 두 시작점 중 작은 것을 시작점으로 본다.
                        overlap_start = min(overlap_start, start)
                        # 겹쳐지고 있다면 두 끝점 중 큰 것을 끝점으로 본다.
                        overlap_end = max(overlap_end, end)
                        # 구간이 변겨됐으니 새롭게 계산해서 계산
                        overlap_length = overlap_end - overlap_start
                        # 기존 구간 삭제
                        overlaps.remove((start, end))
                # 새로운 구간 추가
                overlaps.append((overlap_start, overlap_end))
    # 총 길이
    # overlaps 에 들어있는 구간들을 모두 계산해서 더하기
    answer = sum([end - start for start, end in overlaps])
    
    return answer
                        
                
                