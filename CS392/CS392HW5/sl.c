// Author: Ethan Kalika
// Date: April 8, 2024
// Pledge: I pledge my honor that I have abided by the Stevens Honor System

#include <stdio.h>
#include <dirent.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <limits.h>
#include <errno.h>
#include <string.h>

#define WRITE_END 1
#define READ_END 0

int main(int argc, char* argv[])
{
    // Checking input validity
    if (argc != 2)
    {
        fprintf(stderr, "Needs exaclty one argument.\n");
        exit(1);
    }
    struct stat filestat;
    if (stat(argv[1], &filestat) == -1)
    {
        fprintf(stderr, "Permission denied. %s cannot be read.", argv[1]);
        exit(1);
    }
    if (!S_ISDIR(filestat.st_mode))
    {
        fprintf(stderr, "The first argument has to be a directory.");
        exit(1);
    }
    if (!(filestat.st_mode & S_IRUSR) || !(filestat.st_mode & S_IRGRP) || !(filestat.st_mode & S_IROTH))
    {
        fprintf(stderr, "Permission denied. %s cannot be read.", argv[1]);
        exit(1);
    }

    // Creation of pipe
    int pipeai[2];
    int pipesort[2];
    if (pipe(pipeai) == -1)
    {
        fprintf(stderr, "Error: pipe failed. %s", strerror(errno));
        exit(EXIT_FAILURE);
    }
    if (pipe(pipesort) == -1)
    {
        fprintf(stderr, "Error: pipe failed. %s", strerror(errno));
        exit(EXIT_FAILURE);
    }
    pid_t ai = fork();
    if (ai < 0)
    {
        fprintf(stderr, "Error: fork failed");
        exit(EXIT_FAILURE);
    }
    else if (ai == 0)
    {
        if (close(pipeai[READ_END]) == -1)
        {
            fprintf(stderr, "Error: close failed. %s", strerror(errno));
            exit(EXIT_FAILURE);
        }
        if (dup2(pipeai[WRITE_END], 1) == -1)
        {
            fprintf(stderr, "Error: dup2 failed. %s", strerror(errno));
            exit(EXIT_FAILURE);
        }
        if (close(pipeai[WRITE_END]) == -1)
        {
            fprintf(stderr, "Error: close failed. %s", strerror(errno));
            exit(EXIT_FAILURE);
        }
        if (close(pipesort[READ_END]) == -1)
        {
            fprintf(stderr, "Error: close failed. %s", strerror(errno));
            exit(EXIT_FAILURE);
        }
        if ((execlp("ls", "ls", "-ai", argv[1], NULL)) == -1)
        {
            fprintf(stderr, "Error: ls failed.");
            exit(EXIT_FAILURE);
        }
    }
    else
    {
        if (wait(NULL) == -1)
        {
            fprintf(stderr, "Error: wait failed. %s", strerror(errno));
            exit(EXIT_FAILURE);
        }
        pid_t childSort = fork();
        if (childSort < 0)
        {
            fprintf(stderr, "Error: fork failed");
            exit(EXIT_FAILURE);
        }
        else if (childSort == 0)
        {
            char sortData[PIPE_BUF] = {0};
            if (close(pipeai[WRITE_END]) == -1)
            {
                fprintf(stderr, "Error: close failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if (dup2(pipeai[READ_END], 0) == -1)
            {
                fprintf(stderr, "Error: dup2 failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if (close(pipeai[READ_END]) == -1)
            {
                fprintf(stderr, "Error: close failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if (close(pipesort[READ_END]) == -1)
            {
                fprintf(stderr, "Error: close failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if (dup2(pipesort[WRITE_END], 1) == -1)
            {
                fprintf(stderr, "Error: dup2 failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if (close(pipesort[WRITE_END]) == -1)
            {
                fprintf(stderr, "Error: close failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if ((execlp("sort", "sort", NULL) == -1))
            {
                fprintf(stderr, "Error: sort failed.");
                exit(EXIT_FAILURE);
            }
        }
        else
        {
            char parData[PIPE_BUF] = {0};
            char* countPointer = parData;
            int numFile = 0;
            if (close(pipeai[WRITE_END]) == -1)
            {
                fprintf(stderr, "Error: close failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if (close(pipeai[READ_END]) == -1)
            {
                fprintf(stderr, "Error: close failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if (close(pipesort[WRITE_END]) == -1)
            {
                fprintf(stderr, "Error: close failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if (wait(NULL) == -1)
            {
                fprintf(stderr, "Error: wait failed. %s", strerror(errno));
                exit(EXIT_FAILURE);
            }
            int curr;
            while((curr = read(pipesort[READ_END], &parData, PIPE_BUF)) != 0)
            {
                if (curr == -1)
                {
                    fprintf(stderr, "Error: read failed. %s", strerror(errno));
                    exit(EXIT_FAILURE);
                }
                write(1, &parData, curr);
                for(int i = 0; i < curr; i++)
                {
                    if (parData[i] == '\n')
                    {
                        numFile++;
                    }
                }
            }
            printf("Total files: %d\n", numFile);
        }
    }
    return 0;
}