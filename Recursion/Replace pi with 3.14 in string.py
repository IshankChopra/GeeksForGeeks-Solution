def replace(s):
    if len(s) == 0:
        return
    else:
        if s[0] == "p" and s[1] == "i":
            print("3.14", end="")
            replace(s[2:])
        else:
            print(s[0], end="")
            replace(s[1:])


s = "pipypipkpi"
replace(s)
