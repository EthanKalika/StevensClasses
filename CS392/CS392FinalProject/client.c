// Author: Ethan Kalika
// Pledge: I pledge my honor that I have abided by the Stevens Honor System

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int BUFFER_SIZE = 1024;

void parse_connect(int argc, char** argv, int* server_fd)
{
    char* ip_address = "127.0.0.1";
    int port_number = 25555;
    int opt;
    while ((opt = getopt(argc, argv, ":i:p:h")) != -1)
    {
        switch (opt)
        {
            case 'i':
                ip_address = optarg;
                break;
            case 'p':
                port_number = atoi(optarg);
                break;
            case 'h':
                printf("Usage: %s [-i IP_address] [-p port_number] [-h]\n", argv[0]);
                printf("\n");
                printf("  -i IP_address\t\tDefault to \"127.0.0.1\";\n");
                printf("  -p port_number\tDefault to 25555;\n");
                printf("  -h\t\t\tDisplay this help info.\n");
                exit(0);
            default:
                fprintf(stderr, "Error: Unknown option '-%c' received.\n", optopt);
                exit(1);
        }
    }
    struct sockaddr_in server_address;
    memset(&server_address, 0, sizeof(server_address));
    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = inet_addr(ip_address);
    server_address.sin_port = htons(port_number);
    *server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (*server_fd < 0)
    {
        perror("Error creating socket");
        exit(EXIT_FAILURE);
    }
    if (connect(*server_fd, (struct sockaddr*)&server_address, sizeof(server_address)) < 0)
    {
        perror("Error connecting to server");
        exit(EXIT_FAILURE);
    }
}

int main(int argc, char* argv[]) {
    int server_fd;
    parse_connect(argc, argv, &server_fd);
    char buffer[BUFFER_SIZE];
    if (read(server_fd, buffer, BUFFER_SIZE) == 0)
    {
        exit(0);
    }
    printf("%s", buffer);
    char name[128];
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0';
    write(server_fd, name, strlen(name));
    fd_set read_fds;
    int max_fd;
    while (1)
    {
        FD_ZERO(&read_fds);
        FD_SET(server_fd, &read_fds);
        FD_SET(STDIN_FILENO, &read_fds);
        max_fd = (server_fd > STDIN_FILENO) ? server_fd : STDIN_FILENO;
        select(max_fd + 1, &read_fds, NULL, NULL, NULL);
        if (FD_ISSET(server_fd, &read_fds))
        {
            memset(buffer, 0, sizeof(buffer));
            if (read(server_fd, buffer, BUFFER_SIZE) == 0)
            {
                break;
            }
            buffer[strlen(buffer)] = '\n';
            printf("%s", buffer);
        }
        if (FD_ISSET(STDIN_FILENO, &read_fds))
        {
            char choice;
            scanf(" %c", &choice);
            write(server_fd, &choice, 1);
        }
    }
    close(server_fd);
    return 0;
}