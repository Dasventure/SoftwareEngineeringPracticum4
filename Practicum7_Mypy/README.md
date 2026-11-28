# Mypy - generate reports

- cd pull_requests
- rm -rf reports/*
- mypy
- mypy > reports/errors.txt
- mypy -O json > reports/errors.json
- ls -R reports/
- xdg-open reports/html/index.html
