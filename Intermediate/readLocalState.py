


account_info = algorand.account.get_information(account)
local_state = next(app['local-state'] 
                   for app in account_info['apps-local-state'] 
                   if app['id'] == app_id)
print(local_state)


