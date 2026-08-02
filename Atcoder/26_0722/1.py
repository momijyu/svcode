# https://kenkoooo.com/atcoder/#/contest/show/493e0b0c-20ae-49d9-b507-0f6ba90ce9fe
a, b, c = map(int,input().split())
ans = sum([a,b,c])
ans -= min([a,b,c])
print(ans) 