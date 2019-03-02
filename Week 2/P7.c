#include<stdio.h>
#include<unistd.h>
#include<bits/types.h>

void main(){
    pid_t pid = fork();
    if(pid > 0){
        pid_t pid2 = fork();
        if(pid2 > 0){
            pid_t pid3 = fork();
            if(pid3 == 0){
                pid_t pid4 = fork();
                if(pid4 == 0){
                    pid_t pid5 = fork();
                    if(pid5 > 0){
                        pid_t pid6 = fork();
                    }
                }
            }
        }
        else if(pid == 0) {
            pid_t pid7 = fork();
            if(pid7 > 0){
                pid_t pid8 = fork();
            }
        }
        
    }
}                               