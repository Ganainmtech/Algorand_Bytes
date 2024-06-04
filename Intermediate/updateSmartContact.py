


app_id = 123456  # Assume app_id is known
approval_program = b"new approval program bytecode"
clear_program = b"new clear program bytecode"

algorand.send.application_update(
    ApplicationUpdateParams(
        sender=deployer.address,
        app_id=app_id,
        approval_program=approval_program,
        clear_program=clear_program
    )
)




