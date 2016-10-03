import connexion
import datetime
import logging
# use as memory storage for employees
EMPS = {}

def post_asset(emp_name, emp):
	exists = emp_name in EMPS
	emp['name'] = emp_name
	if exists:
		logging.info('Employee Record exists %s...', emp_name)
		return 'Record exist please use PUT request', 409
	else:
		logging.info('Creating employee %s...', emp_name)
		emp['taken_at'] = datetime.datetime.now()
		EMPS[emp_name] = emp
	return emp, 201

def get_emps(name=None):
	return [emp for emp in EMPS.values() if not name or emp['name'] == name]
	
def delete_emp(emp_name):
	if emp_name in EMPS:
		logging.info('Deleting Employee %s..', emp_name)
		del EMPS[emp_name]
		return 'Employee record deleted', 204
	else:
		return 'Employee record does not exist.', 404

def put_emp(emp_name, emp):
	exists = emp_name in EMPS
	emp['name']=emp_name
	if exists:
		logging.info('Updating pet %s..', emp_name)
		EMPS[emp_name].update
		(emp)
		return 'Record updated ', 200
	else:
		logging.info('Record does not exists %s..', emp_name)
		return 'Not found', 404






if __name__ == '__main__':
	app = connexion.App(__name__, 9091, specification_dir='swagger/')
	app.add_api('emp-api.yaml')
	app.run()