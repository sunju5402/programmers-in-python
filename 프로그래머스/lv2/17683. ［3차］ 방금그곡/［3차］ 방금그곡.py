def solution(m, musicinfos):
    l = []
    for mu in musicinfos:
        s, e, t, c = mu.split(",") # 시작시간, 끝나는 시간, 제목, 악보 정보
        s1, s2 = s.split(":") # 시작시간 시, 분
        e1, e2 = e.split(":") # 끝나는 시간 시, 분
        c = c.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        time = (int(e1) * 60 + int(e2)) - (int(s1) * 60 + int(s2)) # 총 재생시간(분)
        
        cnt = time // len(c) # 악보가 반복되는 횟수
        code = c * cnt + c[:time % len(c)] # 총 재생시간동안 연주된 음
        
        m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        
        if m in code:
            l.append((time, t))
        

    l.sort(reverse=True, key=lambda x:x[0]) # 재생된 시간이 제일 긴 음악, 같을 경우 먼저 입력된 음악 
    if not len(l):
        return "(None)"
    else:
        return l[0][1]