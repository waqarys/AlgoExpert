package hard;

import common.BST;
import common.BinaryTree;
import common.LinkedListNode;
import hard.arrays.*;
import hard.binarysearchtrees.*;
import hard.binarytrees.*;
import veryhard.binarytrees.IterativeInOrderTraversal;
import hard.dynamicprogramming.*;
import hard.famousalgorithms.*;
import hard.graphs.*;
import hard.heaps.*;
import hard.linkedlists.*;
import hard.recursion.*;
import hard.searching.*;
import hard.sorting.*;
import hard.stacks.*;
import hard.strings.*;
import hard.tries.MultiStringSearch;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class HardTest {
    @Test void arrays() {
        var q = FourNumberSum.fourNumberSum(new int[]{7, 6, 4, -1, 1, 2}, 16);
        assertEquals(2, q.size());
        for (Integer[] x : q) assertEquals(16, x[0] + x[1] + x[2] + x[3]);
        assertTrue(FourNumberSum.fourNumberSum(new int[]{1, 2, 3, 4}, 100).isEmpty());
        assertArrayEquals(new int[]{3, 9}, SubarraySort.subarraySort(new int[]{1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19}));
        assertArrayEquals(new int[]{-1, -1}, SubarraySort.subarraySort(new int[]{1, 2}));
        assertArrayEquals(new int[]{0, 7}, LargestRange.largestRange(new int[]{1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6}));
        assertArrayEquals(new int[]{4, 4}, LargestRange.largestRange(new int[]{4}));
        assertEquals(25, MinRewards.minRewards(new int[]{8, 4, 2, 1, 3, 6, 7, 9, 5}));
        assertEquals(1, MinRewards.minRewards(new int[]{5}));
        var zz = List.of(List.of(1, 3, 4, 10), List.of(2, 5, 9, 11), List.of(6, 8, 12, 15), List.of(7, 13, 14, 16));
        assertEquals(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), ZigzagTraverse.zigzagTraverse(zz));
        assertEquals(List.of(1, 2, 3), ZigzagTraverse.zigzagTraverse(List.of(List.of(1), List.of(2), List.of(3))));
        int[] ls = LongestSubarrayWithSum.longestSubarrayWithSum(new int[]{1, 2, 15, 3, 4, 5, 6, 7, 8}, 25);
        assertEquals(4, ls[1] - ls[0]);
        assertArrayEquals(new int[]{0, 1}, LongestSubarrayWithSum.longestSubarrayWithSum(new int[]{1, 2, 3, 0}, 3));
        assertEquals(0, LongestSubarrayWithSum.longestSubarrayWithSum(new int[]{5}, 3).length);
        assertEquals(1, KnightConnection.knightConnection(new int[]{0, 0}, new int[]{4, 2}));
        assertEquals(2, KnightConnection.knightConnection(new int[]{0, 0}, new int[]{1, 0}));
        assertEquals(0, KnightConnection.knightConnection(new int[]{1, 1}, new int[]{1, 1}));
        assertEquals(1, CountSquares.countSquares(new int[][]{{0, 0}, {0, 1}, {1, 1}, {1, 0}}));
        assertEquals(1, CountSquares.countSquares(new int[][]{{0, 1}, {1, 0}, {2, 1}, {1, 2}, {5, 5}}));
    }

    @Test void bst() {
        assertTrue(SameBsts.sameBsts(List.of(10, 15, 8, 12, 94, 81, 5, 2, 11), List.of(10, 8, 5, 15, 2, 12, 11, 94, 81)));
        assertFalse(SameBsts.sameBsts(List.of(1, 2), List.of(2, 1)));
        BST t = BST.of(5, 2, 7, 1, 4, 6, 8, 0, 3);
        BST n2 = t.left, n4 = t.left.right, n3 = t.left.right.left;
        assertTrue(ValidateThreeNodes.validateThreeNodes(t, n2, n3));
        assertFalse(ValidateThreeNodes.validateThreeNodes(n2, n3, n4));
        BST bad = BST.of(10, 7, 20, 3, 12, 8, 22, 2, 14);
        int tmp = bad.left.value; bad.left.value = bad.right.left.value; bad.right.left.value = tmp;
        RepairBst.repairBst(bad);
        assertEquals(List.of(2, 3, 7, 8, 10, 12, 14, 20, 22), BST.inOrder(bad));
        assertEquals(6, SumBsts.sumBsts(BinaryTree.fromLevelOrder(2, 1, 3)));
        assertEquals(0, SumBsts.sumBsts(BinaryTree.fromLevelOrder(2, 3, 1)));
    }

    @Test void binaryTrees() {
        assertEquals(18, MaxPathSumInBinaryTree.maxPathSum(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7)));
        assertEquals(-2, MaxPathSumInBinaryTree.maxPathSum(new BinaryTree(-2)));
        var d = FindNodesDistanceK.findNodesDistanceK(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, null, 6, null, null, null, null, 7, 8), 3, 2);
        d.sort(null);
        assertEquals(List.of(2, 7, 8), d);
        assertTrue(FindNodesDistanceK.findNodesDistanceK(new BinaryTree(1), 1, 3).isEmpty());
        List<Integer> seen = new ArrayList<>();
        IterativeInOrderTraversal.iterativeInOrderTraversal(BinaryTree.fromLevelOrder(1, 2, 3, 4, null, 6, 7, null, 9), n -> seen.add(n.value));
        assertEquals(List.of(4, 9, 2, 1, 6, 3, 7), seen);
    }

    @Test void dp() {
        assertEquals(List.of(List.of(110), List.of(10, 20, 30, 50)), MaxSumIncreasingSubsequence.maxSumIncreasingSubsequence(new int[]{10, 70, 20, 30, 50, 11, 30}));
        assertEquals(List.of(List.of(-1), List.of(-1)), MaxSumIncreasingSubsequence.maxSumIncreasingSubsequence(new int[]{-5, -1, -3}));
        assertEquals(List.of('X', 'Y', 'Z', 'W'), LongestCommonSubsequence.longestCommonSubsequence("ZXVVYZW", "XKYKZPW"));
        assertEquals(List.of(), LongestCommonSubsequence.longestCommonSubsequence("abc", "xyz"));
        assertEquals(4, MinNumberOfJumps.minNumberOfJumps(new int[]{3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3}));
        assertEquals(0, MinNumberOfJumps.minNumberOfJumps(new int[]{1}));
        assertEquals(48, WaterArea.waterArea(new int[]{0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3}));
        assertEquals(0, WaterArea.waterArea(new int[]{}));
        assertEquals(List.of(List.of(10), List.of(1, 3)), KnapsackProblem.knapsackProblem(new int[][]{{1, 2}, {4, 3}, {5, 6}, {6, 7}}, 10));
        assertEquals(List.of(List.of(0), List.of()), KnapsackProblem.knapsackProblem(new int[][]{{5, 20}}, 10));
        var ds = DiskStacking.diskStacking(List.of(new Integer[]{2, 1, 2}, new Integer[]{3, 2, 3}, new Integer[]{2, 2, 8}, new Integer[]{2, 3, 4}, new Integer[]{1, 3, 1}, new Integer[]{4, 4, 5}));
        assertEquals(3, ds.size());
        assertEquals(10, ds.stream().mapToInt(x -> x[2]).sum());
        assertEquals(2, NumbersInPi.numbersInPi("3141592653589793238462643383279", new String[]{"314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"}));
        assertEquals(-1, NumbersInPi.numbersInPi("31", new String[]{"3"}));
        assertEquals(18, MaximumSumSubmatrix.maximumSumSubmatrix(new int[][]{{5, 3, -1, 5}, {-7, 3, 7, 4}, {12, 8, 0, 0}, {1, -8, -8, 2}}, 2));
        assertEquals(-1, MaximumSumSubmatrix.maximumSumSubmatrix(new int[][]{{-1, -2}}, 1));
        assertEquals(4, MaximizeExpression.maximizeExpression(new int[]{3, 6, 1, -3, 2, 7}));
        assertEquals(0, MaximizeExpression.maximizeExpression(new int[]{1, 2, 3}));
        assertEquals(6, DiceThrows.diceThrows(2, 6, 7));
        assertEquals(0, DiceThrows.diceThrows(1, 2, 3));
        var jb = JuiceBottling.juiceBottling(new int[]{0, 1, 3, 2});
        assertEquals(3, jb.stream().mapToInt(Integer::intValue).sum());
        assertEquals(4, jb.stream().mapToInt(s -> new int[]{0, 1, 3, 2}[s]).sum());
    }

    @Test void famous() {
        int[][][] g = {{{1, 7}}, {{2, 6}, {3, 20}, {4, 3}}, {{3, 14}}, {{4, 2}}, {}, {}};
        assertArrayEquals(new int[]{0, 7, 13, 27, 10, -1}, DijkstrasAlgorithm.dijkstrasAlgorithm(0, g));
        var order = TopologicalSort.topologicalSort(List.of(1, 2, 3, 4), List.of(new Integer[]{1, 2}, new Integer[]{1, 3}, new Integer[]{3, 2}, new Integer[]{4, 2}, new Integer[]{4, 3}));
        assertTrue(order.indexOf(1) < order.indexOf(3) && order.indexOf(3) < order.indexOf(2) && order.indexOf(4) < order.indexOf(3));
        assertTrue(TopologicalSort.topologicalSort(List.of(1, 2), List.of(new Integer[]{1, 2}, new Integer[]{2, 1})).isEmpty());
        int[][][] u = {{{1, 3}, {2, 5}}, {{0, 3}, {2, 10}, {3, 12}}, {{0, 5}, {1, 10}}, {{1, 12}}};
        assertEquals(20, weight(KruskalsAlgorithm.kruskalsAlgorithm(u)));
        assertEquals(20, weight(PrimsAlgorithm.primsAlgorithm(u)));
    }

    private static int weight(int[][][] g) {
        int s = 0;
        for (int[][] adj : g) for (int[] e : adj) s += e[1];
        return s / 2;
    }

    @Test void graphs() {
        char[][] b = {{'t', 'h', 'i', 's'}, {'w', 'a', 't', 's'}, {'o', 'a', 'n', 'z'}};
        var w = BoggleBoard.boggleBoard(b, new String[]{"this", "is", "not", "that", "a", "zzz"});
        assertTrue(w.containsAll(List.of("this", "is", "that", "a")));
        assertFalse(w.contains("not"));
        assertEquals(5, LargestIsland.largestIsland(new int[][]{{0, 1, 1}, {0, 0, 1}, {1, 1, 0}}));
        assertEquals(1, LargestIsland.largestIsland(new int[][]{{1}}));
    }

    @Test void heaps() {
        var h = new ContinuousMedian.ContinuousMedianHandler();
        h.insert(5); h.insert(10);
        assertEquals(7.5, h.getMedian());
        h.insert(100);
        assertEquals(10, h.getMedian());
        assertArrayEquals(new int[]{1, 2, 3, 3, 4, 5, 6, 8}, SortKSortedArray.sortKSortedArray(new int[]{3, 2, 1, 5, 4, 3, 6, 8}, 3));
        assertArrayEquals(new int[]{}, SortKSortedArray.sortKSortedArray(new int[]{}, 2));
        assertEquals(3, LaptopRentals.laptopRentals(new int[][]{{0, 2}, {1, 4}, {4, 6}, {0, 4}, {7, 8}, {9, 11}, {3, 10}}));
        assertEquals(1, LaptopRentals.laptopRentals(new int[][]{{0, 1}, {1, 2}}));
    }

    @Test void linkedLists() {
        var l = LinkedListNode.of(0, 1, 2, 3, 4, 5, 6);
        LinkedListNode n4 = l.next.next.next.next, end = n4.next.next;
        end.next = n4;
        assertSame(n4, FindLoop.findLoop(l));
        assertEquals(List.of(3, 2, 1), LinkedListNode.toList(ReverseLinkedList.reverseLinkedList(LinkedListNode.of(1, 2, 3))));
        assertNull(ReverseLinkedList.reverseLinkedList(null));
        assertEquals(List.of(1, 2, 3, 4, 5, 6), LinkedListNode.toList(MergeLinkedLists.mergeLinkedLists(LinkedListNode.of(2, 6), LinkedListNode.of(1, 3, 4, 5))));
        assertEquals(List.of(4, 5, 0, 1, 2, 3), LinkedListNode.toList(ShiftLinkedList.shiftLinkedList(LinkedListNode.of(0, 1, 2, 3, 4, 5), 2)));
        assertEquals(List.of(2, 3, 4, 5, 0, 1), LinkedListNode.toList(ShiftLinkedList.shiftLinkedList(LinkedListNode.of(0, 1, 2, 3, 4, 5), -2)));
    }

    @Test void recursion() {
        var A = new LowestCommonManager.OrgChart('A'); var B = new LowestCommonManager.OrgChart('B');
        var C = new LowestCommonManager.OrgChart('C'); var D = new LowestCommonManager.OrgChart('D');
        var E = new LowestCommonManager.OrgChart('E');
        A.add(B, C); B.add(D, E);
        assertEquals('B', LowestCommonManager.getLowestCommonManager(A, D, E).name);
        assertEquals('A', LowestCommonManager.getLowestCommonManager(A, E, C).name);
        assertTrue(InterweavingStrings.interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjob"));
        assertFalse(InterweavingStrings.interweavingStrings("a", "b", "ba1"));
        int[][] board = {
                {7, 8, 0, 4, 0, 0, 1, 2, 0}, {6, 0, 0, 0, 7, 5, 0, 0, 9}, {0, 0, 0, 6, 0, 1, 0, 7, 8},
                {0, 0, 7, 0, 4, 0, 2, 6, 0}, {0, 0, 1, 0, 5, 0, 9, 3, 0}, {9, 0, 4, 0, 6, 0, 0, 0, 5},
                {0, 7, 0, 3, 0, 0, 0, 1, 2}, {1, 2, 0, 0, 0, 7, 4, 0, 0}, {0, 4, 9, 2, 0, 6, 0, 0, 7}};
        SolveSudoku.solveSudoku(board);
        for (int[] row : board) assertEquals(45, java.util.Arrays.stream(row).sum());
        assertArrayEquals(new int[]{7, 8, 5, 4, 3, 9, 1, 2, 6}, board[0]);
        assertEquals(List.of("<div><div></div></div>", "<div></div><div></div>"), GenerateDivTags.generateDivTags(2));
        assertEquals(5, GenerateDivTags.generateDivTags(3).size());
        assertTrue(AmbiguousMeasurements.ambiguousMeasurements(new int[][]{{200, 210}, {450, 465}, {800, 850}}, 2100, 2300));
        assertFalse(AmbiguousMeasurements.ambiguousMeasurements(new int[][]{{10, 20}}, 1, 5));
    }

    @Test void searching() {
        assertEquals(8, ShiftedBinarySearch.shiftedBinarySearch(new int[]{45, 61, 71, 72, 73, 0, 1, 21, 33, 37}, 33));
        assertEquals(-1, ShiftedBinarySearch.shiftedBinarySearch(new int[]{5, 1, 3}, 4));
        assertArrayEquals(new int[]{4, 9}, SearchForRange.searchForRange(new int[]{0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73}, 45));
        assertArrayEquals(new int[]{-1, -1}, SearchForRange.searchForRange(new int[]{1, 3}, 2));
        assertEquals(5, Quickselect.quickselect(new int[]{8, 5, 2, 9, 7, 6, 3}, 3));
        assertEquals(9, Quickselect.quickselect(new int[]{8, 5, 2, 9, 7, 6, 3}, 7));
        assertEquals(3, IndexEqualsValue.indexEqualsValue(new int[]{-5, -3, 0, 3, 4, 5, 9}));
        assertEquals(-1, IndexEqualsValue.indexEqualsValue(new int[]{1, 2}));
    }

    @Test void sorting() {
        int[] want = {2, 3, 5, 5, 6, 8, 9};
        assertArrayEquals(want, QuickSort.quickSort(new int[]{8, 5, 2, 9, 5, 6, 3}));
        assertArrayEquals(want, HeapSort.heapSort(new int[]{8, 5, 2, 9, 5, 6, 3}));
        assertEquals(List.of(2, 24, 45, 66, 75, 90, 170, 802), RadixSort.radixSort(new ArrayList<>(List.of(170, 45, 75, 90, 802, 24, 2, 66))));
        assertEquals(List.of(), RadixSort.radixSort(new ArrayList<>()));
    }

    @Test void stacksStrings() {
        assertEquals("/foo/bar/baz", ShortenPath.shortenPath("/foo/../test/../test/../foo//bar/./baz"));
        assertEquals("../../a", ShortenPath.shortenPath("../../a/b/.."));
        assertEquals("/", ShortenPath.shortenPath("/../.."));
        assertEquals(9, LargestRectangleUnderSkyline.largestRectangleUnderSkyline(new int[]{1, 3, 3, 2, 4, 1, 5, 3, 2}));
        assertEquals(0, LargestRectangleUnderSkyline.largestRectangleUnderSkyline(new int[]{}));
        assertEquals("mentisac", LongestSubstringWithoutDuplication.longestSubstringWithoutDuplication("clementisacap"));
        assertEquals("a", LongestSubstringWithoutDuplication.longestSubstringWithoutDuplication("aaa"));
        assertEquals("_test_this is a _testtest_ to see if _testestest_ it works",
                UnderscorifySubstring.underscorifySubstring("testthis is a testtest to see if testestest it works", "test"));
        assertEquals("abc", UnderscorifySubstring.underscorifySubstring("abc", "z"));
        assertArrayEquals(new String[]{"go", "powerranger"}, PatternMatcher.patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"));
        assertArrayEquals(new String[]{"a", ""}, PatternMatcher.patternMatcher("xxx", "aaa"));
        assertArrayEquals(new String[]{}, PatternMatcher.patternMatcher("xy", "a"));
        assertEquals(List.of(true, false, true, true, false, true, false),
                MultiStringSearch.multiStringSearch("this is a big string", new String[]{"this", "yo", "is", "a", "bigger", "string", "kappa"}));
    }
}
