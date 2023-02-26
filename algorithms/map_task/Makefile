CC = g++
CFLAGS = --std=c++17 -Wall -pedantic
SOURCE1 = main.cpp
SOURCE2 = main.py
OUT1 = main.exe

ifeq ($(OS), Windows_NT)
	RM = del
else
	RM = rm
endif

all:
	$(CC) $(CFLAGS) -o $(OUT1) $(SOURCE1)
	
clean:
	$(RM) $(OUT1) $(OUT2)

run: all
	.\$(OUT1) | python $(SOURCE2)