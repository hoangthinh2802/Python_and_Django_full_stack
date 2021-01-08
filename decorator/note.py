def new_decorator(func):
    def wrap_funs():
        print("CODE HERE BEFORE EXUCUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")
    return wrap_funs

def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")

func_needs_decorator = new_decorator(func_needs_decorator)