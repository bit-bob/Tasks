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
	npm run prettier:fix

clean:
	.venv/bin/python api/gen_openapi.py openapi.json
	npm run generate-client
	npm run prettier:fix
	.venv/bin/pytest

test:
	.venv/bin/pytest

storybook:
	npm run storybook

run:
	./cxy.sh -fastapi ".venv/bin/python api/main.py" -client "npm run dev"
