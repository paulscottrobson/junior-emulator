ifeq ($(OS),Windows_NT)
include ..\documents\common.make
else
include ../documents/common.make
endif

APPNAME = jr256$(APPSTEM)

SOURCES = 	src$(S)sys_processor.o  framework$(S)main.o framework$(S)gfx.o framework$(S)debugger.o \
			src$(S)sys_debug_uk101.o src$(S)hardware.o
  
CC = g++

.PHONY: all clean emulator prebuild release run

all: emulator

run: emulator 
	.$(S)$(APPNAME) basic.rom@8000

monitor:
	make -BC ..$(S)newmon
	touch src$(S)sys_processor.cpp 

emulator: prebuild $(APPNAME)
	$(CCOPY) $(APPNAME) ..$(S)..$(S)bin
	
%.o:%.cpp
	$(CC) $(CXXFLAGS) -D INCLUDE_DEBUGGING_SUPPORT -I cpu -I framework -I include -c -o $@ $<

clean:
	$(CDEL) $(APPNAME) 
	$(CDEL) src$(S)*.o 
	$(CDEL) framework$(S)*.o

$(APPNAME): $(SOURCES)
	$(CC) $(SOURCES) $(LDFLAGS) $(SDL_LDFLAGS) -o $@
	