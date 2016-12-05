#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <functional>

using namespace std;
void solve(istream&);

int main() {
    ifstream input_file;
    input_file.open(".\\input0.txt", ios::out);
    if (input_file.is_open())
    {
        solve(input_file);
    }
    else {
        cout << "Error?" << endl;
    }

    return 0;
}

void solve(istream& input) {

    map<string, map<string, int>> aunts;

    for (int i = 0; i < 500; i++) {

        map<string, int> mp;

        string line;
        getline(input, line);

        string word;
        string number;
        string aunt_number;
        stringstream ss(line);

        getline(ss, aunt_number, ':');
        getline(ss, word, ' ');

        while (!ss.eof()) {
            getline(ss, word, ' ');
            getline(ss, number, ' ');
            if (number.find(',') != -1) {
                number = number.substr(0, number.size() - 1);
            }
            int value = stoi(number);
            mp[word.substr(0, word.size() - 1)] = value;
        }

        aunts[aunt_number] = mp;
    }

    map<string, pair<int, function<bool(int, int)>>> reference;
    reference["children"] = make_pair<int, function<bool(int, int)>>(3, equal_to<int>());
    reference["cats"] = make_pair<int, function<bool(int, int)>>(7, greater<int>());
    reference["samoyeds"] = make_pair<int, function<bool(int, int)>>(2, equal_to<int>());
    reference["pomeranians"] = make_pair<int, function<bool(int, int)>>(3, less<int>());
    reference["akitas"] = make_pair<int, function<bool(int, int)>>(0, equal_to<int>());
    reference["vizslas"] = make_pair<int, function<bool(int, int)>>(0, equal_to<int>());
    reference["goldfish"] = make_pair<int, function<bool(int, int)>>(5, less<int>());
    reference["trees"] = make_pair<int, function<bool(int, int)>>(3, greater<int>());
    reference["cars"] = make_pair<int, function<bool(int, int)>>(2, equal_to<int>());
    reference["perfumes"] = make_pair<int, function<bool(int, int)>>(1, equal_to<int>());

    for (map<string, pair<int, function<bool(int, int)>>>::iterator current_attribute = reference.begin(); current_attribute != reference.end(); current_attribute++) {
        map<string, map<string, int>>::iterator current_aunt = aunts.begin();
        while(current_aunt != aunts.end()){
            if (current_aunt->second.find(current_attribute->first) != current_aunt->second.end()) {

                int expected_value = (current_attribute->second).first;
                int actual_value = current_aunt->second[current_attribute->first];
                function<bool(int, int)> compare_operator = (current_attribute->second).second;

                if (!compare_operator(actual_value, expected_value)) {
                    current_aunt = aunts.erase(current_aunt);
                    continue;
                }
            }
            current_aunt++;
        }
    }


    for (map<string, map<string, int>>::iterator iter = aunts.begin(); iter != aunts.end(); iter++) {
        
        cout << iter->first << endl;
    }
}