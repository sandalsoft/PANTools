import socket
import pan.xapi
import sys

PA_API_KEY = 'LUFRPT13WjRsY25CeDFLYm9YQkc3QkdQQTVwVHZ6L2s9Y3ZYbXZmazZib2J6UXpwNkNZOGJkdz09'
PA_HOST = '192.168.55.10'

HOSTNAME = 'www.paloaltonetworks.com'
DAG_OBJECT = 'my dag object'
DAG_XML_FNAME = 'dns2dag.xml'
xmlFh=open('./' + DAG_XML_FNAME, 'w+')


ip = socket.gethostbyname(HOSTNAME)

xmlString = '''
	<uid-message>
	<version>1.0</version>
	<type>update</type>
	<payload>
		<register>
			<entry identifier="''' + DAG_OBJECT + '''" ip="''' + ip + '''"/>        
		</register>            
	</payload>  
	</uid-message>
	'''

xmlFh.write(xmlString)
DAG_POST_XML_PATH = 'https://' + PA_HOST + '/api/?type=user-id&action=set&key=' + PA_API_KEY + '=&file-name=' + DAG_XML_FNAME + '&client=PANTool'




sys.exit(1)

try:
	xapi = pan.xapi.PanXapi(api_key=PA_API_KEY, hostname=PA_HOST)
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