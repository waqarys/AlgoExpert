package veryhard;

import common.BinaryTree;
import common.LinkedListNode;
import org.junit.jupiter.api.Test;
import veryhard.arrays.*;
import veryhard.binarysearchtrees.RightSmallerThan;
import veryhard.binarytrees.*;
import veryhard.dynamicprogramming.*;
import veryhard.famousalgorithms.*;
import veryhard.graphs.*;
import veryhard.heaps.MergeSortedArrays;
import veryhard.linkedlists.*;
import veryhard.recursion.*;
import veryhard.searching.*;
import veryhard.sorting.*;
import veryhard.stacks.LargestPark;
import veryhard.strings.*;
import veryhard.tries.StringsMadeUpOfStrings;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

/** One test per Very Hard problem, each covering the sample plus edge cases. */
class VeryHardProblemsTest {
    // ---------- Arrays ----------
    @Test void apartmentHunting() {
        var blocks = List.of(
                Map.of("gym", false, "school", true, "store", false),
                Map.of("gym", true, "school", false, "store", false),
                Map.of("gym", true, "school", true, "store", false),
                Map.of("gym", false, "school", true, "store", false),
                Map.of("gym", false, "school", true, "store", true));
        assertEquals(3, ApartmentHunting.apartmentHunting(blocks, new String[]{"gym", "school", "store"}));
        assertEquals(0, ApartmentHunting.apartmentHunting(List.of(Map.of("gym", true)), new String[]{"gym"}));
        assertEquals(0, ApartmentHunting.apartmentHunting(List.of(Map.of("a", true), Map.of("a", false), Map.of("a", true)), new String[]{"a"}), "ties go to lowest index");
    }

    @Test void calendarMatching() {
        var slots = CalendarMatching.calendarMatching(
                List.of(new String[]{"9:00", "10:30"}, new String[]{"12:00", "13:00"}, new String[]{"16:00", "18:00"}), new String[]{"9:00", "20:00"},
                List.of(new String[]{"10:00", "11:30"}, new String[]{"12:30", "14:30"}, new String[]{"14:30", "15:00"}, new String[]{"16:00", "17:00"}), new String[]{"10:00", "18:30"}, 30);
        assertEquals(3, slots.size());
        assertArrayEquals(new String[]{"11:30", "12:00"}, slots.get(0));
        assertArrayEquals(new String[]{"15:00", "16:00"}, slots.get(1));
        assertArrayEquals(new String[]{"18:00", "18:30"}, slots.get(2));
        var free = CalendarMatching.calendarMatching(List.of(), new String[]{"9:00", "17:00"}, List.of(), new String[]{"9:00", "17:00"}, 60);
        assertEquals(1, free.size());
        assertArrayEquals(new String[]{"9:00", "17:00"}, free.get(0));
        assertTrue(CalendarMatching.calendarMatching(List.of(), new String[]{"9:00", "10:00"}, List.of(), new String[]{"9:30", "10:00"}, 45).isEmpty(), "slot too short");
    }

    @Test void waterfallStreams() {
        double[][] grid = {
                {0, 0, 0, 0, 0, 0, 0}, {1, 0, 0, 0, 0, 0, 0}, {0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0},
                {1, 1, 1, 0, 0, 1, 0}, {0, 0, 0, 0, 0, 0, 1}, {0, 0, 0, 0, 0, 0, 0}};
        assertArrayEquals(new double[]{0, 0, 0, 25, 25, 0, 0}, WaterfallStreams.waterfallStreams(grid, 3), 1e-9);
        assertArrayEquals(new double[]{0, 100}, WaterfallStreams.waterfallStreams(new double[][]{{0, 0}, {0, 0}}, 1), 1e-9);
        assertArrayEquals(new double[]{50, 0, 50}, WaterfallStreams.waterfallStreams(new double[][]{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}, 1), 1e-9, "even split");
        assertArrayEquals(new double[]{0, 0, 50}, WaterfallStreams.waterfallStreams(new double[][]{{0, 0, 0}, {1, 1, 0}, {0, 0, 0}}, 1), 1e-9, "left half lost at the wall");
    }

