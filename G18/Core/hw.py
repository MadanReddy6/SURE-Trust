s='malayalam'
# rev_s = ''


s = "helleoh"
s_rev = s[::-1]

if s == s_rev:
    print(-1)

for i in range(len(s)):
    if s[i] != s_rev[i]:
        s_del = s[:i]+s[i+1:] 
        s_rev_del = s_rev[:len(s)-i-1]+s_rev[len(s)-i:]

        if s_del == s_rev_del:
            print(i)