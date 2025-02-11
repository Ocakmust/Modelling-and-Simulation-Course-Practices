#include <iostream> // Giriş ve çıkış işlemleri için
#include <string>   // String veri türü için
#include <cstdlib>  // rand ve srand için gerekli kütüphane
#include <ctime>    // time() fonksiyonu için gerekli kütüphane

using namespace std;

int main() {

    //1
    int test_size;
    int n_dollars;
    int m_dollars;
    int b_dollars;
    int desired_dollars;
    //2
    string user_color;
    string roulette_color;
    int user_choice; 
    int roulette_num;
    int count=0;
    srand(time(0));

	cout << "n_dollars:";
    cin >> n_dollars;

    cout << "m_dollars:";
    cin >> m_dollars;

    cout << "b_dollars:";
    cin >> b_dollars;

    cout << "test_size:";
    cin >> test_size;


    desired_dollars=m_dollars+n_dollars;
    cout << "desired_dollars: "<<desired_dollars<< endl;

    int n_temp=n_dollars;

    for (int i = 0; i < test_size; i++) {
        n_dollars=n_temp;

        while (true){
	        user_choice = rand() % 2;
	        if (user_choice==0){
	            user_color="black";
	        } else{
	            user_color="red";
	        }
	
	        roulette_num = rand() % 38 + 1;
	        if (roulette_num<=18){
	            roulette_color="black";
	        } else if(roulette_num>=18 & roulette_num<=36){
	            roulette_color="red";
	        } else {
	            roulette_color="green";
	        }
	
	        if (roulette_color == user_color){
	            n_dollars = n_dollars + b_dollars;
	        } else {
	            n_dollars = n_dollars - b_dollars;
	        }


	        if (n_dollars==desired_dollars) {
	            count=count+1;
	            break;
	        } else if(n_dollars==0){
	            break;
	        }

        }
    }
	float rate=float(count)/test_size;
    cout << "counter:" << count <<"   Rate:"<<rate <<endl;
	
	

    return 0; // Program başarıyla sonlandı
}