    @Test void minimumAreaRectangle() {
        assertEquals(3, MinimumAreaRectangle.minimumAreaRectangle(new int[][]{{1, 5}, {5, 1}, {4, 2}, {2, 4}, {2, 2}, {1, 2}, {4, 5}, {2, 5}, {-1, -2}}));
        assertEquals(0, MinimumAreaRectangle.minimumAreaRectangle(new int[][]{{0, 0}, {1, 1}}));
        assertEquals(0, MinimumAreaRectangle.minimumAreaRectangle(new int[][]{}));
        assertEquals(4, MinimumAreaRectangle.minimumAreaRectangle(new int[][]{{-1, -1}, {-1, 1}, {1, -1}, {1, 1}}));
    }

    @Test void lineThroughPoints() {
        assertEquals(4, LineThroughPoints.lineThroughPoints(new int[][]{{1, 1}, {2, 2}, {3, 3}, {0, 4}, {-2, 6}, {4, 0}, {2, 1}}));
        assertEquals(1, LineThroughPoints.lineThroughPoints(new int[][]{{5, 5}}));
        assertEquals(0, LineThroughPoints.lineThroughPoints(new int[][]{}));
        assertEquals(3, LineThroughPoints.lineThroughPoints(new int[][]{{0, 0}, {0, 5}, {0, -3}}), "vertical line");
    }

    // ---------- BST / Binary trees ----------
    @Test void rightSmallerThan() {
        assertEquals(List.of(5, 4, 4, 0, 1, 1, 0), RightSmallerThan.rightSmallerThan(List.of(8, 5, 11, -1, 3, 4, 2)));
        assertEquals(List.of(), RightSmallerThan.rightSmallerThan(List.of()));
        assertEquals(List.of(0, 0, 0), RightSmallerThan.rightSmallerThan(List.of(2, 2, 2)), "equal is not smaller");
        assertEquals(List.of(0), RightSmallerThan.rightSmallerThan(List.of(9)));
    }

    @Test void iterativeInOrderTraversal() {
        List<Integer> seen = new ArrayList<>();
        IterativeInOrderTraversal.iterativeInOrderTraversal(BinaryTree.fromLevelOrder(1, 2, 3, 4, null, 6, 7, null, 9), n -> seen.add(n.value));
        assertEquals(List.of(4, 9, 2, 1, 6, 3, 7), seen);
        List<Integer> one = new ArrayList<>();
        IterativeInOrderTraversal.iterativeInOrderTraversal(new BinaryTree(5), n -> one.add(n.value));
        assertEquals(List.of(5), one);
    }

