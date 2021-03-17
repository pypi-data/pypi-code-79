import aiohttp_jinja2
from aiohttp import web


async def handle_401(request):
    return aiohttp_jinja2.render_template('401.html', request, {}, status=401)


async def handle_403(request):
    return aiohttp_jinja2.render_template('403.html', request, {}, status=403)


async def handle_404(request):
    return aiohttp_jinja2.render_template('404.html', request, {}, status=404)


async def handle_500(request):
    return aiohttp_jinja2.render_template('500.html', request, {}, status=500)


def create_error_middleware(overrides):

    @web.middleware
    async def error_middleware(request, handler):
        try:
            return await handler(request)
        except web.HTTPException as ex:
            override = overrides.get(ex.status)
            if override:
                return await override(request)

            raise
        except Exception:
            return await overrides[500](request)

    return error_middleware


def setup_error_pages(app=None):
    error_middleware = create_error_middleware({
        401: handle_401,
        403: handle_403,
        404: handle_404,
        500: handle_500
    })
    app.middlewares.append(error_middleware)
