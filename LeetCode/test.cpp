#include<iostream>
using namespace std;

char *position(char *str,char c){
	while(*str!='\0'){
		if(*str==c){
			return str;
			str++;
		}
	}
   return NULL;
} 

int main() {
	char *str = "abcdefghijk";
    cout<<str;
	char *p;
	p=position(str,'j');
    cout<<"ma";
	cout<<p;
	if(p==NULL){
		cout<<"the letter could not be found"<<endl;
	}
	else{
		cout<<"the position is:"<<p-str<<endl;
	}
	return 0;
}