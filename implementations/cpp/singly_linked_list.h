/*
 * File: singly_linked_list.h
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 */

#ifndef SINGLY_LINKED_LIST_H
#define SINGLY_LINKED_LIST_H

#include <algorithm>
#include <iostream>
#include <optional>
#include <stdexcept>

namespace custom {

template <typename T>
class singly_linked_list {
  private:
    struct node {
        T     data_;
        node *next_;

        node( T data ) : data_{ data }, next_{ nullptr } {}
    };
    node *head;

  public:
    singly_linked_list() : head{ nullptr } {}

    ~singly_linked_list() {
        node *prev = nullptr;
        node *curr = head;
        while ( curr != nullptr ) {
            prev = curr;
            curr = curr->next_;
            delete prev;
        }
        prev = curr = nullptr;
    }

    void prepend( const T data ) {
        node *new_node = new node( data );
        if ( !head ) {
            head = new_node;
            return;
        }
        new_node->next_ = head;
        head            = new_node;
    }

    void append( const T data ) {
        node *new_node = new node( data );
        if ( !head ) {
            head = new_node;
            return;
        }
        node *prev = nullptr;
        node *curr = head;
        while ( curr != nullptr ) {
            prev = curr;
            curr = curr->next_;
        }
        prev->next_ = new_node;
    }

    T get_nth( const size_t n ) {
        T      result = NULL;
        size_t k      = 0;
        node  *curr   = head;
        while ( curr ) {
            if ( k == n ) {
                result = curr->data_;
                return result;
            }
            k++;
            curr = curr->next_;
        }
        return result;
    }

    const T &front() const { return head->data; }

    bool empty() const noexcept { return head != nullptr; }

    void print() {
        node *curr = head;
        while ( curr != nullptr ) {
            std::cout << curr->data_ << " ";
            curr = curr->next_;
        }
        std::cout << "\n";
    }
};

} // namespace custom

#endif // SINGLY_LINKED_LIST_H
