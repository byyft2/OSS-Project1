#include <stdio.h>
main() {
	system("chmod 640 /etc/sudoers");
	system("vi /etc/sudoers");
	system("chmod 440 /etc/sudoers");
}