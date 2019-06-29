cmake_minimum_required(VERSION 3.0)
project(Block)

add_library(dynlib SHARED source/block.c headers/block.h)
add_executable(dynamic_block program.c)
target_link_libraries(dynamic_block dynlib)

add_library(stalib STATIC source/block.c headers/block.h)
add_executable(static_block program.c)
target_link_libraries(static_block stalib)
