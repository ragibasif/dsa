CXX=clang++
CXXFLAGS=-std=c++17 -Wall -Wextra

EXECUTABLE=exe

all:
	$(CXX) -o $(EXECUTABLE) main.cpp $(CXXFLAGS)

clean:
	$(RM) $(EXECUTABLE)

run:
	make clean
	make all
	./$(EXECUTABLE)
	make clean

.PHONY: all clean run

