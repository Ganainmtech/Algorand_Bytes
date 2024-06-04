


app_id = 123456  # Assume app_id is known
algorand.send.application_delete(
    ApplicationDeleteParams(
        sender=deployer.address,
        app_id=app_id
    )
)


