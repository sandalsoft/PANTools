import pan.xapi

API_KEY = 'LUFRPT13WjRsY25CeDFLYm9YQkc3QkdQQTVwVHZ6L2s9Y3ZYbXZmazZib2J6UXpwNkNZOGJkdz09'
HOST = '192.168.55.10'

try:
	xapi = pan.xapi.PanXapi(api_key=API_KEY, hostname=HOST)
except pan.xapi.PanXapiError as msg:
	print('edit: ' + msg)
	sys.exit(1)

xpath = "/config/devices/entry/vsys/entry/rulebase/security/rules/"
xpath += "entry[@name='api_delete_rule']/disabled"
element = "<disabled>yes</disabled>"

try:
	xapi.edit(xpath=xpath, element=element)
except pan.xapi.PanXapiError as msg:
	print('edit: ' + msg)
	sys.exit(1)

print('policy disabled')
