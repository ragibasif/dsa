CXX = clang++
CXXFLAGS = -std=c++20 -Wall -Wextra -pedantic -O2 -Wshadow -Wformat=2 \
		   -Wfloat-equal -Wconversion \
		   -Wcast-qual -Wcast-align -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC \
		   -fsanitize=address -fsanitize=undefined -fno-omit-frame-pointer \
		   -fno-sanitize-recover -fstack-protector -g -DLOCAL

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

.PHONY: check
check:
	@$(CXX) --version | head -n 1

.PHONY: clean
clean:
	@rm -rf build
