# File: Makefile
# Author: Ragib Asif
# GitHub: https://github.com/ragibasif
# LinkedIn: https://www.linkedin.com/in/ragibasif/
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Ragib Asif
# Version 1.0.0

RESET:=\033[0m
BOLD:=\033[1m
GREEN:=\033[0;92m
RED:=\033[0;91m
MAGENTA:=\033[0;95m
CYAN:=\033[0;96m

ERROR:=$(BOLD)$(RED)
SUCCESS:=$(BOLD)$(GREEN)
INFO:=$(BOLD)$(CYAN)

CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Wvla -O1 -g3 -pedantic -v -fsanitize=address,undefined -fno-omit-frame-pointer -fno-optimize-sibling-calls -Wshadow -Wconversion -Wfloat-equal -fno-sanitize-recover -D_GLIBCXX_DEBUG
DBG := gdb
LDFLAGS := -v -lc

BUILD_DIRECTORY := build

EXECUTABLE := program
EXEC_PATH := $(BUILD_DIRECTORY)/$(EXECUTABLE)

SRCS := $(wildcard *.cpp)
HDRS := $(wildcard *.h)
OBJS := $(patsubst %.cpp, $(BUILD_DIRECTORY)/%.o, $(SRCS))

.PHONY: all clean help run check debug

all: $(EXEC_PATH)

check:
	@echo "$(INFO)make check$(RESET)"
	@which $(CXX) > /dev/null && echo "$(SUCCESS)SUCCESS:$(RESET) $(CXX) is installed" || echo "$(ERROR)ERROR:$(RESET) $(CXX) not found, please install $(CXX)"
	@which $(DBG) > /dev/null && echo "$(SUCCESS)SUCCESS:$(RESET) $(DBG) is installed" || echo "$(ERROR)ERROR:$(RESET) $(DBG) not found, please install $(DBG)"

$(EXEC_PATH): $(OBJS)
	@echo "$(INFO)Linking$(RESET) $@ ..."
	@mkdir -p $(@D)
	@$(CXX) $(CXXFLAGS) $^ -o $@ $(LDFLAGS) && \
		echo "$(SUCCESS)SUCCESS$(RESET) Built $@" || \
		(echo "$(ERROR)ERROR$(RESET) Failed to link $@" && exit 1)

$(BUILD_DIRECTORY)/%.o: %.cpp
	@echo "$(INFO)Compiling$(RESET) $< ..."
	@mkdir -p $(@D)
	@$(CXX) $(CXXFLAGS) -c $< -o $@ && \
		echo "$(SUCCESS)SUCCESS:$(RESET) Compiled $<" || \
		(echo "$(ERROR)ERROR$(RESET) Failed to compile $<" && exit 1)

debug: $(EXEC_PATH)
	@echo "$(INFO)make debug$(RESET)"
	@echo "$(DBG) ./$(EXEC_PATH)"
	@$(DBG) ./$(EXEC_PATH)

clean:
	@echo "$(INFO)make clean$(RESET)"
	@echo "$(RM) -r $(EXEC_PATH) $(OBJS) $(BUILD_DIRECTORY) *~ *.bak *.dSYM *.out .*.un~"
	@$(RM) -r $(EXEC_PATH) $(OBJS) $(BUILD_DIRECTORY) *~ *.bak *.dSYM *.out .*.un~

run: $(EXEC_PATH)
	@echo "$(INFO)make run$(RESET)"
	@make clean
	@make all
	@./$(EXEC_PATH)
	@make clean

help:
	@echo "$(INFO)make help$(RESET)"
	@echo "Makefile for Building $(INFO)$(EXECUTABLE)$(RESET)."
	@echo "Usage:"
	@echo "  $(MAGENTA)make$(RESET)             — build $(INFO)$(EXECUTABLE)$(RESET)"
	@echo "  $(MAGENTA)make all$(RESET)         — build $(INFO)$(EXECUTABLE)$(RESET)"
	@echo "  $(MAGENTA)make check$(RESET)       — dependency check for $(INFO)$(CXX)$(RESET) and $(INFO)$(DBG)$(RESET)"
	@echo "  $(MAGENTA)make clean$(RESET)       — remove $(INFO)$(BUILD_DIRECTORY)$(RESET) files"
	@echo "  $(MAGENTA)make debug$(RESET)       — run $(INFO)$(EXECUTABLE)$(RESET) with $(INFO)$(DBG)$(RESET)"
	@echo "  $(MAGENTA)make run$(RESET)         — run $(INFO)$(EXECUTABLE)$(RESET)"
