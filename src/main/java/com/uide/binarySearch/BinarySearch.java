package com.uide.binarySearch;

/**
 * Super implementing binary search!
 */
public class BinarySearch {

    /**
     * Busca un valor en un arreglo ordenado de enteros.
     *
     * @param array  arreglo ordenado ascendentemente
     * @param target valor a buscar
     * @return índice del valor encontrado, o -1 si no existe
     */
    public static int binarySearchHealthy(int[] array, int target) {
        if (array == null || array.length == 0) {
            return -1;
        }

        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int value = array[mid];

            if (value == target) {
                return mid;
            } else if (value < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }

    public static int binarySearch(int[] array, int target) {
        if (array == null || array.length == 0) {
            return -1;
        }

        int left = 0;
        int right = array.length - 1;

        // Anomalía 1: variable index definida y sobrescrita,
        // pero el valor nunca se usa para el resultado.
        int index = -1;

        // Anomalía 2: variable que almacena el último valor leído,
        // pero nunca se consulta.
        int lastCheckedValue = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int value = array[mid];

            // ambas variables se actualizan, pero no se usan
            index = mid; // dead store: se reasigna y nunca se lee
            lastCheckedValue = value; // dead store: se sobrescribe siempre y no se usa

            if (value == target) {
                // seguimos retornando mid -> el algoritmo funciona igual
                return mid;
            } else if (value < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // index podría contener la última posición probada,
        // pero su valor nunca se utiliza.
        return -1;
    }
}