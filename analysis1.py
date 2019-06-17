#拡張子を観察することでファイルの種類を調べる

def dfs1(p):
    visit[p] = 1
    d = urls[p][-3:]
    if d in data:
        data[d] += 1
    else:
        data[d] = 1
    for j in range(N):
        if A[p][j] == 1 and visit[j] == -1:
            dfs1(j)
url = input()
N = int(input())
urls = []
nam = []
for i in range(N):
    a = input().strip().split(" ")
    urls.append(a[1])
    s = ""
    for i in range(2,len(a)):
        s += " " + a[i]
    nam.append(s)
A = [[0 for j in range(N)]for i in range(N)]
k = int(input())
for i in range(k):
    a,b = map(int,input().strip().split(" "))
    A[a][b] = 1
visit = [-1]*N
data = {}
for i in range(N):
    if visit[i] == -1:
        dfs1(i)
for k,v in sorted(data.items(),key = lambda x:-x[1]):
    print(str(k)+" "+str(v))
