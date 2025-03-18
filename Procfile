web: PYTHONPATH=$(pip show waitress | grep Location | cut -d' ' -f2) python3 -m waitress --listen=0.0.0.0:$PORT app:app
