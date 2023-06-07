
format:
	@sh -c " \
		pdm run ssort buti/**; \
		pdm run ssort tests/**; \
		pdm run isort .; \
		pdm run black . \
	"

test:
	@sh -c " \
		pdm run pytest --cov=buti tests; \
		pdm run mypy; \
		pdm run ssort --check buti/**; \
		pdm run ssort --check tests/**; \
		pdm run isort --check-only buti/**; \
		pdm run isort --check-only .; \
		pdm run black --check ."


test-ff:		## test and fail fast, providing details
	pdm run pytest -l -s -x

.PHONY: format test
