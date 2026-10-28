package easy;

import common.BST;
import common.BinaryTree;
import common.LinkedListNode;
import easy.arrays.*;
import easy.binarysearchtrees.FindClosestValueInBst;
import easy.binarytrees.*;
import easy.graphs.DepthFirstSearch;
import easy.greedyalgorithms.*;
import easy.linkedlists.*;
import easy.recursion.*;
import easy.searching.*;
import easy.sorting.*;
import easy.strings.*;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

/** One test per Easy problem, each covering the sample plus edge cases. */
class EasyProblemsTest {
    // ---------- Arrays ----------
    @Test void twoNumberSum() {
        int[] r = TwoNumberSum.twoNumberSum(new int[]{3, 5, -4, 8, 11, 1, -1, 6}, 10);
        assertEquals(10, r[0] + r[1]);
        assertEquals(0, TwoNumberSum.twoNumberSum(new int[]{}, 5).length);
        assertEquals(0, TwoNumberSum.twoNumberSum(new int[]{5}, 10).length, "cannot use one element twice");
        int[] neg = TwoNumberSum.twoNumberSum(new int[]{-7, -3, 4}, -10);
        assertEquals(-10, neg[0] + neg[1]);
    }

    @Test void validateSubsequence() {
        assertTrue(ValidateSubsequence.isValidSubsequence(List.of(5, 1, 22, 25, 6, -1, 8, 10), List.of(1, 6, -1, 10)));
        assertTrue(ValidateSubsequence.isValidSubsequence(List.of(1, 1, 1), List.of(1, 1)));
        assertFalse(ValidateSubsequence.isValidSubsequence(List.of(1, 2, 3), List.of(3, 2)));
        assertFalse(ValidateSubsequence.isValidSubsequence(List.of(1), List.of(1, 1)));
        assertTrue(ValidateSubsequence.isValidSubsequence(List.of(4), List.of(4)));
    }

    @Test void sortedSquaredArray() {
        assertArrayEquals(new int[]{1, 4, 9, 25}, SortedSquaredArray.sortedSquaredArray(new int[]{-3, -1, 2, 5}));
        assertArrayEquals(new int[]{}, SortedSquaredArray.sortedSquaredArray(new int[]{}));
        assertArrayEquals(new int[]{49}, SortedSquaredArray.sortedSquaredArray(new int[]{-7}));
        assertArrayEquals(new int[]{4, 4, 9}, SortedSquaredArray.sortedSquaredArray(new int[]{-3, -2, 2}));
    }

    @Test void tournamentWinner() {
        var comps = List.of(List.of("HTML", "C#"), List.of("C#", "Python"), List.of("Python", "HTML"));
        assertEquals("Python", TournamentWinner.tournamentWinner(comps, List.of(0, 0, 1)));
        assertEquals("A", TournamentWinner.tournamentWinner(List.of(List.of("A", "B")), List.of(1)));
        assertEquals("B", TournamentWinner.tournamentWinner(List.of(List.of("A", "B")), List.of(0)));
    }

    @Test void nonConstructibleChange() {
        assertEquals(20, NonConstructibleChange.nonConstructibleChange(new int[]{5, 7, 1, 1, 2, 3, 22}));
        assertEquals(1, NonConstructibleChange.nonConstructibleChange(new int[]{}));
        assertEquals(2, NonConstructibleChange.nonConstructibleChange(new int[]{1}));
        assertEquals(6, NonConstructibleChange.nonConstructibleChange(new int[]{1, 1, 1, 1, 1}));
    }

    @Test void transposeMatrix() {
        assertArrayEquals(new int[][]{{1, 3}, {2, 4}}, TransposeMatrix.transposeMatrix(new int[][]{{1, 2}, {3, 4}}));
        assertArrayEquals(new int[][]{{1}, {2}}, TransposeMatrix.transposeMatrix(new int[][]{{1, 2}}));
        assertArrayEquals(new int[][]{{-5}}, TransposeMatrix.transposeMatrix(new int[][]{{-5}}));
    }

