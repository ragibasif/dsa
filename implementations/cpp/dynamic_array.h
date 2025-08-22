/*
 * File: dynamic_array.h
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 */

#ifndef DYNAMIC_ARRAY_H
#define DYNAMIC_ARRAY_H

#include <algorithm>
#include <iostream>
#include <optional>
#include <stdexcept>

namespace custom {

constexpr size_t DA_DEFAULT_SIZE     = 0;
constexpr size_t DA_DEFAULT_CAPACITY = 0;
constexpr size_t DA_GROWTH_FACTOR    = 2;

template <typename T>
class dynamic_array {
  private:
    T     *buffer_;
    size_t size_;
    size_t capacity_;

    void bounds_check( int index ) {
        if ( index < 0 || index >= size_ ) {
            throw std::out_of_range( "Index is out of range." );
        }
    }

  public:
    dynamic_array()
        : size_{ DA_DEFAULT_SIZE }, capacity_{ DA_DEFAULT_CAPACITY } {
        buffer_ = new T[capacity_];
    }

    dynamic_array( int size ) {
        if ( size <= 0 ) { return dynamic_array(); }
        size_     = size;
        capacity_ = size_ * DA_GROWTH_FACTOR;
        buffer_   = new T[capacity_]{};
    }

    dynamic_array( int size, T item ) {
        if ( size <= 0 ) { return dynamic_array(); }
        size_     = size;
        capacity_ = size_ * DA_GROWTH_FACTOR;
        buffer_   = new T[capacity_]{};
        for ( size_t i = 0; i < size_; i++ ) { buffer_[i] = item; }
    }

    ~dynamic_array() {
        delete[] buffer_;
        buffer_   = nullptr;
        size_     = 0;
        capacity_ = 0;
    }

    void print() {
        for ( size_t i = 0; i < size_; i++ ) { std::cout << buffer_[i] << " "; }
        std::cout << "\n";
    }

    std::optional<size_t> find( const T item ) {
        for ( size_t i = 0; i < size_; i++ ) {
            if ( buffer_[i] == item ) { return i; }
        }
        return std::nullopt; // not found
    }

    const T at( int index ) {
        bounds_check( index );
        return buffer_[index];
    }

    const T &front() { return &buffer_[0]; }

    const T &back() { return &buffer_[size_ - 1]; }

    const T *data() { return *buffer_; }

    const bool empty() { return size_ > 0; }

    const size_t size() { return size_; }

    const size_t capacity() { return capacity_; }

    void clear() { size_ = 0; }

    // Time: O(1) amortized
    void push_back( const T item ) {
        if ( size_ == capacity_ ) { resize(); }
        buffer_[size_++] = item;
    }

    // Time: O(1)
    void pop_back() {
        if ( size_ == 0 ) { return; }
        size_--;
    }

    void resize() {
        if ( capacity_ == 0 ) { capacity_++; }
        capacity_ *= DA_GROWTH_FACTOR;
        T *temp_buffer = new T[capacity_];
        for ( size_t i = 0; i < size_; i++ ) { temp_buffer[i] = buffer_[i]; }
        std::swap( buffer_, temp_buffer );
        delete[] temp_buffer;
        temp_buffer = nullptr;
    }

    // Time: O(N)
    void push_front( const T item ) {
        push_back( item );
        for ( size_t i = size_ - 1; i > 0; i-- ) {
            buffer_[i] = buffer_[i - 1];
        }
        buffer_[0] = item;
    }

    // Time: O(N)
    void pop_front() {
        for ( size_t i = 0; i < size_ - 1; i++ ) {
            buffer_[i] = buffer_[i + 1];
        }
        size_--;
    }
};

} // namespace custom

#endif // DYNAMIC_ARRAY_H
