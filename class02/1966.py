from sys import stdin
n = int(stdin.readline())
result = []
for _ in range(n):
    # N : 문서의 개수, M : 몇 번째로 인쇄되었는지 궁금한 문서 인덱스
    N, M = map(int, stdin.readline().split())
    # data : N개의 문서의 중요도 리스트
    data = list(map(int, stdin.readline().split()))
    
    # out : 출력한 횟수, 즉 몇 번째로 출력했는지 의미
    out = 0
    
    # t : 타겟(궁금한 문서)의 인덱스
    t = M
    
    while(True):
        # 9 1 '1' 1 9 9     out=0 t=2
        # 1 '1' 1 9 9       out=1 t=1
        # '1' 1 9 9 1             t=0
        # 1 9 9 1 '1'             t=len(list)-1=4
        # 9 9 1 '1' 1             t=3
        # 9 1 '1' 1         out=2 t=2
        # 1 '1' 1           out=3 t=1
        # '1' 1             out=4 t=0
        # '1' 출력          out=5
        
        # 첫 번째 데이터가 최대 우선순위일 경우 (출력함)
        if data[0] == max(data):
            # 출력 횟수 증가
            out+=1
            # 첫 번째 데이터가 최대 우선순위면서 타겟일 경우
            if t==0:
                # 결과에 몇 번째 출력인지 추가하고 종료
                result.append(out)
                break;
            # 첫 번째 데이터가 최대 우선순위이라서 출력은 하지만 타겟이 아닐 경우
            else:
                # 타겟 인덱스 앞으로 1 당김
                t-=1
                # 출력한 데이터 삭제 (큐에서 빠져나감)
                del data[0]
        # 첫 번째 데이터가 최대 우선순위가 아닐 경우 (출력하지않음)
        else:
            # 첫 번째 데이터가 타겟일 경우
            if t==0:
                # 첫 번째 데이터를 끝에 추가하고
                # 첫 번째 데이터를 지움
                data.append(data[0])
                del data[0]
                # 타겟의 인덱스는 맨 뒤로 이동 (타겟의 인덱스가 0이기 때문)
                t=len(data)-1
            # 첫 번째 데이터가 타겟이 아닌 경우
            else:
                # 첫 번째 데이터를 끝에 추가하고
                # 첫 번째 데이터를 지움
                data.append(data[0])
                del data[0]
                # 타겟 인덱스 앞으로 1 당김
                t-=1

for i in result:
    print(i)
