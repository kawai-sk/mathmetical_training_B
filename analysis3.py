#任意の2頂点間の最短距離を調べる(Floyd-Warshall法)

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
D = [[0 if i != j else 0 for j in range(N)]for i in range(N)]
K = int(input())
for i in range(K):
    a,b = map(int,input().strip().split(" "))
    D[a][b] = 1

#ここまでデータの読み込み
#以下でデータの解析
for k in range(N):#Floyd-Warshall法
    for i in range(N):
        for j in range(N):
            if D[i][k] > 0 and D[k][j] > 0:
                if D[i][j] == 0 or D[i][j] > D[i][k]+D[k][j]:
                    D[i][j] = D[i][k]+D[k][j]

countz = 0#距離不定な組合せの個数(CountZero
ave = 0#平均距離
M = 0#最大距離
for i in range(N):
    for j in range(N):
        a = D[i][j]
        if a == 0:#距離不定な組の数
            countz += 1
        else:#距離が定まる場合
            ave += a
            if M < a:
                M = a
print(countz/(N*N))
print(ave/(N*N-countz))
print(M)
