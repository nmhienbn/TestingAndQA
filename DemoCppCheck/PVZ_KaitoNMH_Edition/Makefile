# USE make -j to compile faster
# USE make -j4 or make -j8 to compile faster in limited threads
# USE make run to run the program
# USE make clean to clean the object files


SHELL := pwsh.exe

TARGET = pvz

SDL2_path = .

CC = g++
CFLAGS = -std=c++17 -Wall -pedantic -MMD -MP 

OUTDIR = .
DATADIR = ./data
SUBDIR = semihost stream arg_parser
ICONDIR = ./resources/icon/main.res
DIR_OBJ = ./obj
DIR_SRC = ./obj


rwildcard=$(foreach d,$(wildcard $(1:=/*)),$(call rwildcard,$d,$2) $(filter $(subst *,%,$2),$d))

INCS = 
SRC = $(call rwildcard,src,*.cpp)
#NODIR_SRC = $(notdir $(SRC))
OBJS = $(addprefix $(DIR_OBJ)/, $(SRC:cpp=o)) # obj/xxx.o obj/folder/xxx .o
INC_DIRS = -Isrc -I$(SDL2_path)\include\SDL2 -I$(SDL2_path)\include -I.\src

LIBS = 
LIB_DIRS = 
#* SDL flags
LIB_DIRS += -L$(SDL2_path)\lib
LIBS     += -lmingw32 -lSDL2main -lSDL2 -lSDL2_image -lSDL2_ttf -lSDL2_mixer -mwindows


.PHONY: all 
all: compile run

.PHONY: compile
compile: $(TARGET) 


.PHONY: $(TARGET)
$(TARGET): $(OBJS)
	$(CC) -o $(OUTDIR)/$@ $(OBJS) $(ICONDIR) $(LIB_DIRS) $(LIBS)

DEPS=$(OBJS:.o=.d)
-include $(DEPS)

$(DIR_OBJ)/%.o: %.cpp 
	powershell mkdir -Force $(subst /,\,$(@D))
	$(CC) -o $@ $(CFLAGS) -c $< $(INC_DIRS)
	@echo "$(patsubst %.o,%.d,$@)"



.PHONY: clean
clean:
	powershell rm -r -Force $(subst /,\,$(DIR_OBJ))\src

.PHONY: echo
echo:
	@echo "INC files: $(INCS)"
	@echo "SRC files: $(SRC)"
	@echo "OBJ files: $(OBJS)"
	@echo "LIB files: $(LIBS)"
	@echo "INC DIR: $(INC_DIRS)"
	@echo "LIB DIR: $(LIB_DIRS)"
	@echo "DEP files: $(DEPS)"

.PHONY: run
run: 
	$(OUTDIR)/$(TARGET)

.PHONY: cppcheck
cppcheck:
	cppcheck --enable=all --inconclusive -j32 --std=c++17 --language=c++ --force $(INC_DIRS) src 2> cppcheck-report.txt
	@echo "📄 Report saved to cppcheck-report.txt"