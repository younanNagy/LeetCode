// 155. Min Stack
#include <list>
class MinStack {
// int min_;
list <int>stack;
list <int> min_stack;
public:
    
    MinStack() {
        // min_=INT_MAX;
    // list <int>stack;
    }
    
    void psuhMin(int new_val)
    {
        if(min_stack.empty())
            min_stack.push_front(new_val);
        else if(new_val<min_stack.front())
            min_stack.push_front(new_val);
        else
            min_stack.push_front(min_stack.front());
    }
    void push(int val) {
        psuhMin(val);
        stack.push_front(val);
    }
    
    void pop() {
        min_stack.pop_front();
        stack.pop_front();
    }
    
    int top() {
        return stack.front();
    }
    
    int getMin() {
        return min_stack.front();
    }
};
