test: lexer code_generation


lexer: Test/lexer_test.py
	python3 Test/lexer_test.py

code_generation: Test/code_generation.py
	python3 Test/code_generation.py

main: src/main.py
	cd src && make run && cd ..

