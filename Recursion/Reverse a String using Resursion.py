def reverse(s):
    if len(s) == 0:
        return ()
    else:
        r = s[1:]
        reverse(r)
        print(s[0], end="")


reverse("ishank chopra")
