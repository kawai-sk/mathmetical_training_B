#拡張子を観察することでファイルの種類を調べる

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

#ここまでデータの読み込み
#以下でデータの解析
def dfs1(p):
    visit[p] = 1
    d = urls[p][-3:]#拡張子の抜粋
    if d in data:#既知の拡張子をカウント
        data[d] += 1
    else:#未知の拡張子を追加
        data[d] = 1
    for j in range(N):
        if A[p][j] == 1 and visit[j] == -1:
            dfs1(j)
visit = [-1]*N
data = {}#拡張子名を変数名としてその個数を収納する
for i in range(N):
    if visit[i] == -1:
        dfs1(i)
for k,v in sorted(data.items(),key = lambda x:-x[1]):
    print(str(k)+" "+str(v))
