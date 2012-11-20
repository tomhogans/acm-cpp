#include <stdio.h>
#include <iostream>

class StandardDie {
  protected:
    int value[2];

  public:
  StandardDie(int top=5, int front=1, int right=3) {
    this->value[0] = top;
    this->value[1] = front;
    this->value[2] = right;
  }

  void info() {
    printf("StandardDie (%d, %d, %d)\n", this->value[0], this->value[1], 
        this->value[2]);
  }

  void tip(char direction) {
    switch (direction) {
      case 'f': // front
        std::swap(this->value[0], this->value[1]);
        this->value[0] = 7 - this->value[0];
        break;
      case 'b': // back
        std::swap(this->value[0], this->value[1]);
        this->value[1] = 7 - this->value[1];
        break;
      case 'l': // left
        std::swap(this->value[0], this->value[2]);
        this->value[2] = 7 - this->value[2];
        break;
      case 'r': // right
        std::swap(this->value[0], this->value[2]);
        this->value[0] = 7 - this->value[0];
        break;
    }
  }

  int face() {
    return this->value[1];
  }

  int opposite() {
    return (7 - this->face());
  }
};


int main() {
  StandardDie die;
  die.info();
  die.tip('r');
  die.info();
  return 0;
}
