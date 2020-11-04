import sys
import json
from json import JSONEncoder

credential = ""
uri = ""
createPostMethod = False
createPutMethod = False
createDeleteMethod = False
createGetMethod = False

if len(sys.argv) > 1:
    credential = sys.argv[1]

if len(sys.argv) > 2:
    uri = sys.argv[2]

if len(sys.argv) > 3:
    createPostMethod = sys.argv[3]

if len(sys.argv) > 4:
    createPutMethod = sys.argv[4]

if len(sys.argv) > 5:
    createDeleteMethod = sys.argv[5]

if len(sys.argv) > 6:
    createGetMethod = sys.argv[6]

print("Credential: %s" % credential)
print("Uri: %s" % uri)


class PostModel:
    def __init__(self, tags, summary, description, operationId, consumes, produces, responses,
                 xAmazonApigatewayIntegration):
        self.tags = tags
        self.summary = summary
        self.description = description
        self.operationId = operationId
        self.consumes = consumes
        self.produces = produces
        self.responses = responses
        self.xAmazonApigatewayIntegration = xAmazonApigatewayIntegration


class PutModel:
    def __init__(self, tags, summary, description, operationId, consumes, produces, responses,
                 xAmazonApigatewayIntegration):
        self.tags = tags
        self.summary = summary
        self.description = description
        self.operationId = operationId
        self.consumes = consumes
        self.produces = produces
        self.responses = responses
        self.xAmazonApigatewayIntegration = xAmazonApigatewayIntegration


class DeleteModel:
    def __init__(self, tags, summary, description, operationId, produces, parameters, responses,
                 xAmazonApigatewayIntegration):
        self.tags = tags
        self.summary = summary
        self.description = description
        self.operationId = operationId
        self.produces = produces
        self.parameters = parameters
        self.responses = responses
        self.xAmazonApigatewayIntegration = xAmazonApigatewayIntegration


class GetModel:
    def __init__(self, tags, summary, description, operationId, produces, parameters, responses,
                 xAmazonApigatewayIntegration):
        self.tags = tags
        self.summary = summary
        self.description = description
        self.operationId = operationId
        self.produces = produces
        self.parameters = parameters
        self.responses = responses
        self.xAmazonApigatewayIntegration = xAmazonApigatewayIntegration


# subclass JSONEncoder
class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


# Method for parameter body
def my_parameter_function(name, inString, description, required, type, format):
    parameters = {'name': name, 'in': inString, 'description': description, 'required': required, 'type': type,
                  'format': format}
    return parameters


# Hardcoded body for responses
responses = {}
description200 = {'description': 'Successful operation.'}
description400 = {'description': 'Invalid ID supplied.'}
description404 = {'description': 'Not found.'}
description405 = {'description': 'Invalid input.'}

responses['200'] = description200
responses['400'] = description400
responses['404'] = description404
responses['405'] = description405

# Hardcoded body for xAmazonApigatewayIntegration
xAmazonApigatewayIntegration = {}

responsesXAmazonApigatewayIntegration = {}
statusCode = {'statusCode': '200'}
responsesXAmazonApigatewayIntegration['default'] = statusCode

xAmazonApigatewayIntegration['uri'] = uri
xAmazonApigatewayIntegration['responses'] = responsesXAmazonApigatewayIntegration
xAmazonApigatewayIntegration['passthroughBehavior'] = 'when_no_match'
xAmazonApigatewayIntegration['httpMethod'] = 'POST'
xAmazonApigatewayIntegration['contentHandling'] = 'CONVERT_TO_TEXT'
xAmazonApigatewayIntegration['type'] = 'aws'
xAmazonApigatewayIntegration['credentials'] = credential

# Call PostModel class to create post method body
post = PostModel(["todo"], "Add a new todo note", "", "addTodo", ["application/json", "application/xml"],
                 ["application/json", "application/xml"], responses, xAmazonApigatewayIntegration)

# Call DeleteModel class to create delete method body
delete = DeleteModel(["todo"], "Deletes a todo note", "", "deleteTodo", ["application/json", "application/xml"],
                     [my_parameter_function('api_key', 'header', '', 'false', 'string', ''),
                      my_parameter_function('todoId', 'path', 'Todo id to delete', 'true', 'integer', 'int64')],
                     responses,
                     xAmazonApigatewayIntegration)

# Call GetModel class to create get method body
get = GetModel(["todo"], "Find pet by ID", "Returns a single todo note", "getTodoById",
               ["application/json", "application/xml"],
               [my_parameter_function('todoId', 'path', 'Id of todo to return', 'true', 'integer', 'int64')],
               responses, xAmazonApigatewayIntegration)

# Call PutModel class to create put method body
put = PutModel(["todo"], "Update an existing todo note", "", "updateTodo", ["application/json", "application/xml"],
               ["application/json", "application/xml"], responses, xAmazonApigatewayIntegration)

# Add selected methods to existing swagger.json
with open('swagger.json', 'r') as json_file:
    data = json.load(json_file)

if createPostMethod:
    postjsondata = {'post': json.dumps(post.__dict__)}
    data['paths']['/todo'].append(postjsondata)
    print("Added post method.")

if createDeleteMethod:
    deletejsondata = {'delete': json.dumps(delete.__dict__)}
    data['paths']['/todo'].append(deletejsondata)
    print("Added delete method.")

if createGetMethod:
    getjsondata = {'get': json.dumps(get.__dict__)}
    data['paths']['/todo'].append(getjsondata)
    print("Added get method.")

if createPutMethod:
    putjsondata = {'put': json.dumps(put.__dict__)}
    data['paths']['/todo'].append(putjsondata)
    print("Added put method.")

with open('swagger.json', 'w') as json_file:
    json.dump(data, json_file)

print(data)
