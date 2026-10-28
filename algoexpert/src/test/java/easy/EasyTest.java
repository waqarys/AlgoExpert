package easy;

import common.*;
import easy.arrays.*;
import easy.binarysearchtrees.*;
import easy.binarytrees.*;
import easy.graphs.DepthFirstSearch;
import easy.greedyalgorithms.*;
import easy.linkedlists.*;
import easy.recursion.*;
import easy.searching.*;
import easy.sorting.*;
import easy.strings.*;
import org.junit.jupiter.api.Test;

import java.util.ArrayList; import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class EasyTest {
    @Test void twoNumberSum() {
        int[] r = TwoNumberSum.twoNumberSum(new int[]{3, 5, -4, 8, 11, 1, -1, 6}, 10);
        assertEquals(10, r[0] + r[1]);
        assertEquals(0, TwoNumberSum.twoNumberSum(new int[]{1, 2}, 10).length);
    }
    @Test void validateSubsequence() {
        assertTrue(ValidateSubsequence.isValidSubsequence(List.of(5, 1, 22, 25, 6, -1, 8, 10), List.of(1, 6, -1, 10)));
        assertFalse(ValidateSubsequence.isValidSubsequence(List.of(1, 2, 3), List.of(3, 2)));
    }
    @Test void sortedSquared() {
        assertArrayEquals(new int[]{1, 4, 9, 25}, SortedSquaredArray.sortedSquaredArray(new int[]{-3, -1, 2, 5}));
        assertArrayEquals(new int[]{0, 1, 4}, SortedSquaredArray.sortedSquaredArray(new int[]{-2, -1, 0}));
    }
    @Test void tournament() {
        var comps = List.of(List.of("HTML", "C#"), List.of("C#", "Python"), List.of("Python", "HTML"));
        assertEquals("Python", TournamentWinner.tournamentWinner(comps, List.of(0, 0, 1)));
        assertEquals("A", TournamentWinner.tournamentWinner(List.of(List.of("A", "B")), List.of(1)));
    }
    @Test void nonConstructible() {
        assertEquals(20, NonConstructibleChange.nonConstructibleChange(new int[]{5, 7, 1, 1, 2, 3, 22}));
        assertEquals(1, NonConstructibleChange.nonConstructibleChange(new int[]{}));
        assertEquals(1, NonConstructibleChange.nonConstructibleChange(new int[]{2}));
    }
    @Test void transpose() {
        assertArrayEquals(new int[][]{{1, 3}, {2, 4}}, TransposeMatrix.transposeMatrix(new int[][]{{1, 2}, {3, 4}}));
        assertArrayEquals(new int[][]{{1}, {2}}, TransposeMatrix.transposeMatrix(new int[][]{{1, 2}}));
    }
    @Test void closestBst() {
        BST t = BST.of(10, 5, 15, 2, 5, 13, 22, 1, 14);
        assertEquals(13, FindClosestValueInBst.findClosestValueInBst(t, 12));
        assertEquals(1, FindClosestValueInBst.findClosestValueInBst(t, -5));
    }
    @Test void branchSumsAndDepths() {
        BinaryTree t = BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        assertEquals(List.of(15, 16, 18, 10, 11), BranchSums.branchSums(t));
        assertEquals(16, NodeDepths.nodeDepths(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7, 8, 9)));
        assertEquals(0, NodeDepths.nodeDepths(new BinaryTree(1)));
    }
    @Test void expressionTree() {
        BinaryTree t = BinaryTree.fromLevelOrder(-1, -2, -3, -4, 2, 8, 3, 2, 3);
        assertEquals(6, EvaluateExpressionTree.evaluateExpressionTree(t));
        assertEquals(7, EvaluateExpressionTree.evaluateExpressionTree(new BinaryTree(7)));
    }
    @Test void dfs() {
        var a = new DepthFirstSearch.Node("A").addChild("B").addChild("C");
        a.children.get(0).addChild("D");
        assertEquals(List.of("A", "B", "D", "C"), a.depthFirstSearch(new ArrayList<>()));
    }
    @Test void greedy() {
        assertEquals(17, MinimumWaitingTime.minimumWaitingTime(new int[]{3, 2, 1, 2, 6}));
        assertEquals(0, MinimumWaitingTime.minimumWaitingTime(new int[]{5}));
        assertTrue(ClassPhotos.classPhotos(new ArrayList<>(List.of(5, 8, 1, 3, 4)), new ArrayList<>(List.of(6, 9, 2, 4, 5))));
        assertFalse(ClassPhotos.classPhotos(new ArrayList<>(List.of(5, 5)), new ArrayList<>(List.of(5, 6))));
        assertEquals(32, TandemBicycle.tandemBicycle(new int[]{5, 5, 3, 9, 2}, new int[]{3, 6, 7, 2, 1}, true));
        assertEquals(25, TandemBicycle.tandemBicycle(new int[]{5, 5, 3, 9, 2}, new int[]{3, 6, 7, 2, 1}, false));
    }
    @Test void linkedLists() {
        var h = RemoveDuplicatesFromLinkedList.removeDuplicatesFromLinkedList(LinkedListNode.of(1, 1, 3, 4, 4, 4, 5, 6, 6));
        assertEquals(List.of(1, 3, 4, 5, 6), LinkedListNode.toList(h));
        assertEquals(3, MiddleNode.middleNode(LinkedListNode.of(1, 2, 3, 4, 5)).value);
        assertEquals(3, MiddleNode.middleNode(LinkedListNode.of(1, 2, 3, 4)).value);
    }
    @Test void recursion() {
        assertEquals(0, NthFibonacci.getNthFib(1));
        assertEquals(1, NthFibonacci.getNthFib(2));
        assertEquals(5, NthFibonacci.getNthFib(6));
        List<Object> arr = List.of(5, 2, List.of(7, -1), 3, List.of(6, List.of(-13, 8), 4));
        assertEquals(12, ProductSum.productSum(arr));
    }
    @Test void searching() {
        assertEquals(3, BinarySearch.binarySearch(new int[]{0, 1, 21, 33, 45, 45, 61, 71, 72, 73}, 33));
        assertEquals(-1, BinarySearch.binarySearch(new int[]{1, 5}, 3));
        assertArrayEquals(new int[]{18, 141, 541}, FindThreeLargestNumbers.findThreeLargestNumbers(new int[]{141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7}));
    }
    @Test void sorting() {
        int[] want = {2, 3, 5, 5, 6, 8, 9};
        assertArrayEquals(want, BubbleSort.bubbleSort(new int[]{8, 5, 2, 9, 5, 6, 3}));
        assertArrayEquals(want, InsertionSort.insertionSort(new int[]{8, 5, 2, 9, 5, 6, 3}));
        assertArrayEquals(want, SelectionSort.selectionSort(new int[]{8, 5, 2, 9, 5, 6, 3}));
        assertArrayEquals(new int[]{}, BubbleSort.bubbleSort(new int[]{}));
    }
    @Test void strings() {
        assertTrue(PalindromeCheck.isPalindrome("abcdcba"));
        assertFalse(PalindromeCheck.isPalindrome("ab"));
        assertEquals("zab", CaesarCipherEncryptor.caesarCypherEncryptor("xyz", 2));
        assertEquals("abc", CaesarCipherEncryptor.caesarCypherEncryptor("abc", 52));
        assertEquals("9A4A2B4C2D", RunLengthEncoding.runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"));
        assertEquals("1a", RunLengthEncoding.runLengthEncoding("a"));
        assertArrayEquals(new String[]{"b", "c"}, CommonCharacters.commonCharacters(new String[]{"abc", "bcd", "cbaccd"}));
        assertTrue(GenerateDocument.generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"));
        assertFalse(GenerateDocument.generateDocument("a", "aa"));
        assertEquals(1, FirstNonRepeatingCharacter.firstNonRepeatingCharacter("abcdcaf"));
        assertEquals(-1, FirstNonRepeatingCharacter.firstNonRepeatingCharacter("aabb"));
        assertEquals(List.of(List.of("diaper", "repaid"), List.of("abc", "cba")),
                Semordnilap.semordnilap(new String[]{"diaper", "abc", "test", "cba", "repaid"}));
    }
}
