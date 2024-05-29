// Author: Ethan Kalika
// Pledge: I pledge my honor that I have abided by the Stevens Honor System

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define MAX_PLAYERS 3
#define MAX_QUESTIONS 50
#define BUFFER_SIZE 1024

int lostConnection = 0;

struct Entry {
    char prompt[1024];
    char options[3][50];
    int answer_idx;
};

struct Player {
    int fd;
    int score;
    char name[128];
};

void underScoretoSpace(char entry[], int size)
{
    for (int i = 0; i < size; i++)
    {
        if(entry[i] == '_')
        {
            entry[i] = ' ';
        }
    }
}

int read_questions(struct Entry* arr, char* filename)
{
    FILE* file = fopen(filename, "r");
    if (!file)
    {
        perror("Error opening file");
        return -1;
    }
    char buffer[BUFFER_SIZE];
    int count = 0;
    char word1[BUFFER_SIZE];
    char word2[BUFFER_SIZE];
    char word3[BUFFER_SIZE];
    while (fgets(buffer, BUFFER_SIZE, file))
    {
        strcpy(arr[count].prompt, buffer);
        fgets(buffer, BUFFER_SIZE, file);
        sscanf(buffer, "%s %s %s", word1, word2, word3);
        underScoretoSpace(word1, BUFFER_SIZE);
        underScoretoSpace(word2, BUFFER_SIZE);
        underScoretoSpace(word3, BUFFER_SIZE);
        strcpy(arr[count].options[0], word1);
        strcpy(arr[count].options[1], word2);
        strcpy(arr[count].options[2], word3);
        fgets(buffer, BUFFER_SIZE, file);
        arr[count].answer_idx = (buffer[0] == arr[count].options[0][0]) ? 0 : (buffer[0] == arr[count].options[1][0]) ? 1 : 2;
        fgets(buffer, BUFFER_SIZE, file);
        memset(word1, 0, sizeof(word1));
        memset(word2, 0, sizeof(word2));
        memset(word3, 0, sizeof(word3));
        count++;
    }
    fclose(file);
    return count;
}

int get_max_fd(fd_set* set) {
    int max_fd = -1;
    for (int fd = 0; fd < FD_SETSIZE; ++fd) {
        if (FD_ISSET(fd, set) && fd > max_fd) {
            max_fd = fd;
        }
    }
    return max_fd;
}

