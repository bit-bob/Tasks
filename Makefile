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
	.venv/bin/python api/gen_openapi.py openapi.json
	npm run generate-client

pretty:
	npx nx run-many -t prettier:fix

pytest:
	.venv/bin/pytest

clean: openapi pretty pytest

storybook:
	npx nx run components:storybook

run:
	./cxy.sh -fastapi ".venv/bin/python api/main.py"
