msg-extract:
	pybabel extract -F babel.cfg -o locale/pyschool.pot templates/*.html

msg-update:
	pybabel update -i locale/pyschool.pot -l es -d locale/
	pybabel update -i locale/pyschool.pot -l en -d locale/

msg-build:
	pybabel compile -d locale -f 
