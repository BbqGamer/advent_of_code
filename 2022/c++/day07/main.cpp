#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<climits>
#include<memory>
#include <algorithm>

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
    std::vector<Node*> children;

public:
    Node(std::string name, Node* parent, NodeType ntype)
    : name(name), parent(parent), ntype(ntype), size(0) {}

    std::string get_name() {return this->name;}
    int get_size() {return this->size;}
    NodeType get_type() {return this->ntype;}

    Node* get_parent() { return this->parent;}
    Node* get_child(std::string name) {
        for(auto child: children) {
            if(!child->get_name().compare(name)) {
                return child;
            }
        }
        return nullptr;
    }

    void add_child(Node* child) { this->children.push_back(child);}
    void set_size(int size) { this->size = size;}

    struct Iterator {
        std::vector<Node*>::iterator it;
        Iterator(std::vector<Node*>::iterator it) : it(it) {}
        Iterator operator++() { ++it; return *this; }
        Node* operator*() { return *it; }
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

void freeTree(Node* root) {
    if(root == nullptr) { return; }
    for(Node* child : *root) {
        freeTree(child);
    }
    delete root;
}

int main() {
    std::string input;

    Node* root = new Node("/", nullptr, Directory);
    Node* current = root;

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
            Node* new_dir = new Node(input, current, Directory);
            current->add_child(new_dir);
        } else {
            int size = std::stoi(input);
            std::cin >> input;
            Node* new_file = new Node(input, current, File);
            new_file->set_size(size);
            current->add_child(new_file);
        }
    }
    

    calculateSize(root);
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

    freeTree(root);
}   