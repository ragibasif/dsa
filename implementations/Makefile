CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -pedantic -O2 -Wshadow -Wformat=2 \
		   -Wfloat-equal -Wconversion \
		   -Wcast-qual -Wcast-align -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC \
		   -fsanitize=address -fsanitize=undefined -fno-omit-frame-pointer \
		   -fno-sanitize-recover -fstack-protector -g

.PHONY: all
all: main
main: main.cpp
	@make clean
	@mkdir -p build
	@$(CXX) $(CXXFLAGS) $< -o build/$@
	@./build/main < input.txt
	@make clean

# Usage: 'make name' to compile name.cpp into an executable
%: %.cpp
	@mkdir -p build
	@$(CXX) $(CXXFLAGS) $< -o build/$@

clean:
	@rm -rf build
