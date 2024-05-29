// Author: Ethan Kalika
// Date: Thursday March 28, 2024
// Pledge: I pledge my honor that I have abided by the Stevnes Honor System

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>
#include <pwd.h>
#include <errno.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <signal.h>
#include <limits.h>

#define BLUE "\x1b[34;1m"
#define DEFAULT "\x1b[0m"

char cont = 1;
char* currWorkingDir;
int activeChild = -1;
volatile sig_atomic_t interrupted = -1;

int containsSpaces(char* givenStr)
{
    while(*givenStr)
    {
        if (isspace(*givenStr))
        {
            return 1;
        }
        givenStr++;
    }
    return 0;
}

int compare(const void* a, const void* b)
{
    return *(int*)a - *(int*)b;
}

int getNumSubDir(char* givenDir)
{
    DIR* dir = opendir(givenDir);
    struct dirent* currFiles;
    char* currFile;
    int num = 0;
    while((currFiles = readdir(dir)) != NULL)
    {
        char currFile[PATH_MAX];
        strcpy(currFile, currFiles -> d_name);
        if (atoi(currFile))
        {
            num++;
        }
    }
    closedir(dir);
    return num;
}

int numlen(int num)
{
    int counter = 0;
    while (num > 0)
    {
        num /= 10;
        counter++;
    }
    return counter;
}

void handler(int sig)
{
    printf("\n");
    interrupted = 0;
    if (activeChild != -1)
    {
        kill(activeChild, SIGINT);
    }
}

void cdCommand(const char* path)
{
    if (strlen(path) == 0 || strcmp(path, "~") == 0)
    {
        pid_t uid = getuid();
        struct passwd* pw = getpwuid(uid);
        if (pw == NULL)
        {
            fprintf(stderr, "Error: Cannot get passwd entry. %s.\n", strerror(errno));
        }
        if (chdir(pw->pw_dir) != 0)
        {
            fprintf(stderr, "Error: Cannot change directory to %s. %s.\n", path, strerror(errno));
        }
    }
    else if (*path == '~')
    {
        pid_t uid = getuid();
        struct passwd* pw = getpwuid(uid);
        if (pw == NULL)
        {
            fprintf(stderr, "Error: Cannot get passwd entry. %s.\n", strerror(errno));
        }
        if (chdir(pw->pw_dir) != 0)
        {
            fprintf(stderr, "Error: Cannot change directory to %s. %s.\n", path, strerror(errno));
        }
        if (chdir(path + 1) != 0)
        {
            if (chdir(currWorkingDir) != 0)
            {
                fprintf(stderr, "Error: Cannot change directory to %s. %s.\n", path, strerror(errno));
            }
            fprintf(stderr, "Error: Cannot change directory to %s. %s.\n", path, strerror(errno));
        }
    }
    else if (chdir(path) != 0)
    {
        fprintf(stderr, "Error: Cannot change directory to %s. %s.\n", path, strerror(errno));
    }
}

void exitProgram()
{
    cont = 0;
    exit(EXIT_SUCCESS);
}

void printWorkingDir()
{
    char* temp;
    temp = getcwd(NULL, 0);
    if (temp == NULL)
    {
        fprintf(stderr, "Error: Cannot get current working directory. %s.\n", strerror(errno));
    }
    else
    {
        printf("%s\n", temp);
    }
    free(temp);
    temp = NULL;
}

void lfCommand()
{
    DIR* dir = opendir(currWorkingDir);
    struct dirent* currFiles;
    char* currFile;
    while((currFiles = readdir(dir)) != NULL)
    {
        if ((currFile = malloc(strlen(currFiles -> d_name) + 1)) == NULL)
        {
            fprintf(stderr, "Error: malloc() failed. %s.\n", strerror(errno));
        }
        strcpy(currFile, currFiles -> d_name);
        if (strcmp(currFile, "..") != 0 && strcmp(currFile, ".") != 0)
        {
            printf("%s\n", currFiles -> d_name);
        }
        free(currFile);
        currFile = NULL;
    }
    closedir(dir);
}

