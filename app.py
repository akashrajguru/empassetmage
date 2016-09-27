import connexion
import datetime
import logging
# use as memory storage for employees
EMPS = {}

def post_asset(emp_name, emp):
	exists = emp_name in EMPS
	emp['name'] = emp_name
	if exists:
		logging.info('Updating employee %s...', emp_name)
		EMPS[emp_name].update(emp)
	else:
		logging.info('Creating employee %s...', emp_name)
		emp['taken_at'] = datetime.datetime.utcnow()
		EMPS[emp_name] = emp
	return emp, (409 if exists else 201) 

def get_emps(name=None):
	return [emp for emp in EMPS.values() if not name or emp['name'] == name]
	



if __name__ == '__main__':
	app = connexion.App(__name__, 9091, specification_dir='swagger/')
	app.add_api('emp-api.yaml')
	app.run()