    // ---------- BST / Binary trees / Graphs ----------
    @Test void findClosestValueInBst() {
        BST t = BST.of(10, 5, 15, 2, 5, 13, 22, 1, 14);
        assertEquals(13, FindClosestValueInBst.findClosestValueInBst(t, 12));
        assertEquals(1, FindClosestValueInBst.findClosestValueInBst(t, -5));
        assertEquals(22, FindClosestValueInBst.findClosestValueInBst(t, 1000));
        assertEquals(7, FindClosestValueInBst.findClosestValueInBst(new BST(7), 3));
    }

    @Test void branchSums() {
        assertEquals(List.of(15, 16, 18, 10, 11), BranchSums.branchSums(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)));
        assertEquals(List.of(4), BranchSums.branchSums(new BinaryTree(4)));
        assertEquals(List.of(-3), BranchSums.branchSums(BinaryTree.fromLevelOrder(-1, -2)));
    }

    @Test void nodeDepths() {
        assertEquals(16, NodeDepths.nodeDepths(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7, 8, 9)));
        assertEquals(0, NodeDepths.nodeDepths(new BinaryTree(1)));
        assertEquals(3, NodeDepths.nodeDepths(BinaryTree.fromLevelOrder(1, 2, null, 3)));
    }

    @Test void evaluateExpressionTree() {
        assertEquals(6, EvaluateExpressionTree.evaluateExpressionTree(BinaryTree.fromLevelOrder(-1, -2, -3, -4, 2, 8, 3, 2, 3)));
        assertEquals(7, EvaluateExpressionTree.evaluateExpressionTree(new BinaryTree(7)));
        assertEquals(-1, EvaluateExpressionTree.evaluateExpressionTree(BinaryTree.fromLevelOrder(-2, 2, 3)));
        assertEquals(2, EvaluateExpressionTree.evaluateExpressionTree(BinaryTree.fromLevelOrder(-3, 5, 2)), "division truncates");
    }

    @Test void depthFirstSearch() {
        var a = new DepthFirstSearch.Node("A").addChild("B").addChild("C");
        a.children.get(0).addChild("D");
        assertEquals(List.of("A", "B", "D", "C"), a.depthFirstSearch(new ArrayList<>()));
        assertEquals(List.of("X"), new DepthFirstSearch.Node("X").depthFirstSearch(new ArrayList<>()));
    }

    // ---------- Greedy ----------
    @Test void minimumWaitingTime() {
        assertEquals(17, MinimumWaitingTime.minimumWaitingTime(new int[]{3, 2, 1, 2, 6}));
        assertEquals(0, MinimumWaitingTime.minimumWaitingTime(new int[]{5}));
        assertEquals(6, MinimumWaitingTime.minimumWaitingTime(new int[]{2, 2, 2}));
    }

    @Test void classPhotos() {
        assertTrue(ClassPhotos.classPhotos(new ArrayList<>(List.of(5, 8, 1, 3, 4)), new ArrayList<>(List.of(6, 9, 2, 4, 5))));
        assertFalse(ClassPhotos.classPhotos(new ArrayList<>(List.of(5, 5)), new ArrayList<>(List.of(5, 6))));
        assertTrue(ClassPhotos.classPhotos(new ArrayList<>(List.of(6)), new ArrayList<>(List.of(5))));
        assertFalse(ClassPhotos.classPhotos(new ArrayList<>(List.of(5)), new ArrayList<>(List.of(5))), "equal heights fail");
    }

    @Test void tandemBicycle() {
        assertEquals(32, TandemBicycle.tandemBicycle(new int[]{5, 5, 3, 9, 2}, new int[]{3, 6, 7, 2, 1}, true));
        assertEquals(25, TandemBicycle.tandemBicycle(new int[]{5, 5, 3, 9, 2}, new int[]{3, 6, 7, 2, 1}, false));
        assertEquals(0, TandemBicycle.tandemBicycle(new int[]{}, new int[]{}, true));
        assertEquals(4, TandemBicycle.tandemBicycle(new int[]{4}, new int[]{1}, false));
    }

    @Test void optimalFreelancing() {
        List<Map<String, Integer>> jobs = List.of(Map.of("deadline", 1, "payment", 1), Map.of("deadline", 2, "payment", 1), Map.of("deadline", 2, "payment", 2));
        assertEquals(3, OptimalFreelancing.optimalFreelancing(jobs));
        assertEquals(0, OptimalFreelancing.optimalFreelancing(List.of()));
        assertEquals(2, OptimalFreelancing.optimalFreelancing(List.of(Map.of("deadline", 1, "payment", 1), Map.of("deadline", 1, "payment", 2))));
        List<Map<String, Integer>> many = new ArrayList<>();
        for (int i = 1; i <= 10; i++) many.add(Map.of("deadline", 10, "payment", i));
        assertEquals(4 + 5 + 6 + 7 + 8 + 9 + 10, OptimalFreelancing.optimalFreelancing(many), "only 7 days available");
    }

    // ---------- Linked lists ----------
    @Test void removeDuplicatesFromLinkedList() {
        assertEquals(List.of(1, 3, 4, 5, 6), LinkedListNode.toList(RemoveDuplicatesFromLinkedList.removeDuplicatesFromLinkedList(LinkedListNode.of(1, 1, 3, 4, 4, 4, 5, 6, 6))));
        assertEquals(List.of(2), LinkedListNode.toList(RemoveDuplicatesFromLinkedList.removeDuplicatesFromLinkedList(LinkedListNode.of(2, 2, 2))));
        assertEquals(List.of(1), LinkedListNode.toList(RemoveDuplicatesFromLinkedList.removeDuplicatesFromLinkedList(LinkedListNode.of(1))));
    }

    @Test void middleNode() {
        assertEquals(3, MiddleNode.middleNode(LinkedListNode.of(1, 2, 3, 4, 5)).value);
        assertEquals(3, MiddleNode.middleNode(LinkedListNode.of(1, 2, 3, 4)).value);
        assertEquals(9, MiddleNode.middleNode(LinkedListNode.of(9)).value);
    }

    // ---------- Recursion ----------
    @Test void nthFibonacci() {
        assertEquals(0, NthFibonacci.getNthFib(1));
        assertEquals(1, NthFibonacci.getNthFib(2));
        assertEquals(5, NthFibonacci.getNthFib(6));
        assertEquals(4181, NthFibonacci.getNthFib(20));
    }

    @Test void productSum() {
        assertEquals(12, ProductSum.productSum(List.of(5, 2, List.of(7, -1), 3, List.of(6, List.of(-13, 8), 4))));
        assertEquals(0, ProductSum.productSum(List.of()));
        assertEquals(6, ProductSum.productSum(List.of(List.of(List.of(1)))));
    }

    // ---------- Searching ----------
    @Test void binarySearch() {
        assertEquals(3, BinarySearch.binarySearch(new int[]{0, 1, 21, 33, 45, 45, 61, 71, 72, 73}, 33));
        assertEquals(-1, BinarySearch.binarySearch(new int[]{1, 5}, 3));
        assertEquals(-1, BinarySearch.binarySearch(new int[]{}, 3));
        assertEquals(0, BinarySearch.binarySearch(new int[]{-4}, -4));
    }

    @Test void findThreeLargestNumbers() {
        assertArrayEquals(new int[]{18, 141, 541}, FindThreeLargestNumbers.findThreeLargestNumbers(new int[]{141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7}));
        assertArrayEquals(new int[]{10, 10, 12}, FindThreeLargestNumbers.findThreeLargestNumbers(new int[]{10, 5, 9, 10, 12}));
        assertArrayEquals(new int[]{-3, -2, -1}, FindThreeLargestNumbers.findThreeLargestNumbers(new int[]{-1, -2, -3, -7}));
    }

    // ---------- Sorting ----------
    private static void checkSort(java.util.function.UnaryOperator<int[]> sorter) {
        assertArrayEquals(new int[]{2, 3, 5, 5, 6, 8, 9}, sorter.apply(new int[]{8, 5, 2, 9, 5, 6, 3}));
        assertArrayEquals(new int[]{}, sorter.apply(new int[]{}));
        assertArrayEquals(new int[]{1}, sorter.apply(new int[]{1}));
        assertArrayEquals(new int[]{-3, -1, 0, 0}, sorter.apply(new int[]{0, -1, 0, -3}));
    }

    @Test void bubbleSort() { checkSort(BubbleSort::bubbleSort); }
    @Test void insertionSort() { checkSort(InsertionSort::insertionSort); }
    @Test void selectionSort() { checkSort(SelectionSort::selectionSort); }

    // ---------- Strings ----------
    @Test void palindromeCheck() {
        assertTrue(PalindromeCheck.isPalindrome("abcdcba"));
        assertTrue(PalindromeCheck.isPalindrome(""));
        assertTrue(PalindromeCheck.isPalindrome("a"));
        assertFalse(PalindromeCheck.isPalindrome("ab"));
    }

    @Test void caesarCipherEncryptor() {
        assertEquals("zab", CaesarCipherEncryptor.caesarCypherEncryptor("xyz", 2));
        assertEquals("abc", CaesarCipherEncryptor.caesarCypherEncryptor("abc", 52));
        assertEquals("", CaesarCipherEncryptor.caesarCypherEncryptor("", 3));
    }

    @Test void runLengthEncoding() {
        assertEquals("9A4A2B4C2D", RunLengthEncoding.runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"));
        assertEquals("1a", RunLengthEncoding.runLengthEncoding("a"));
        assertEquals("9a", RunLengthEncoding.runLengthEncoding("aaaaaaaaa"));
        assertEquals("1a1b1a", RunLengthEncoding.runLengthEncoding("aba"));
    }

    @Test void commonCharacters() {
        assertArrayEquals(new String[]{"b", "c"}, CommonCharacters.commonCharacters(new String[]{"abc", "bcd", "cbaccd"}));
        assertArrayEquals(new String[]{"a", "b"}, CommonCharacters.commonCharacters(new String[]{"abba"}));
        assertArrayEquals(new String[]{}, CommonCharacters.commonCharacters(new String[]{"a", "b"}));
    }

    @Test void generateDocument() {
        assertTrue(GenerateDocument.generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"));
        assertFalse(GenerateDocument.generateDocument("a", "aa"));
        assertTrue(GenerateDocument.generateDocument("abc", ""));
        assertFalse(GenerateDocument.generateDocument("a", "A"), "case-sensitive");
    }

    @Test void firstNonRepeatingCharacter() {
        assertEquals(1, FirstNonRepeatingCharacter.firstNonRepeatingCharacter("abcdcaf"));
        assertEquals(-1, FirstNonRepeatingCharacter.firstNonRepeatingCharacter("aabb"));
        assertEquals(-1, FirstNonRepeatingCharacter.firstNonRepeatingCharacter(""));
        assertEquals(0, FirstNonRepeatingCharacter.firstNonRepeatingCharacter("z"));
    }

    @Test void semordnilap() {
        assertEquals(List.of(List.of("diaper", "repaid"), List.of("abc", "cba")),
                Semordnilap.semordnilap(new String[]{"diaper", "abc", "test", "cba", "repaid"}));
        assertEquals(List.of(), Semordnilap.semordnilap(new String[]{"aba"}), "palindromes don't pair with themselves");
        assertEquals(List.of(), Semordnilap.semordnilap(new String[]{}));
    }
}
