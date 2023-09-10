venv:
    if [ ! -d "$(DIR1)" ]; then \
        python3 -m venv .venv; \
    fi
