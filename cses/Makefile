CXX = clang++
CXXFLAGS = -std=c++17 -O2 -Wall -Wextra -Wshadow -g \
           -fsanitize=address -fsanitize=undefined \
           -fno-omit-frame-pointer -DLOCAL

TARGET = main

.PHONY: all
all: $(TARGET)

$(TARGET): main.cpp
	@$(CXX) $(CXXFLAGS) main.cpp -o $(TARGET)

.PHONY: run
run:
	@make clean
	@make all
	@./$(TARGET) < input.txt > output.txt
	@cat output.txt
	@make clean

.PHONY: clean
clean:
	@rm -rf $(TARGET) *.dSYM
