#リンクの種別個数を調べる


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
    A[a][b] += 1

#ここまでデータの読み込み
#以下でデータの解析
def dfs1(p):
    global inp,inc,ouc,ntf
    visit[p] = 1
    for j in range(N):
        if A[p][j] > 0:
            if p == j:#同じページの中に出るリンク
                inp += A[p][j]
            elif nam[j] == " \"Out of domain\"":#サイト外に出るリンク
                ouc += A[p][j]
            elif nam[j] == " \"error 404\"":#NotFoundになるリンク
                ntf += A[p][j]
            else:#サイト内に出るリンク
                inc += A[p][j]
            if visit[j] == -1:
                dfs1(j)
visit = [-1]*N
inp = 0#ページ内リンク(InPage
inc = 0#サイト内リンク(InCite
ouc = 0#サイト外リンク(OutCite
ntf = 0#404エラーの出るリンク(NotFound
for i in range(N):
    if visit[i] == -1:
        dfs1(i)
print("ページ内リンク",inp)
print("サイト内リンク",inc)
print("サイト外リンク",ouc)
print("Not Found",ntf)
