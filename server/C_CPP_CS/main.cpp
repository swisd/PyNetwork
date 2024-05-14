#include <iostream>
#include <string>
using namespace std;

/* Program to handle requests */

void handler(string client_ip, string command, int pid = 21500) {
    // Handle request
    const string server_ip = "127.0.0.1";
    const int server_port = 8000;
    cout << "$handler\t";
    cout << server_ip;
    cout << ":";
    cout << server_ip;
}


int main() {
    handler("127.0.0.1", "s", 21502);
    return 0;
}