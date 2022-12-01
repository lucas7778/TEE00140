/* Projeto 3
Alunos: Claudio Coelho da Silva Junior (120.038.029) e Elias da Silva Dutra (220.038.092)
Linguagens de Programação para Engenharia Elétrica
TEE00140 */

#include <iostream>
using namespace std;

class Product {
    public:
        string name;
        float price;
        float discount;
    
    float finalPrice() {
        return price - (price*(discount));
    }
    
};
    
int main() {
    Product p1;
    p1.name = "Notebook";
    p1.price = 1600.45;
    p1.discount = 0.15;

    cout << p1.name << endl;
    cout << p1.price << endl;
    cout << p1.discount << endl;
    cout << p1.finalPrice() << endl;
    
    return 0;
}
