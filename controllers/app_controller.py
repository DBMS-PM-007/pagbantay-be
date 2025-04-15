def api_controller(app):
    from controllers.user_router import user_router

    app.include_router(user_router, prefix='/users', tags=['User'])
