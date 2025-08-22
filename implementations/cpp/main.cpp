/*
 * File: main.cpp
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 */

#include "array.h"
#include "dynamic_array.h"
#include "singly_linked_list.h"

#include <cassert>
#include <chrono>
#include <iostream>
#include <random>

static void test_array();
static void test_dynamic_array();
static void test_singly_linked_list();

int main() {

    auto start = std::chrono::high_resolution_clock::now();

    test_array();
    test_dynamic_array();
    test_singly_linked_list();

    std::random_device                                       rd;
    std::mt19937                                             mt( rd() );
    std::uniform_int_distribution<std::mt19937::result_type> dist( 1, 6 );

    for ( size_t i = 0; i < 10; i++ ) { std::cout << dist( mt ) << std::endl; }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::cout << "Finished in: " << duration.count() << std::endl;

    return EXIT_SUCCESS;
}

static void test_array() {
    custom::array<int> v;
    v.print();

    auto result = v.find( 5 );
    if ( result.has_value() ) {
        std::cout << "Found at index: " << *result << "\n";
    } else {
        std::cout << "Value not found.\n";
    }
    result = v.find( 55 );
    if ( result.has_value() ) {
        std::cout << "Found at index: " << *result << "\n";
    } else {
        std::cout << "Value not found.\n";
    }
}

void test_dynamic_array() {
    custom::dynamic_array<int> v;
    for ( int i = 0; i < 10; i++ ) { v.push_back( i ); }
    v.print();

    auto result = v.find( 5 );
    if ( result.has_value() ) {
        std::cout << "Found at index: " << *result << "\n";
    } else {
        std::cout << "Value not found.\n";
    }
    result = v.find( 55 );
    if ( result.has_value() ) {
        std::cout << "Found at index: " << *result << "\n";
    } else {
        std::cout << "Value not found.\n";
    }

    v.push_front( 99 );
    v.print();
    v.pop_front();
    v.print();
}

void test_singly_linked_list() {
    custom::singly_linked_list<int> sll;
    for ( size_t i = 0; i < 20; i++ ) { sll.prepend( i ); }
    sll.print();
    for ( size_t i = 0; i < 20; i++ ) { sll.append( i ); }
    sll.print();
    for ( size_t i = 0; i < 50; i++ ) {
        std::cout << "sll.get_nth( i+5 ): " << sll.get_nth( i + 5 ) << '\n';
    }
    sll.print();
}
