all: wrong.out right.out
wrong.out: def.o wrong.o
	gcc -o wrong.out def.o wrong.o
right.out: def.o right.o
	gcc -o right.out def.o right.o
def.o: def.c
right.o: right.c
wrong.o: wrong.c
clean:
	rm *.o *.out
