CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -pedantic -O2 -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wcast-qual -Wcast-align -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC -D_FORTIFY_SOURCE=2 -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -fstack-protector -g -DDEBUG=1

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