int main(int argc, char *argv[]) {
    char *question_file = "questions.txt";
    char *ip_address = "127.0.0.1";
    int port_number = 25555;
    int opt;
    while ((opt = getopt(argc, argv, "f:i:p:h")) != -1)
    {
        switch (opt)
        {
            case 'f':
                question_file = optarg;
                break;
            case 'i':
                ip_address = optarg;
                break;
            case 'p':
                port_number = atoi(optarg);
                break;
            case 'h':
                printf("Usage: %s [-f question_file] [-i IP_address] [-p port_number] [-h]\n\n", argv[0]);
                printf("  -f question_file\tDefault to \"question.txt\";\n");
                printf("  -i IP_address\t\tDefault to \"127.0.0.1\";\n");
                printf("  -p port_number\tDefault to 25555;\n");
                printf("  -h\t\t\tDisplay this help info.\n");
                return 0;
            default:
                printf("Error: Unknown option '-%c' received.\n", optopt);
                return 1;
        }
    }
    int server_fd, new_socket;
    struct sockaddr_in address;
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("Error creating socket");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = inet_addr(ip_address);
    address.sin_port = htons(port_number);
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0)
    {
        perror("Error binding socket");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, MAX_PLAYERS) < 0)
    {
        perror("Error listening");
        exit(EXIT_FAILURE);
    }
    printf("Welcome to 392 Trivia!\n");
    struct Entry questions[MAX_QUESTIONS];
    int num_questions = read_questions(questions, question_file);
    if (num_questions < 0)
    {
        perror("Error could not read questions");
        exit(EXIT_FAILURE);
    }
    struct Player players[MAX_PLAYERS];
    int num_players = 0;
    fd_set mySet;
    FD_ZERO(&mySet);
    FD_SET(server_fd, &mySet);
    int nameCounter = 0;
    while (1)
    {
        fd_set readySet = mySet;
        int max_fd = get_max_fd(&readySet);
        select(max_fd + 1, &readySet, NULL, NULL, NULL);
        if (FD_ISSET(server_fd, &readySet))
        {
            int addrlen = sizeof(address);
            if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0)
            {
                perror("Error accepting connection");
                exit(EXIT_FAILURE);
            }
            if (num_players == MAX_PLAYERS)
            {
                printf("Max connection reached!\n");
                close(new_socket);
            }
            else
            {
                printf("New connection detected!\n");
                players[num_players].fd = new_socket;
                FD_SET(new_socket, &mySet);
                char message[] = "Please type your name: ";
                write(new_socket, message, strlen(message));
                num_players++;
            }
        }
        for (int i = 0; i < num_players; i++)
        {
            if (FD_ISSET(players[i].fd, &readySet) && players[i].name[0] == '\0')
            {
                read(players[i].fd, players[i].name, sizeof(players[i].name));
                printf("Hi %s!\n", players[i].name);
                nameCounter++;
            }
        }
        if (nameCounter == MAX_PLAYERS)
        {
            break;
        }
    }
    printf("The game starts now!\n");
    for (int i = 0; i < num_questions; i++)
    {
        printf("Question %d: %s\n1: %s\n2: %s\n3: %s\n", i + 1, questions[i].prompt, questions[i].options[0], questions[i].options[1], questions[i].options[2]);
        char message[BUFFER_SIZE];
        char ansmessage[BUFFER_SIZE];
        sprintf(message, "Question %d: %s\nPress 1: %s\nPress 2: %s\nPress 3: %s\n", i + 1, questions[i].prompt, questions[i].options[0], questions[i].options[1], questions[i].options[2]);
        for (int j = 0; j < num_players; j++)
        {
            write(players[j].fd, message, strlen(message));
        }
        fd_set readySet;
        FD_ZERO(&readySet);
        for (int j = 0; j < num_players; j++)
        {
            FD_SET(players[j].fd, &readySet);
        }
        int max_fd = get_max_fd(&readySet);
        select(max_fd + 1, &readySet, NULL, NULL, NULL);
        int player_idx = -1;
        char choice;
        for (int j = 0; j < num_players; j++)
        {
            if (FD_ISSET(players[j].fd, &readySet))
            {
                if (read(players[j].fd, &choice, 1) == 0)
                {
                    printf("\nLost connection!\n");
                    lostConnection = 1;
                }
                else
                {
                    player_idx = j;
                    break;
                }
            }
        }
        if (player_idx == -1)
        {
            break;
        }
        int answer = choice - '1';
        if (answer == questions[i].answer_idx)
        {
            players[player_idx].score++;
            printf("\n%s answered correctly!\nScore: ", players[player_idx].name);
        }
        else
        {
            if (players[player_idx].score > 0)
            {
                players[player_idx].score--;
            }
            printf("\n%s answered incorrectly!\nScore: ", players[player_idx].name);
        }
        for (int j = 0; j < num_players; j++)
        {
            printf("%s: %d\t", players[j].name, players[j].score);
        }
        sprintf(ansmessage, "\nThe correct answer is: %s\n==================================================\n", questions[i].options[questions[i].answer_idx]);
        printf("%s\n\n", ansmessage);
        for (int j = 0; j < num_players; j++)
        {
            write(players[j].fd, ansmessage, strlen(ansmessage));
        }
    }
    if (lostConnection == 0)
    {
        int max_score = 0;
        int winner_idx = 0;
        for (int i = 0; i < num_players; i++)
        {
            if (players[i].score > max_score)
            {
                max_score = players[i].score;
                winner_idx = i;
            }
        }
        printf("Congrats, %s!\n", players[winner_idx].name);
    }
    for (int i = 0; i < num_players; i++)
    {
        close(players[i].fd);
    }
    close(server_fd);
    return 0;
}