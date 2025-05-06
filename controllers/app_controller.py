def api_controller(app):
    from controllers.user_router import user_router
    from controllers.event_router import event_router
    from controllers.event_availability_router import event_availability_router
    from controllers.volunteer_assignment_router import volunteer_assignment_router

    app.include_router(user_router, prefix='/users', tags=['User'])
    app.include_router(event_router, prefix='/events', tags=['Events'])
    app.include_router(event_availability_router, prefix='/availability', tags=['Event Availability'])
    app.include_router(volunteer_assignment_router, prefix='/assignments', tags=['Volunteer Assignment'])
