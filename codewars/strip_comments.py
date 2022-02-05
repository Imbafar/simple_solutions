def func(string, comment):
    string = string.split("\n")
    new_str = []
    for st in string[:]:
        f = False
        for i in comment:
            idx = st.find(i)
            if idx != -1:
                new_str.append(st[0:idx].strip())
                f = True
                continue
        if not f:
            new_str.append(st)
    return "\n".join(new_str)


result = func("apples, pears\ngrapes\nbananas\nbananas #!#apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
print(result)
