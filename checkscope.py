def check_scope():
    def do_local():
        test = "local text" #ith print aavanel print local aayi kodkkanam

    def do_non_local():
        nonlocal test #thottumunne(local)nte value marum
        test = "non local text"

    def do_global():
        global test #global aayi value change aavum
        test = "global text"

    test = "default"
    do_local()
    print("the value after do local is:" + test)
    do_non_local()
    print("the value after non do local is:" + test)
    do_global()
    print("the value after do global is :" + test)

check_scope()
print("the value after main" + test)
