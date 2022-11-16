#include <iostream>


using namespace std;


class Product {        
    public:          
        string name;  // Atributo
        float price;  // Atributo
        float discount;      // Atributo
        Product(string x, float y, float z) { // Construtor com parametros
            name = x;
            price = y;
            discount = z;
        };
        void finalPrice() {
            float nprice = (price)-(discount * price);
            cout << "Preco com desconto: " << nprice << endl;
        };
};


int main() {
    // Criando um objeto
    Product p1("Notebook", 1600.45, 0.15);
    // Imprimindo valores
    cout <<  "Nome do produto: " << p1.name << endl;
    cout << "Preco sem desconto: " << p1.price << endl;
    cout << "Desconto: " << p1.discount << endl;
    p1.finalPrice();
    
    return 0;
};
