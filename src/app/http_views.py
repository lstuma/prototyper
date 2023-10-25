from http_utils import JSONRequest, JSONResponse

def not_found(request: JSONRequest):
    return JSONResponse(body={'error':f'the requested resource ({request.path}) was not found'}, status=404)

def welcome(request: JSONRequest):
    return JSONResponse(body={'welcome':f'Prototyper'})

# place your views here