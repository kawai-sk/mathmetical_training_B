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
for k in range(N):
    for i in range(N):
        for j in range(N):
            if D[i][k] > 0 and D[k][j] > 0:
                if D[i][j] == 0 or D[i][j] > D[i][k]+D[k][j]:
                    D[i][j] = D[i][k]+D[k][j]
ave = 0
countz = 0
M = 0
for i in range(N):
    for j in range(N):
        a = D[i][j]
        if a == 0:
            countz += 1
        else:
            ave += a
            if M < a:
                M = a
print(countz/(N*N))
print(ave/(N*N-countz))
print(M)
