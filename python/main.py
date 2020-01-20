from prtty import pretty

def hello(request):
    pretty(dir(request))
    pretty(request.json)
    return "Hello world!"
    