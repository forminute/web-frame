import  json
def get_name(args=[]):
	data = {}
	data['name'] = args['name']
	return json.dumps(data)