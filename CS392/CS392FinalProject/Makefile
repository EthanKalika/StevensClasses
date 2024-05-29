# Author: Ethan Kalika
# Pledge: I pledge my honor that I have abided by the Stevens Honor System

CC = gcc

CFLAGS = -Wall

SERVER_SRCS = server.c
SERVER_OBJS = $(SERVER_SRCS:.c=.o)
SERVER_EXEC = server

CLIENT_SRCS = client.c
CLIENT_OBJS = $(CLIENT_SRCS:.c=.o)
CLIENT_EXEC = client

all: $(SERVER_EXEC) $(CLIENT_EXEC) clean

$(SERVER_EXEC): $(SERVER_OBJS)
	$(CC) $(CFLAGS) $(SERVER_OBJS) -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

$(CLIENT_EXEC): $(CLIENT_OBJS)
	$(CC) $(CFLAGS) $(CLIENT_OBJS) -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm *.o