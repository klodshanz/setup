C Program to dump text in colors on terminal:

```c
#include <stdio.h>

#define KNRM  "\x1B[0m"
#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define KYEL  "\x1B[33m"
#define KBLU  "\x1B[34m"
#define KMAG  "\x1B[35m"
#define KCYN  "\x1B[36m"
#define KWHT  "\x1B[37m"
#define CR "\n"
#define EM ""

void line(int lines) {
	printf(CR);
	for (int index=0; index<lines; index++) {
    	printf("%s##################################################################\n",KGRN);
    }
	printf(CR);
}

int main()
{
    line(2);
	FILE *fp;
	char path[1035];
	fp = popen("pwd", "r");
	if (fp!=NULL) {
		while (fgets(path, sizeof(path)-1, fp) != NULL) {
			printf("  %s%s", KWHT,path);
		}
	}
	pclose(fp);
	line(2);

    return 0;
}
```
