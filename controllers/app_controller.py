def api_controller(app):
    from controllers.user_router import user_router
    from controllers.event_router import event_router

    app.include_router(user_router, prefix='/users', tags=['User'])
    app.include_router(event_router, prefix='/events', tags=['Events'])