    @Test void flattenBinaryTree() {
        BinaryTree head = FlattenBinaryTree.flattenBinaryTree(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6));
        List<Integer> vals = new ArrayList<>();
        BinaryTree last = null;
        for (BinaryTree c = head; c != null; c = c.right) { vals.add(c.value); last = c; }
        assertEquals(List.of(4, 2, 5, 1, 6, 3), vals);
        assertEquals(6, last.left.value);
        assertNull(head.left);
        BinaryTree single = FlattenBinaryTree.flattenBinaryTree(new BinaryTree(1));
        assertNull(single.left);
        assertNull(single.right);
    }

    @Test void rightSiblingTree() {
        BinaryTree r = RightSiblingTree.rightSiblingTree(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7));
        assertEquals(3, r.left.right.value);
        assertNull(r.right);
        assertEquals(5, r.left.left.right.value);
        assertEquals(6, r.left.left.right.right.value);
        BinaryTree s = RightSiblingTree.rightSiblingTree(new BinaryTree(1));
        assertNull(s.right);
    }

    @Test void allKindsOfNodeDepths() {
        assertEquals(26, AllKindsOfNodeDepths.allKindsOfNodeDepths(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7, 8, 9)));
        assertEquals(0, AllKindsOfNodeDepths.allKindsOfNodeDepths(new BinaryTree(1)));
        assertEquals(4, AllKindsOfNodeDepths.allKindsOfNodeDepths(BinaryTree.fromLevelOrder(1, 2, null, 3)));
    }

    @Test void compareLeafTraversal() {
        assertTrue(CompareLeafTraversal.compareLeafTraversal(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, null, 6, null, null, 7, 8),
                BinaryTree.fromLevelOrder(1, 2, 3, 4, 7, null, 5, null, null, null, null, 8, 6)));
        assertFalse(CompareLeafTraversal.compareLeafTraversal(BinaryTree.fromLevelOrder(1, 2, 3), BinaryTree.fromLevelOrder(1, 3, 2)));
        assertTrue(CompareLeafTraversal.compareLeafTraversal(new BinaryTree(4), BinaryTree.fromLevelOrder(9, 4)));
        assertFalse(CompareLeafTraversal.compareLeafTraversal(BinaryTree.fromLevelOrder(1, 2, 3), BinaryTree.fromLevelOrder(1, 2)), "different leaf counts");
    }

    // ---------- Dynamic programming ----------
    @Test void maxProfitWithKTransactions() {
        assertEquals(93, MaxProfitWithKTransactions.maxProfitWithKTransactions(new int[]{5, 11, 3, 50, 60, 90}, 2));
        assertEquals(0, MaxProfitWithKTransactions.maxProfitWithKTransactions(new int[]{}, 2));
        assertEquals(0, MaxProfitWithKTransactions.maxProfitWithKTransactions(new int[]{5, 4, 3}, 3), "falling prices");
        assertEquals(0, MaxProfitWithKTransactions.maxProfitWithKTransactions(new int[]{1, 5}, 0));
    }

    @Test void palindromePartitioningMinCuts() {
        assertEquals(2, PalindromePartitioningMinCuts.palindromePartitioningMinCuts("noonabbad"));
        assertEquals(0, PalindromePartitioningMinCuts.palindromePartitioningMinCuts("aba"));
        assertEquals(0, PalindromePartitioningMinCuts.palindromePartitioningMinCuts(""));
        assertEquals(2, PalindromePartitioningMinCuts.palindromePartitioningMinCuts("abc"));
    }

    @Test void longestIncreasingSubsequence() {
        assertEquals(List.of(-24, 2, 3, 5, 6, 35), LongestIncreasingSubsequence.longestIncreasingSubsequence(new int[]{5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35}));
        assertEquals(List.of(), LongestIncreasingSubsequence.longestIncreasingSubsequence(new int[]{}));
        assertEquals(1, LongestIncreasingSubsequence.longestIncreasingSubsequence(new int[]{3, 3, 3}).size(), "strictly increasing");
    }

    @Test void longestStringChain() {
        assertEquals(List.of("abcdef", "abcde", "abde", "ade", "ae"), LongestStringChain.longestStringChain(List.of("abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef")));
        assertEquals(List.of(), LongestStringChain.longestStringChain(List.of("abc", "xyz")));
        assertEquals(List.of(), LongestStringChain.longestStringChain(List.of()));
    }

    @Test void squareOfZeroes() {
        assertTrue(SquareOfZeroes.squareOfZeroes(new int[][]{{1, 1, 1, 0, 1, 0}, {0, 0, 0, 0, 0, 1}, {0, 1, 1, 1, 0, 1}, {0, 0, 0, 1, 0, 1}, {0, 1, 1, 1, 0, 1}, {0, 0, 0, 0, 0, 1}}));
        assertFalse(SquareOfZeroes.squareOfZeroes(new int[][]{{1, 0}, {0, 0}}));
        assertFalse(SquareOfZeroes.squareOfZeroes(new int[][]{{0}}), "1x1 doesn't count");
        assertTrue(SquareOfZeroes.squareOfZeroes(new int[][]{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}), "interior may contain 1s");
    }

    // ---------- Famous ----------
    @Test void knuthMorrisPrattAlgorithm() {
        assertTrue(KnuthMorrisPrattAlgorithm.knuthMorrisPrattAlgorithm("aefoaefcdaefcdaed", "aefcdaed"));
        assertFalse(KnuthMorrisPrattAlgorithm.knuthMorrisPrattAlgorithm("testwhere", "wert"));
        assertTrue(KnuthMorrisPrattAlgorithm.knuthMorrisPrattAlgorithm("abc", ""));
        assertFalse(KnuthMorrisPrattAlgorithm.knuthMorrisPrattAlgorithm("", "a"));
        assertTrue(KnuthMorrisPrattAlgorithm.knuthMorrisPrattAlgorithm("aaaab", "aaab"));
    }

    @Test void aStarAlgorithm() {
        int[][] grid = {{0, 0, 0, 0, 0}, {0, 1, 1, 1, 0}, {0, 0, 0, 0, 0}, {1, 0, 1, 1, 1}, {0, 0, 0, 0, 0}};
        int[][] path = AStarAlgorithm.aStarAlgorithm(0, 1, 4, 3, grid);
        assertEquals(9, path.length);
        assertArrayEquals(new int[]{0, 1}, path[0]);
        assertArrayEquals(new int[]{4, 3}, path[path.length - 1]);
        assertEquals(0, AStarAlgorithm.aStarAlgorithm(0, 0, 0, 2, new int[][]{{0, 1, 0}}).length);
        assertEquals(1, AStarAlgorithm.aStarAlgorithm(0, 0, 0, 0, new int[][]{{0}}).length);
    }

    // ---------- Graphs ----------
    @Test void rectangleMania() {
        assertEquals(3, RectangleMania.rectangleMania(new int[][]{{0, 0}, {0, 1}, {1, 1}, {1, 0}, {2, 1}, {2, 0}, {3, 1}, {0, 3}}));
        assertEquals(0, RectangleMania.rectangleMania(new int[][]{{0, 0}, {1, 1}}));
        assertEquals(0, RectangleMania.rectangleMania(new int[][]{}));
    }

    @Test void airportConnections() {
        List<String> airports = List.of("A", "B", "C", "D", "E");
        assertEquals(2, AirportConnections.airportConnections(airports, List.of(List.of("A", "B"), List.of("C", "D"), List.of("D", "C")), "A"));
        assertEquals(0, AirportConnections.airportConnections(List.of("A", "B"), List.of(List.of("A", "B")), "A"));
        assertEquals(0, AirportConnections.airportConnections(List.of("A"), List.of(), "A"));
        assertEquals(1, AirportConnections.airportConnections(List.of("A", "B"), List.of(List.of("B", "A")), "A"));
    }

    @Test void detectArbitrage() {
        assertTrue(DetectArbitrage.detectArbitrage(new double[][]{{1.0, 0.8631, 0.5903}, {1.1586, 1.0, 0.6849}, {1.6939, 1.46, 1.0}}));
        assertFalse(DetectArbitrage.detectArbitrage(new double[][]{{1, 2}, {0.5, 1}}));
        assertFalse(DetectArbitrage.detectArbitrage(new double[][]{{1}}));
    }

    @Test void twoEdgeConnectedGraph() {
        assertTrue(TwoEdgeConnectedGraph.twoEdgeConnectedGraph(new int[][]{{1, 2, 5}, {0, 2}, {0, 1, 3}, {2, 4, 5}, {3, 5}, {0, 3, 4}}));
        assertFalse(TwoEdgeConnectedGraph.twoEdgeConnectedGraph(new int[][]{{1}, {0}}));
        assertTrue(TwoEdgeConnectedGraph.twoEdgeConnectedGraph(new int[][]{}));
        assertFalse(TwoEdgeConnectedGraph.twoEdgeConnectedGraph(new int[][]{{1, 2}, {0, 2}, {0, 1}, {}}), "disconnected");
    }

    // ---------- Heaps / Linked lists ----------
    @Test void mergeSortedArrays() {
        assertEquals(List.of(-124, -1, 1, 5, 9, 21, 81, 121), MergeSortedArrays.mergeSortedArrays(List.of(List.of(1, 5, 9, 21), List.of(-1), List.of(-124, 81, 121))));
        assertEquals(List.of(), MergeSortedArrays.mergeSortedArrays(List.of(List.of())));
        assertEquals(List.of(1, 1, 2), MergeSortedArrays.mergeSortedArrays(List.of(List.of(1, 2), List.of(1))));
    }

    @Test void lruCache() {
        var lru = new LruCache(3);
        assertNull(lru.getMostRecentKey());
        lru.insertKeyValuePair("b", 2); lru.insertKeyValuePair("a", 1); lru.insertKeyValuePair("c", 3);
        assertEquals("c", lru.getMostRecentKey());
        assertEquals(1, lru.getValueFromKey("a"));
        lru.insertKeyValuePair("d", 4);
        assertNull(lru.getValueFromKey("b"));
        lru.insertKeyValuePair("a", 10);
        assertEquals(10, lru.getValueFromKey("a"), "update replaces value");
        var one = new LruCache(1);
        one.insertKeyValuePair("x", 1); one.insertKeyValuePair("y", 2);
        assertNull(one.getValueFromKey("x"));
    }

    @Test void rearrangeLinkedList() {
        assertEquals(List.of(0, 2, 1, 3, 3, 5), LinkedListNode.toList(RearrangeLinkedList.rearrangeLinkedList(LinkedListNode.of(3, 0, 5, 2, 1, 3), 3)));
        assertEquals(List.of(1, 2), LinkedListNode.toList(RearrangeLinkedList.rearrangeLinkedList(LinkedListNode.of(1, 2), 5)));
        assertEquals(List.of(7, 8), LinkedListNode.toList(RearrangeLinkedList.rearrangeLinkedList(LinkedListNode.of(7, 8), -1)));
        assertEquals(List.of(4), LinkedListNode.toList(RearrangeLinkedList.rearrangeLinkedList(LinkedListNode.of(4), 4)));
    }

    @Test void linkedListPalindrome() {
        assertTrue(LinkedListPalindrome.linkedListPalindrome(LinkedListNode.of(0, 1, 2, 2, 1, 0)));
        assertFalse(LinkedListPalindrome.linkedListPalindrome(LinkedListNode.of(0, 1)));
        assertTrue(LinkedListPalindrome.linkedListPalindrome(LinkedListNode.of(1)));
        var odd = LinkedListNode.of(1, 2, 1);
        assertTrue(LinkedListPalindrome.linkedListPalindrome(odd));
        assertEquals(List.of(1, 2, 1), LinkedListNode.toList(odd), "list restored");
    }

    @Test void zipLinkedList() {
        assertEquals(List.of(1, 6, 2, 5, 3, 4), LinkedListNode.toList(ZipLinkedList.zipLinkedList(LinkedListNode.of(1, 2, 3, 4, 5, 6))));
        assertEquals(List.of(1, 3, 2), LinkedListNode.toList(ZipLinkedList.zipLinkedList(LinkedListNode.of(1, 2, 3))));
        assertEquals(List.of(1), LinkedListNode.toList(ZipLinkedList.zipLinkedList(LinkedListNode.of(1))));
    }

    @Test void nodeSwap() {
        assertEquals(List.of(1, 0, 3, 2, 5, 4), LinkedListNode.toList(NodeSwap.nodeSwap(LinkedListNode.of(0, 1, 2, 3, 4, 5))));
        assertEquals(List.of(1), LinkedListNode.toList(NodeSwap.nodeSwap(LinkedListNode.of(1))));
        assertEquals(List.of(2, 1, 3), LinkedListNode.toList(NodeSwap.nodeSwap(LinkedListNode.of(1, 2, 3))));
    }

    // ---------- Recursion / Searching / Sorting ----------
    @Test void numberOfBinaryTreeTopologies() {
        assertEquals(5, NumberOfBinaryTreeTopologies.numberOfBinaryTreeTopologies(3));
        assertEquals(1, NumberOfBinaryTreeTopologies.numberOfBinaryTreeTopologies(0));
        assertEquals(16796, NumberOfBinaryTreeTopologies.numberOfBinaryTreeTopologies(10));
    }

    @Test void nonAttackingQueens() {
        assertEquals(2, NonAttackingQueens.nonAttackingQueens(4));
        assertEquals(92, NonAttackingQueens.nonAttackingQueens(8));
        assertEquals(1, NonAttackingQueens.nonAttackingQueens(1));
        assertEquals(0, NonAttackingQueens.nonAttackingQueens(2));
    }

    @Test void medianOfTwoSortedArrays() {
        assertEquals(3.5f, MedianOfTwoSortedArrays.medianOfTwoSortedArrays(new int[]{1, 3, 4, 5}, new int[]{2, 3, 6, 7}), 1e-6);
        assertEquals(2f, MedianOfTwoSortedArrays.medianOfTwoSortedArrays(new int[]{1, 3}, new int[]{2}), 1e-6);
        assertEquals(4f, MedianOfTwoSortedArrays.medianOfTwoSortedArrays(new int[]{}, new int[]{4}), 1e-6);
        assertEquals(-1.5f, MedianOfTwoSortedArrays.medianOfTwoSortedArrays(new int[]{-2}, new int[]{-1}), 1e-6);
    }

    @Test void optimalAssemblyLine() {
        assertEquals(60, OptimalAssemblyLine.optimalAssemblyLine(new int[]{15, 15, 30, 30, 45}, 3));
        assertEquals(135, OptimalAssemblyLine.optimalAssemblyLine(new int[]{15, 15, 30, 30, 45}, 1));
        assertEquals(45, OptimalAssemblyLine.optimalAssemblyLine(new int[]{15, 15, 30, 30, 45}, 5));
        assertEquals(7, OptimalAssemblyLine.optimalAssemblyLine(new int[]{7}, 1));
    }

    @Test void mergeSort() {
        assertArrayEquals(new int[]{2, 3, 5, 5, 6, 8, 9}, MergeSort.mergeSort(new int[]{8, 5, 2, 9, 5, 6, 3}));
        assertArrayEquals(new int[]{}, MergeSort.mergeSort(new int[]{}));
        assertArrayEquals(new int[]{-2, -1}, MergeSort.mergeSort(new int[]{-1, -2}));
    }

    @Test void countInversions() {
        assertEquals(5, CountInversions.countInversions(new int[]{2, 3, 3, 1, 9, 5, 6}));
        assertEquals(0, CountInversions.countInversions(new int[]{1, 2}));
        assertEquals(0, CountInversions.countInversions(new int[]{}));
        assertEquals(3, CountInversions.countInversions(new int[]{3, 2, 1}));
        assertEquals(0, CountInversions.countInversions(new int[]{2, 2}), "equal values are not inversions");
    }

    // ---------- Stacks / Strings / Tries ----------
    @Test void largestPark() {
        boolean[][] land = {
                {false, true, true, true, false},
                {false, false, false, true, false},
                {false, false, false, false, false},
                {false, true, true, true, true}};
        assertEquals(6, LargestPark.largestPark(land));
        assertEquals(0, LargestPark.largestPark(new boolean[][]{{true}}));
        assertEquals(4, LargestPark.largestPark(new boolean[][]{{false, false}, {false, false}}));
        assertEquals(0, LargestPark.largestPark(new boolean[][]{}));
    }

    @Test void smallestSubstringContaining() {
        assertEquals("f$axb$", SmallestSubstringContaining.smallestSubstringContaining("abcd$ef$axb$c$", "$$abf"));
        assertEquals("", SmallestSubstringContaining.smallestSubstringContaining("abc", "z"));
        assertEquals("a", SmallestSubstringContaining.smallestSubstringContaining("a", "a"));
        assertEquals("", SmallestSubstringContaining.smallestSubstringContaining("a", "aa"), "multiplicity matters");
    }

    @Test void longestBalancedSubstring() {
        assertEquals(4, LongestBalancedSubstring.longestBalancedSubstring("(()))("));
        assertEquals(6, LongestBalancedSubstring.longestBalancedSubstring(")(()())("));
        assertEquals(4, LongestBalancedSubstring.longestBalancedSubstring("(()()"));
        assertEquals(0, LongestBalancedSubstring.longestBalancedSubstring(""));
        assertEquals(0, LongestBalancedSubstring.longestBalancedSubstring(")("));
    }

    @Test void stringsMadeUpOfStrings() {
        assertArrayEquals(new String[]{"superman", "batman"}, StringsMadeUpOfStrings.stringsMadeUpOfStrings(new String[]{"superman", "batman", "bat", "man"}, new String[]{"super", "man", "bat"}));
        assertArrayEquals(new String[]{}, StringsMadeUpOfStrings.stringsMadeUpOfStrings(new String[]{"abc"}, new String[]{"abc"}), "needs two or more pieces");
        assertArrayEquals(new String[]{"aaa"}, StringsMadeUpOfStrings.stringsMadeUpOfStrings(new String[]{"aaa"}, new String[]{"a"}), "reuse allowed");
        assertArrayEquals(new String[]{}, StringsMadeUpOfStrings.stringsMadeUpOfStrings(new String[]{}, new String[]{"a"}));
    }
}