void lpCommand()
{
    int num = getNumSubDir("/proc");
    DIR* dir = opendir("/proc");
    struct dirent* currFiles;
    char* currFile;
    int pArr[num];
    int counter = 0;
    while((currFiles = readdir(dir)) != NULL)
    {
        char currFile[PATH_MAX];
        strcpy(currFile, currFiles -> d_name);
        if (atoi(currFile))
        {
            int temp = atoi(currFile);
            pArr[counter] = temp;
            counter++;
        }
    }
    closedir(dir);
    qsort(pArr, num, sizeof(int), compare);
    int maxlen = numlen(pArr[num - 1]);
    int numSpace;
    for (int i = 0; i < num; i++)
    {
        // Gets the PID's
        char currFile[PATH_MAX];
        numSpace = maxlen - numlen(pArr[i]);
        char firstPart[MAX_INPUT];
        strcpy(firstPart, " ");
        for (int j = 0; j < numSpace; j++)
        {
            strcat(firstPart, " ");
        }
        sprintf(currFile, "%d", pArr[i]);
        strcat(firstPart, currFile);

        // Gets the owner of the file
        char procPath[PATH_MAX];
        strcpy(procPath, "/proc/");
        strcat(procPath, currFile);
        struct stat info;
        stat(procPath, &info);
        struct passwd* pw = getpwuid(info.st_uid);
        if (pw == NULL)
        {
            fprintf(stderr, "Error: Cannot get passwd entry. %s.\n", strerror(errno));
        }

        // Gets the calling command
        FILE* commandFile;
        size_t bufferSize = 0;
        char* commName = NULL;
        char commPath[PATH_MAX];
        strcpy(commPath, procPath);
        strcat(commPath, "/cmdline");
        commandFile = fopen(commPath, "r");

        // Prints, closes files, and clears memory
        printf("%s %s ", firstPart + 1, pw -> pw_name);
        if (getline(&commName, &bufferSize, commandFile) != -1)
        {
            printf("%s", commName);
        }
        printf("\n");
        free(commName);
        commName = NULL;
        fclose(commandFile);
    }
}

void other(char* commName)
{
    pid_t pid = fork();
    if (pid < 0)
    {
        fprintf(stderr, "Error: fork() failed. %s.\n", strerror(errno));
    }
    else if (pid == 0)
    {
        char** tempTokenList = NULL;
        int count = 0;
        char* newToken = strtok(commName, " ");
        while (newToken != NULL)
        {
            tempTokenList = realloc(tempTokenList, (count + 1) * sizeof(char *));
            tempTokenList[count++] = newToken;
            newToken = strtok(NULL, " ");
        }
        tempTokenList = realloc(tempTokenList, (count + 1) * sizeof(char *));
        tempTokenList[count] = NULL;
        if(interrupted = -1 && execvp(tempTokenList[0], tempTokenList) == -1)
        {
            fprintf(stderr, "Error: exec() failed. %s.\n", strerror(errno));
            exit(EXIT_FAILURE);
        }
        for (int i = 0; i < count; i++)
        {
            free(tempTokenList[i]);
            tempTokenList[i] = NULL;
        }
        free(tempTokenList);
        tempTokenList = NULL;
    }
    else
    {
        if (interrupted == -1)
        {
            activeChild = pid;
            if(wait(NULL) < 0 && interrupted == -1)
            {
                fprintf(stderr, "Error: wait() failed. %s.\n", strerror(errno));
            }
        }
    }
}

int main()
{
    struct sigaction action = {0};
    action.sa_handler = handler;
    if(sigaction(SIGINT, &action, NULL) == -1)
    {
        fprintf(stderr, "Error: Cannot register signal handler. %s.\n", strerror(errno));
    }
    char comm[MAX_INPUT];
    while(cont)
    {
        currWorkingDir = getcwd(NULL, 0);
        if (interrupted == -1 && currWorkingDir == NULL)
        {
            fprintf(stderr, "Error: Cannot get current working directory. %s.\n", strerror(errno));
            exit(EXIT_FAILURE);
        }
        printf("%s[%s]%s> ", BLUE, currWorkingDir, DEFAULT);
        if (fgets(comm, sizeof(comm), stdin) == NULL && interrupted == -1)
        {
            fprintf(stderr, "Error: Failed to read from stdin. %s.\n", strerror(errno));
        }
        comm[strcspn(comm, "\n")] = '\0';
        if (interrupted == -1 && strcmp(comm, "pwd") == 0)
        {
            printWorkingDir();
        }
        else if (interrupted == -1 && strcmp(comm, "exit") == 0)
        {
            exitProgram();
        }
        else if (interrupted == -1 && strncmp(comm, "cd", 2) == 0)
        {
            char* path = comm + 2;
            if (*path != ' ' && *path != '\0')
            {
                fprintf(stderr, "Error: Command not found.\n");
                free(currWorkingDir);
                currWorkingDir = NULL;
                interrupted = -1;
                activeChild = -1;
                continue;
            }
            while(*path == ' ')
            {
                path++;
            }
            char* comm_ = path;
            size_t len = strlen(comm_);
            while(len > 0 && comm_[len - 1] == ' ' || comm_[len - 1] == '\n')
            {
                comm_[len - 1] = '\0';
                len--;
            }
            if (containsSpaces(comm_))
            {
                fprintf(stderr, "Error: Too many arguments to cd.\n");
            }
            else
            {
                cdCommand(comm_);
            }
        }
        else if (interrupted == -1 && strcmp(comm, "lf") == 0)
        {
            lfCommand();
        }
        else if (interrupted == -1 && strcmp(comm, "lp") == 0)
        {
            lpCommand();
        }
        else if (interrupted == -1)
        {
            other(comm);
        }
        activeChild = -1;
        interrupted = -1;
        free(currWorkingDir);
        currWorkingDir = NULL;
    }
    return 0;
}
/*
valgrind --leak-check=yes ./a.out
*/