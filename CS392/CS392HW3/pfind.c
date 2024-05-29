// Author: Ethan Kalika
// Date: March 2, 2024
// Pledge: I pledge my honor that I have abided by the Stevens Honor System

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>

int validEntry(char str[])
{
    size_t strlength = strlen(str);
    if (strlength != 9)
    {
        fprintf(stderr, "Error: Permissions string '%s' is invalid.\n", str);
        exit(1);
    }
    for (int i = 0; i < 3; i++)
    {
        if (str[3 * i] != '-' && str[3 * i] != 'r')
        {
            fprintf(stderr, "Error: Permissions string '%s' is invalid.\n", str);
            exit(1);
        }
        if (str[3 * i + 1] != '-' && str[3 * i + 1] != 'w')
        {
            fprintf(stderr, "Error: Permissions string '%s' is invalid.\n", str);
            exit(1);
        }
        if (str[3 * i + 2] != '-' && str[3 * i + 2] != 'x')
        {
            fprintf(stderr, "Error: Permissions string '%s' is invalid.\n", str);
            exit(1);
        }
    }
    return 0;
}

void getDirs(char pathArg[], char perms[])
{
    struct stat fileStat;
    struct dirent* currFile;
    DIR* dir = opendir(pathArg);
    int counter = 0;
    while ((currFile = readdir(dir)) != NULL)
    {
        char currPath[4096];
        strcpy(currPath, pathArg);
        strcat(currPath, currFile -> d_name);
        stat(currPath, &fileStat);
        if ((((fileStat.st_mode & S_IRUSR) ? 'r' : '-') == perms[0]) && (((fileStat.st_mode & S_IWUSR) ? 'w' : '-') == perms[1]) &&
        (((fileStat.st_mode & S_IXUSR) ? 'x' : '-') == perms[2]) && (((fileStat.st_mode & S_IRGRP) ? 'r' : '-') == perms[3]) &&
        (((fileStat.st_mode & S_IWGRP) ? 'w' : '-') == perms[4]) && (((fileStat.st_mode & S_IXGRP) ? 'x' : '-') == perms[5]) &&
        (((fileStat.st_mode & S_IROTH) ? 'r' : '-') == perms[6]) && (((fileStat.st_mode & S_IWOTH) ? 'w' : '-') == perms[7]) &&
        (((fileStat.st_mode & S_IXOTH) ? 'x' : '-') == perms[8]) && (S_ISREG(fileStat.st_mode)))
        {
            fprintf(stdout, "%s\n", currPath);
            fflush(stdout);
        }
        if (S_ISDIR(fileStat.st_mode) && strcmp(currFile -> d_name, ".") != 0 && strcmp(currFile -> d_name, "..") != 0)
        {
            strcat(currPath, "/");
            getDirs(currPath, perms);
        }
        counter++;
    }
    closedir(dir);
}

int main(int argc, char* argv[])
{
    validEntry(argv[2]);
    getDirs(argv[1], argv[2]);
    return 0;
}