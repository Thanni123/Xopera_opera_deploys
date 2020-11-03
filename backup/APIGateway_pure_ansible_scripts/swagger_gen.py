# script to generate swagger.yaml for api gateway (v0.1)
# Following libraries need to be installed: yaml

import yaml
import sys
import argparse


dict_header = {'swagger': '2.0', 'info': {'title': '{{ api_gateway_title }}', 'version': '2020-02-05T12:17:38Z'}, 'host': 'h8xiq5rvv8.execute-api.{{ aws_region }}.amazonaws.com', 
	'basePath': '/production', 'schemes' : ['https'], 'paths': {'/': {}}}

dict_post = {'post': {'tags': ['/'], 'summary': '{{ lambda_description }}', 'description': '{{ lambda_description }}', 'operationId': '{{ lambda_id }}',
	'consumes': ['application/json', 'application/xml'], 'produces': ['application/json', 'application/xml'], 'responses': 
	{'200': {'description': 'Successful operation'}, '405': {'description': 'Invalid input'}}, 'x-amazon-apigateway-integration':
	{'uri': '{{ api_gateway_resource_uri_override|default(api_gateway_resource_uri) }}', 'responses': {'default': {'statusCode': '200'}}, 'passthroughBehavior': 'when_no_match', 'httpMethod': 'POST', 
	'contentHandling': 'CONVERT_TO_TEXT', 'type': 'aws', 'credentials': '{{ aws_role }}'}}}

dict_put = {'put': {'tags': ['/'], 'summary': '{{ lambda_description }}', 'description': '{{ lambda_description }}', 'operationId': '{{ lambda_id }}',
	'consumes': ['application/json', 'application/xml'], 'produces': ['application/json', 'application/xml'], 'responses': 
	{'200': {'description': 'Successful operation'}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Not found'}, '405': {'description': 'Invalid input'}}, 'x-amazon-apigateway-integration':
	{'uri': '{{ api_gateway_resource_uri_override|default(api_gateway_resource_uri) }}', 'responses': {'default': {'statusCode': '200'}}, 'passthroughBehavior': 'when_no_match', 'httpMethod': 'POST', 
	'contentHandling': 'CONVERT_TO_TEXT', 'type': 'aws', 'credentials': '{{ aws_role }}'}}}

dict_get = {'get': {'tags': ['/'], 'summary': '{{ lambda_description }}', 'description': '{{ lambda_description }}', 'operationId': '{{ lambda_id }}',
	'produces': ['application/json', 'application/xml'], 'parameters': [{'name': '', 'in': 'path', 'description': '', 'required': 'true', 'type': 'integer', 'format': 'int64'}], 'responses': {'200': {'description': 'Successful operation'}, 
	'400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Not found'}}, 'x-amazon-apigateway-integration': {'uri': '{{ api_gateway_resource_uri_override|default(api_gateway_resource_uri) }}', 'responses': {'default': {'statusCode': '200'}}, 
	'passthroughBehavior': 'when_no_match', 'httpMethod': 'POST', 'contentHandling': 'CONVERT_TO_TEXT', 'type': 'aws', 'credentials': '{{ aws_role }}'}}}

dict_delete = {'delete': {'tags': ['/'], 'summary': '{{ lambda_description }}', 'description': '{{ lambda_description }}', 'operationId': '{{ lambda_id }}',
	'produces': ['application/json', 'application/xml'], 'parameters': [{'name': 'api_key', 'in': 'header', 'required': 'false', 'type': 'string'}, {'name': '', 'in': 'path', 'description': '', 'required': 'true', 'type': 'integer', 'format': 'int64'}], 
	'responses': {'200': {'description': 'Successful operation'}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Not found'}}, 'x-amazon-apigateway-integration': {'uri': '{{ api_gateway_resource_uri_override|default(api_gateway_resource_uri) }}', 
	'responses': {'default': {'statusCode': '200'}}, 'passthroughBehavior': 'when_no_match', 'httpMethod': 'POST', 'contentHandling': 'CONVERT_TO_TEXT', 'type': 'aws', 'credentials': '{{ aws_role }}'}}}

# NOTE: If parser is needed
# parser = argparse.ArgumentParser(description='Generate swagger file for API Gateway.')
# parser.add_argument("--addHttpMethod", help='type post, put, delete or get to add HTTP methods (default: empty)')
# parser.add_argument('--addPathKey', help='add optional path key to swagger file (default: empty)')
# args = parser.parse_args()

# Count the arguments
arguments = len(sys.argv) - 1

# Iterate through argument based on key word
for x in sys.argv[1:]:
	if x == 'post':
		dict_header['paths']['/'].update(dict_post)
		print("Post method added.")
	elif x == 'get':
		dict_header['paths']['/'].update(dict_get)
		print("Get method added.")
	elif x == 'put':
		dict_header['paths']['/'].update(dict_put)
		print("Put method added.")
	elif x == 'delete':
		dict_header['paths']['/'].update(dict_delete)
		print("Delete method added.")

#--------------------------------------------------------------------------------------------------
# NOTE: Linux directory
#with open(r'/home/phong/Desktop/swagger.yaml', 'w') as file:
#    documents = yaml.dump(dict_header, file, default_flow_style=False)

# NOTE: Windows directory
with open(r'C:\\Users\\thanh\\Desktop\\ToDo_deploy\\swagger.yaml', 'w') as file:
    documents = yaml.dump(dict_header, file, default_flow_style=False)