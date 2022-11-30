#include <iostream>

using namespace std;

class Product {
public:
    string name;
    float price;
    float discount;

    float finalPrice() {
        return price * (1 - discount);
    }

};


int main () {
    Product p1;
    p1.name = "Notebook";
    p1.price = 1600.45;
    p1.discount = 0.15;

    cout << "O produto analisado eh: " << p1.name << endl;
    cout << "O preco do produto antes era R$ " << p1.price << endl;
    cout << "O desconto a ser aplicado eh de: " << p1.discount << endl;
    cout << "O preco do produto apos a aplicacao do desconto eh R$ " << p1.finalPrice() << endl;

    return 0;
}
