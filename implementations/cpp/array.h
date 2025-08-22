/*
 * File: array.h
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 */

#ifndef ARRAY_H
#define ARRAY_H

#include <iostream>
#include <optional>
#include <stdexcept>

namespace custom {

template <typename T>
class array {
  private:
    T     *buffer_;
    size_t size_;

    void bounds( int index ) {
        if ( index < 0 || index >= size_ ) {
            throw std::out_of_range( "Index is out of range." );
        }
    }

  public:
    array( int size = 0 ) {
        if ( size < 0 ) {
            throw std::invalid_argument( "Size must be 0 or greater." );
        }
        size_   = size;
        buffer_ = new T[size_]{};
    }

    array( int size, T item ) {
        if ( size < 0 ) {
            throw std::invalid_argument( "Size must be 0 or greater." );
        }
        size_   = size;
        buffer_ = new T[size_]{};
        if ( item ) {
            for ( size_t i = 0; i < size_; i++ ) { buffer_[i] = item; }
        }
    }

    ~array() {
        delete[] buffer_;
        buffer_ = nullptr;
        size_   = 0;
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
        bounds( index );
        return buffer_[index];
    }

    T &operator[]( int index ) {
        bounds( index );
        return buffer_[index];
    }

    array<T> &operator=( array<T> &old ) {
        if ( buffer_ != nullptr ) { delete[] buffer_; }
        buffer_     = old.buffer_;
        old.buffer_ = nullptr;
        size_       = old.size_;
        return *this;
    }

    const T &front() { return &buffer_[0]; }

    const T &back() { return &buffer_[size_ - 1]; }

    const T *data() { return *buffer_; }

    const bool empty() { return size_ > 0; }

    const size_t size() { return size_; }
};

} // namespace custom

#endif // ARRAY_H
