'''
def middlewarename(get_response):
    code which is required only one time
    execution.For initialization or configuration.

    def your_function(request):

        code to be executed before view function is called.
        variable=get_response(request)
        code to be exeuted after view function is called

        return response
    
    return your_function

'''
'''
def todo_middleware(get_response):

    print("Code to be excecuted only once for Initialization")

    def todo_function(request):

        print("code to be exceuted before view function")
        res=get_response(request)

        print("code to be excecuted after view function")

        return res

    return todo_function

'''

class todo_middleware:

    def __init__(self,get_response):
        self.get_response=get_response
        print('From class base: Code to be excecuted only once for Initialization')

    def __call__(self,request):
        print('From class base:code to be exceuted before view function')
        res=self.get_response(request)

        print('From class base:code to be excecuted after view function')
        return res