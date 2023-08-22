install: ## Install required packages from requirements.txt
	python3 -m pip install --upgrade pip
	python3 -m pip install -U -r requirements.txt

format: ## Run black
	black onlinecourse/

flake8: ## Run flake8
	flake8 ./tests/ ./onlinecourse/

lint: ## Run pylint
	pylint --output-format=colorized ./tests/ ./onlinecourse/
	

refactor: ## Run black and lint
	format lint

test: ## Run tests
	pytest -vv --cov=./onlinecourse/ tests/

migrations:
	python3 manage.py makemigrations onlinecourse
	python3 manage.py migrate

write:
	python3 write.py

admin:
	python3 manage.py createsuperuser

runserver:
	python3 manage.py runserver