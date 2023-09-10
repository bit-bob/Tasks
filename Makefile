venv:
	if [ ! -d "$(DIR1)" ]; then \
		python3 -m venv .venv; \
	fi

requirements:
	.venv/bin/pip install -r requirements.txt

freeze:
	.venv/bin/pip freeze > requirements.txt

npm_install:
	npm install

run:
	./cxy.sh -fastapi ".venv/bin/python main.py" -client "npm run dev"

storybook:
	npm run storybook
