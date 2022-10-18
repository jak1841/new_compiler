test: lexer code_generation


lexer: Test/lexer_test.py
	python3 Test/lexer_test.py

code_generation: Test/code_generation_test.py
	python3 Test/code_generation_test.py

main: src/main.py
	cd src && make run && cd ..

