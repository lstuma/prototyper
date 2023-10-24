from http_utils import JSONRequest, JSONResponse

def not_found(request: JSONRequest):
    return JSONResponse(body={'error':f'the requested resource ({JSONRequest.path}) was not found'}, status=404)