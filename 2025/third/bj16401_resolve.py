import sys
m,n=map(int,sys.stdin.readline().split())
snack=list(map(int,sys.stdin.readline().split()))

start=1 #적어도 길이1로 잘라야 함.
end=max(snack) #자르는 길이의 최대는 과자 중 제일 긴 놈

answer=0
while start<=end:
    mid=(start+end)//2

    cnt=0
    for x in snack:
        if x<mid: #자르려는 단위보다 과자가 작으면 못 자름.
            continue
        else: #자르려는 단위보다 크면,
            cnt+=x//mid #그 과자를 해당 단위로 나눈 몫만큼 과자 나옴.

    if cnt>=m: #cnt가 너무 많으면 길이를 늘려야 함.
        start=mid+1
        answer=mid
    else: #cnt가 너무 적으면 길이를 줄여야 함
        end=mid-1

print(answer)