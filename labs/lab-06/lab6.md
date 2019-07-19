# Lab 6

## Example 0
![example0](example0.png)

## Example 1
### Running Ubuntu container
![example1.1](example1-1.png)
![example1.2](example1-2.png)
### Installing Vim
![example1.3](example1-3.png)
![example1.4](example1-4.png)
### Installing Cowsay
![example1.5](example1-5.png)

## Example 2
For example 2 I followed the instructions as written, including going 
back to a preivous version of rocket.chat, but I coun't get rocket.chat
to work. On the right, you can see 
that all the commands match the ones given and the container is 
running under "docker ps". However, on the left I have localhost:3000
open and it wouldn't connect. I have tried removing the containers 
and trying again many times, but it still didn't work.
![example2.1](example2-1.png)

## Example 3
For example 3 I couldn't get hello world to run on localhost:5000.
I followed the instructions in writing Dockerfile and ran the
docker commands, but nothing showed up in locahost:5000. 
In the image you can see the the commands are running, but 
localhost:5000 wouldn't connect.
### Dockerfile
![example3.1](example3-1.png)
### docker build
![example3.2](example3-2.png)
### docker run
![example3.3](example3-3.png)

## Example 4
### Dockerfile
![example4.1](example4-1.png)
### docker-compose.yml
![example4.2](example4-2.png)

When I tried to build docker-compose I kept getting an error on strp 6
when it's supposed to install and fix the node dependencies. 
Therefore, I wasn't able to proceed with the lab. I tried skipping this
step and moving on, but the next steps all depended on the app to run. 
When I ran the next commands, I got a message saying that docker failed to
connect to localhost:1337. This makes sense because docker-compose was supposed 
to connect to localhost:1337. 
![example4.3](example4-3.png)
![example4.4](example4-4.png)
![example4.5](example4-5.png)
![example4.6](example4-6.png)

