
format:
	@sh -c " \
		pdm run ssort boots/**; \
		pdm run ssort tests/**; \
		pdm run isort .; \
		pdm run black . \
	"

test:
	@sh -c " \
		pdm run pytest --cov=boots tests; \
		pdm run mypy; \
		pdm run ssort --check boots/**; \
		pdm run ssort --check tests/**; \
		pdm run isort --check-only boots/**; \
		pdm run isort --check-only .; \
		pdm run black --check ."


test-ff:		## test and fail fast, providing details
	pdm run pytest -l -s -x

.PHONY: format test
