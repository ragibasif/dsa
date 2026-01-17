CXX = g++-15
CXXFLAGS = -std=c++17 -O2 -Wall -Wextra -Wshadow -D_GLIBCXX_DEBUG

# Usage: 'make name' to compile name.cpp into an executable
%: %.cpp
	@mkdir -p build
	@$(CXX) $(CXXFLAGS) $< -o build/$@

clean:
	@rm -rf build
