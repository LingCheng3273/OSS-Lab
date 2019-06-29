blockmake: source/block.c
	gcc -c source/block.c -o source/block.o
	ar qc source/libblock.a source/block.o
	gcc -fPIC -c source/block.c -o source/block.o
	gcc -shared -o source/libblock.so source/block.o
	gcc -c program.c -o program.o
	gcc program.o source/libblock.a -o static_block
	gcc program.o source/libblock.so -o dynamic_block -Wl,-rpath='$$ORIGIN'
