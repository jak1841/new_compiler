test: lexer


lexer: Test/lexer_test.py
	python3 Test/lexer_test.py

main: src/main.py
	cd src && make run && cd ..

