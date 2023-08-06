#include <stdio.h>
#include <string.h>
#include <sys/capability.h>
#include <sys/resource.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define CHILD "./pcap_session"
#define CHILD_RESTART_TIME 10 // Sleep for a few seconds, then restart child

int main(int argc, char *argv[])
{
    char *child_argv[] = {CHILD, "lo", NULL};
    char *child_env[] = {NULL};
    char is_parent = 1;
    pid_t pid; // Child PID
    int status;
    cap_t caps;
    cap_value_t cap_list[1];

    if (argc >= 2)
    {
        child_argv[1] = argv[1];
    }

    caps = cap_get_proc();
    if (NULL == caps)
    {
        printf("Couldn't find capabilities!\n");
        return(2);
    }
    cap_list[0] = CAP_NET_RAW;
    if (cap_set_flag(caps, CAP_INHERITABLE, 1, cap_list, CAP_SET) == -1)
    {
        printf("Couldn't set capability flags!\n");
        return(2);
    }
    if (cap_set_proc(caps) == -1)
    {
        printf("Couldn't set capabilities for process!\n");
        return(2);
    }
    if (cap_free(caps))
    {
        printf("Couldn't free memory for capability structure!\n");
        return(2);
    }

    while (is_parent)
    {
        pid = fork();
        if (0 == pid)
        {
            struct rlimit lim = {10000000, 10000000};
            is_parent = 0; // Safety measure, execve shouldn't be returning
            setrlimit(RLIMIT_AS, &lim); // Limit virtual memory
            execve(CHILD, child_argv, child_env);
        }
        else
        {
            waitpid(pid, &status, 0);
            printf("Child terminated, WIFEXITED: %s. WIFSIGNALED: %s\n",
                   WIFEXITED(status) ? "true":"false",
                   WIFSIGNALED(status) ? "true":"false");
            if (WIFSIGNALED(status))
            {
                printf("Termination signal: %s\n",
                       strsignal(WTERMSIG(status)));
            }
            printf("Going to sleep...\n");
            sleep(CHILD_RESTART_TIME);
            printf("Woke up, will restart child!\n");
        }
    }

    return(0);
}
