package com.uide.binarySearch;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BinarySearchTest {

    // ==============================
    // 1) Tests para binarySearch (con anomalías)
    // ==============================

    @Test
    @DisplayName("A1 - Elemento existente en el medio (binarySearch)")
    void searchExistingMiddle_binarySearch() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearch(data, 5);
        assertEquals(2, index);
    }

    @Test
    @DisplayName("A2 - Elemento inexistente entre valores (binarySearch)")
    void searchNonExistingBetweenValues_binarySearch() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearch(data, 4);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("A3 - Arreglo nulo devuelve -1 (binarySearch)")
    void nullArrayReturnsMinusOne_binarySearch() {
        int index = BinarySearch.binarySearch(null, 10);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("A4 - Arreglo vacío devuelve -1 (binarySearch)")
    void emptyArrayReturnsMinusOne_binarySearch() {
        int[] data = {};
        int index = BinarySearch.binarySearch(data, 10);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("B1 - Encuentra el primer elemento (binarySearch)")
    void searchFirstElement_binarySearch() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearch(data, 1);
        assertEquals(0, index);
    }

    @Test
    @DisplayName("B2 - Encuentra el último elemento (binarySearch)")
    void searchLastElement_binarySearch() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearch(data, 9);
        assertEquals(4, index);
    }

    @Test
    @DisplayName("B3 - Elemento menor que el mínimo (binarySearch)")
    void targetSmallerThanAll_binarySearch() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearch(data, -5);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("B4 - Elemento mayor que el máximo (binarySearch)")
    void targetGreaterThanAll_binarySearch() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearch(data, 15);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("B5 - Arreglo de un solo elemento - encontrado (binarySearch)")
    void singleElementFound_binarySearch() {
        int[] data = { 42 };
        int index = BinarySearch.binarySearch(data, 42);
        assertEquals(0, index);
    }

    @Test
    @DisplayName("B6 - Arreglo de un solo elemento - no encontrado (binarySearch)")
    void singleElementNotFound_binarySearch() {
        int[] data = { 42 };
        int index = BinarySearch.binarySearch(data, 7);
        assertEquals(-1, index);
    }

    // ==============================
    // 2) Tests para binarySearchHealthy (versión “sana”)
    // -> mismos casos, para cubrir también este método
    // ==============================

    @Test
    @DisplayName("H1 - Elemento existente en el medio (binarySearchHealthy)")
    void searchExistingMiddle_binarySearchHealthy() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearchHealthy(data, 5);
        assertEquals(2, index);
    }

    @Test
    @DisplayName("H2 - Elemento inexistente entre valores (binarySearchHealthy)")
    void searchNonExistingBetweenValues_binarySearchHealthy() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearchHealthy(data, 4);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("H3 - Arreglo nulo devuelve -1 (binarySearchHealthy)")
    void nullArrayReturnsMinusOne_binarySearchHealthy() {
        int index = BinarySearch.binarySearchHealthy(null, 10);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("H4 - Arreglo vacío devuelve -1 (binarySearchHealthy)")
    void emptyArrayReturnsMinusOne_binarySearchHealthy() {
        int[] data = {};
        int index = BinarySearch.binarySearchHealthy(data, 10);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("H5 - Encuentra el primer elemento (binarySearchHealthy)")
    void searchFirstElement_binarySearchHealthy() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearchHealthy(data, 1);
        assertEquals(0, index);
    }

    @Test
    @DisplayName("H6 - Encuentra el último elemento (binarySearchHealthy)")
    void searchLastElement_binarySearchHealthy() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearchHealthy(data, 9);
        assertEquals(4, index);
    }

    @Test
    @DisplayName("H7 - Elemento menor que el mínimo (binarySearchHealthy)")
    void targetSmallerThanAll_binarySearchHealthy() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearchHealthy(data, -5);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("H8 - Elemento mayor que el máximo (binarySearchHealthy)")
    void targetGreaterThanAll_binarySearchHealthy() {
        int[] data = { 1, 3, 5, 7, 9 };
        int index = BinarySearch.binarySearchHealthy(data, 15);
        assertEquals(-1, index);
    }

    @Test
    @DisplayName("H9 - Arreglo de un solo elemento - encontrado (binarySearchHealthy)")
    void singleElementFound_binarySearchHealthy() {
        int[] data = { 42 };
        int index = BinarySearch.binarySearchHealthy(data, 42);
        assertEquals(0, index);
    }

    @Test
    @DisplayName("H10 - Arreglo de un solo elemento - no encontrado (binarySearchHealthy)")
    void singleElementNotFound_binarySearchHealthy() {
        int[] data = { 42 };
        int index = BinarySearch.binarySearchHealthy(data, 7);
        assertEquals(-1, index);
    }
}