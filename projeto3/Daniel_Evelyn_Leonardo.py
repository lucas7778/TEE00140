class Product {
    public:
    string name;
    double price;
    double discount;
    double finalprice;
};

int main() {
    Product p1;
    p1.name = "Notebook";
    p1.price = 1600.45;
    p1.discount = 0.15;
    p1.finalprice = (1600.45 - (1600.45*0.15));

    cout << "O nome do produto é " << p1.name << endl;
    cout << "O preço sem o desconto é de R$ " << p1.price << endl;
    cout << "O desconto é de " << p1.discount << endl;
    cout << "O preço final é de R$ " << p1.finalprice << endl;

    return 0;
}
