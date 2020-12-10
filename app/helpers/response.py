from aiohttp import web

'''
    This helpers has custom response handlers
'''


def validation_error(non_valid_keys):
    keys = non_valid_keys if type(non_valid_keys) is list else [non_valid_keys]

    return web.json_response({
        'errors': [
            '[{}] parameter/s must be passed'.format(', '.join(keys))
        ]
    }, status=400)


def server_error(errors):
    return web.json_response({
        'errors': errors
    }, status=500)
