help:		   	## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

format:			## format with ssort, isort and black
	@sh -c " \
		pdm run ssort buti/**; \
		pdm run ssort tests/**; \
		pdm run isort .; \
		pdm run black . \
	"

mypy:			## check types with mypy
	pdm run mypy

test: 			## run tests and check code (ssort, isort, black, mypy)
	@sh -c " \
		pdm run pytest --cov=buti tests; \
		pdm run mypy; \
		pdm run ssort --check buti/**; \
		pdm run ssort --check tests/**; \
		pdm run isort --check-only buti/**; \
		pdm run black --check ."


test-ff:		## test and fail fast, providing details
	pdm run pytest -l -s -x


.PHONY: format test test-ff mypy help
