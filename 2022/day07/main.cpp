#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<climits>
#include<memory>
#include<algorithm>

enum NodeType {
    Directory,
    File,
};

class Node {
private:
    std::string name;
    int size;
    NodeType ntype;

    Node* parent;
    std::vector<std::unique_ptr<Node>> children;

public:
    Node(std::string name, Node* parent, NodeType ntype)
    : name(name), parent(parent), ntype(ntype), size(0) {}

    std::string get_name() {return this->name;}
    int get_size() {return this->size;}
    NodeType get_type() {return this->ntype;}

    Node* get_parent() { return this->parent;}
    Node* get_child(std::string name) {
        for(int i = 0; i < children.size(); i++) {
            if(!children[i]->get_name().compare(name)) {
                return children[i].get();
            }
        }
        return nullptr; //Child not found
    }

    void add_child(std::string name, NodeType ntype, int size) { 
        children.push_back(std::make_unique<Node>(name, this, ntype));
        children.back()->size = size;
    }
    void set_size(int size) { this->size = size;}

    struct Iterator {
        std::vector<std::unique_ptr<Node>>::iterator it;
        Iterator(std::vector<std::unique_ptr<Node>>::iterator it) : it(it) {}
        Iterator operator++() { ++it; return *this; }
        Node* operator*() { return (*it).get(); }
        bool operator!=(const Iterator& other) { return it != other.it; }
    };

    Iterator begin() { return Iterator(children.begin());}
    Iterator end() { return Iterator(children.end());}
};

std::map<std::string, int> sizes;
int sizes_below_100000 = 0;

void calculateSize(Node* root) {
    if(root == nullptr) { return; }
    for(auto child : *root) {
        calculateSize(child);
        root->set_size(root->get_size() + child->get_size());
    }

    //TASKS
    int size = root->get_size();
    if(root->get_type() == Directory) {
        if(size < 100000) {
            sizes_below_100000 += root->get_size();
        }
        sizes[root->get_name()] = size;
    }
}


int main() {
    std::string input;

    std::unique_ptr<Node> root = std::make_unique<Node>("/", nullptr, Directory);
    Node* current = root.get();

    std::cin >> input >> input >> input; //Throw away first line
    while(1) {
        std::cin >> input;
        if(!input.compare("x")) { break; }
        if(!input.compare("$")) {
            std::cin >> input;
            if(!input.compare("ls")) { continue; }
            std::cin >> input;
            if(!input.compare("..")) {
                current = current->get_parent();
            } else {
                current = current->get_child(input);
            }
        } else if (!input.compare("dir")) {
            std::cin >> input;
            current->add_child(input, Directory, 0);
        } else {
            int size = std::stoi(input);
            std::cin >> input;
            current->add_child(input, File, size);
        }
    }
    

    calculateSize(root.get());
    std::cout << "Part 1: " << sizes_below_100000 << std::endl;

    int min_size = INT_MAX;
    for (auto s : sizes) {
        int free_size = 70000000 - sizes["/"] + s.second;
        if(free_size >= 30000000) {
            if(s.second < min_size) {
                min_size = s.second;
            }
        }
    }
    std::cout << "Part 2: " << min_size << std::endl;
}   