from sevenbridges.http.error_handlers import rate_limit_sleeper, maintenance_sleeper
import sevenbridges as sbg
import os
token = os.environ['CAVATIC_TURBO_TOKEN']
url = 'https://cavatica-api.sbgenomics.com/v2/'
api = sbg.Api(url, token, error_handlers=[rate_limit_sleeper, maintenance_sleeper])

pjt = 'kfdrc-harmonization/pbta-lancet-vardict-analysis'

tasks = list(api.tasks.query(pjt).all())

for t in tasks:
	if t.status == 'COMPLETED':
		cost = t.price.amount
		time = (t.end_time - t.start_time).total_seconds()/3600
		print "{}\t{}\t{}".format(t.name, cost, time)