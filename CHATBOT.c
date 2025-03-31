#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
typedef struct clist {
    char user_message[200] ;
    struct clist *next ;
}node;
node *front = NULL ;
node *rear = NULL ;
void inserrt1 () {
    char ch = 'y' ;
    if (front == NULL && rear == NULL) {
        front = (node *)malloc(sizeof(node)) ;
        printf ("Enter Message : ") ;
        gets(front->user_message) ;
        front->next = front ;
        rear = front ;
    }
}
void inserrt2 () {
    node *ptr , *new_message ;
    new_message = (node *)malloc(sizeof(node)) ;
    printf ("Enter message : ") ;
    gets(new_message->user_message) ;
    new_message->next = front ;
    rear->next = new_message ;
    rear = new_message ;
}


void reemove () {
    node *temp ;
    FILE *file = fopen("User_Messages.csv", "a");
    if (rear==NULL) {
        printf ("No message entered") ;
    }
    else {
        temp = front ;
        front = front->next ;
        puts(temp->user_message) ;
        fprintf(file, "%s\n", temp->user_message);
        fflush(file);
        free(temp) ;
    }
}
int main() {
    char ch = 'y', ch1 = 'y';
    inserrt1() ;
    reemove ();
    printf ("Continue Messaging : ") ;
    ch1 = getche() ;
    if(ch1=='y'){
    while (ch =='y'){
        inserrt2() ;
        reemove();
        printf ("Continue Messaging : ") ;
        ch = getche() ;
    }
}
return 0 ;
}

