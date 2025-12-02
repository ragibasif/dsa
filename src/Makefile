BUILD_DIR := build
CXX := clang++
DBG := lldb
CXXFLAGS := -std=c++20 \
		  -pedantic -Wall -Wextra -Wvla -Wshadow \
		  -Wno-unused-parameter -Wwrite-strings -Wstrict-prototypes \
		  -Wold-style-cast -Wredundant-decls -Wnested-externs \
		  -Wmissing-include-dirs \
		  -Wconversion -Wfloat-equal -Wswitch -Wimplicit-fallthrough \
		  -fno-sanitize-recover -fsanitize=address -fsanitize=undefined \
		  -fno-omit-frame-pointer -fno-optimize-sibling-calls \
		  -fstack-protector-all -Wstack-protector \
		  -MMD -MP \
		  -g3 -O0 -DDEBUG=1 -D_GLIBCXX_DEBUG \
		  -DTEST=1

LDFLAGS := # -lm  -I some/path/to/library

SRC := main.cpp
OBJ := $(BUILD_DIR)/main.o
TARGET := $(BUILD_DIR)/main

.PHONY: default
default: all

.PHONY: all
all: $(TARGET)

$(TARGET): $(OBJ)
	@$(CXX) -o $@ $^ $(CXXFLAGS) $(LDFLAGS)

$(BUILD_DIR)/main.o: main.cpp
	@mkdir -p $(BUILD_DIR)
	@$(CXX) -c $< -o $@ $(CXXFLAGS) $(LDFLAGS)

.PHONY: run
run:
	@make clean
	@make all
	@./$(TARGET)
	@make clean


.PHONY: debug
debug:
	@make clean
	@make all
	@$(DBG) ./$(TARGET)

.PHONY: clean
clean:
	@rm -rf $(BUILD_DIR)

.PHONY: test
test:
	@make clean
	@make all
	@./$(TARGET) < input.txt
	@make clean


