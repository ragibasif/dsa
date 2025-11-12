CXX:=g++
CXXFLAGS:=-std=c++17 -Wall -Wextra
SRC:=main.cpp

EXECUTABLE:=exe

all:
	$(CXX) -o $(EXECUTABLE) $(SRC) $(CXXFLAGS)

clean:
	$(RM) $(EXECUTABLE)

run:
	make clean
	make all
	./$(EXECUTABLE)
	make clean

.PHONY: all clean run

