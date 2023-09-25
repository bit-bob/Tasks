venv:
	if [ ! -d "$(DIR1)" ]; then \
		python3 -m venv .venv; \
	fi

freeze:
	.venv/bin/pip freeze > requirements.txt

install_pip:
	.venv/bin/pip install -r requirements.txt

install_npm:
	npm install

install:
	.venv/bin/pip install -r requirements.txt
	npm install

openapi:
	.venv/bin/python backend/gen_openapi.py openapi.json
	openapi-generator generate -i ./openapi.json -g typescript-fetch -o ./frontend/packages/api

pretty:
	npx nx run-many -t prettier:fix

pytest:
	.venv/bin/pytest

test: pytest

clean: openapi pretty test

storybook:
	npx nx storybook tasks-client

run:
	./cxy.sh -fastapi ".venv/bin/python backend/main.py" -client "npx nx dev tasks-client"
