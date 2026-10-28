package hard;

import common.BST;
import common.BinaryTree;
import common.LinkedListNode;
import hard.arrays.*;
import hard.binarysearchtrees.*;
import hard.binarytrees.*;
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
import hard.tries.*;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/** One test per Hard problem, each covering the sample plus edge cases. */
class HardProblemsTest {
    // ---------- Arrays ----------
    @Test void fourNumberSum() {
        var q = FourNumberSum.fourNumberSum(new int[]{7, 6, 4, -1, 1, 2}, 16);
        assertEquals(2, q.size());
        for (Integer[] x : q) assertEquals(16, x[0] + x[1] + x[2] + x[3]);
        assertTrue(FourNumberSum.fourNumberSum(new int[]{1, 2, 3, 4}, 100).isEmpty());
        assertTrue(FourNumberSum.fourNumberSum(new int[]{}, 0).isEmpty());
        assertEquals(1, FourNumberSum.fourNumberSum(new int[]{-1, -2, -3, -4}, -10).size());
    }

    @Test void subarraySort() {
        assertArrayEquals(new int[]{3, 9}, SubarraySort.subarraySort(new int[]{1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19}));
        assertArrayEquals(new int[]{-1, -1}, SubarraySort.subarraySort(new int[]{1, 2}));
        assertArrayEquals(new int[]{-1, -1}, SubarraySort.subarraySort(new int[]{1}));
        assertArrayEquals(new int[]{0, 1}, SubarraySort.subarraySort(new int[]{2, 1}));
        assertArrayEquals(new int[]{-1, -1}, SubarraySort.subarraySort(new int[]{1, 1, 1}));
    }

    @Test void largestRange() {
        assertArrayEquals(new int[]{0, 7}, LargestRange.largestRange(new int[]{1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6}));
        assertArrayEquals(new int[]{4, 4}, LargestRange.largestRange(new int[]{4}));
        assertArrayEquals(new int[]{-2, 1}, LargestRange.largestRange(new int[]{1, -1, 0, -2, 0}));
    }

    @Test void minRewards() {
        assertEquals(25, MinRewards.minRewards(new int[]{8, 4, 2, 1, 3, 6, 7, 9, 5}));
        assertEquals(1, MinRewards.minRewards(new int[]{5}));
        assertEquals(6, MinRewards.minRewards(new int[]{1, 2, 3}));
        assertEquals(6, MinRewards.minRewards(new int[]{3, 2, 1}));
    }

    @Test void zigzagTraverse() {
        var zz = List.of(List.of(1, 3, 4, 10), List.of(2, 5, 9, 11), List.of(6, 8, 12, 15), List.of(7, 13, 14, 16));
        assertEquals(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), ZigzagTraverse.zigzagTraverse(zz));
        assertEquals(List.of(1, 2, 3), ZigzagTraverse.zigzagTraverse(List.of(List.of(1), List.of(2), List.of(3))));
        assertEquals(List.of(1, 2, 3), ZigzagTraverse.zigzagTraverse(List.of(List.of(1, 2, 3))));
        assertEquals(List.of(1), ZigzagTraverse.zigzagTraverse(List.of(List.of(1))));
    }

    @Test void longestSubarrayWithSum() {
        int[] ls = LongestSubarrayWithSum.longestSubarrayWithSum(new int[]{1, 2, 15, 3, 4, 5, 6, 7, 8}, 25);
        assertEquals(4, ls[1] - ls[0]);
        assertArrayEquals(new int[]{0, 1}, LongestSubarrayWithSum.longestSubarrayWithSum(new int[]{1, 2, 3, 0}, 3));
        assertEquals(0, LongestSubarrayWithSum.longestSubarrayWithSum(new int[]{5}, 3).length);
        assertEquals(0, LongestSubarrayWithSum.longestSubarrayWithSum(new int[]{}, 0).length);
        assertArrayEquals(new int[]{0, 2}, LongestSubarrayWithSum.longestSubarrayWithSum(new int[]{0, 0, 0}, 0), "zeros extend the window");
    }

    @Test void knightConnection() {
        assertEquals(1, KnightConnection.knightConnection(new int[]{0, 0}, new int[]{2, 1}));
        assertEquals(0, KnightConnection.knightConnection(new int[]{15, -12}, new int[]{15, -12}));
        assertEquals(1, KnightConnection.knightConnection(new int[]{0, 0}, new int[]{4, 2}), "each meets halfway in one turn");
        assertEquals(2, KnightConnection.knightConnection(new int[]{0, 0}, new int[]{1, 0}));
    }

    @Test void countSquares() {
        assertEquals(1, CountSquares.countSquares(new int[][]{{0, 0}, {0, 1}, {1, 1}, {1, 0}}));
        assertEquals(1, CountSquares.countSquares(new int[][]{{0, 1}, {1, 0}, {2, 1}, {1, 2}, {5, 5}}), "rotated square");
        assertEquals(0, CountSquares.countSquares(new int[][]{}));
        assertEquals(2, CountSquares.countSquares(new int[][]{{0, 0}, {0, 1}, {1, 1}, {1, 0}, {2, 0}, {2, 1}}));
    }

    // ---------- BST ----------
    @Test void sameBsts() {
        assertTrue(SameBsts.sameBsts(List.of(10, 15, 8, 12, 94, 81, 5, 2, 11), List.of(10, 8, 5, 15, 2, 12, 11, 94, 81)));
        assertFalse(SameBsts.sameBsts(List.of(1, 2), List.of(2, 1)));
        assertTrue(SameBsts.sameBsts(List.of(), List.of()));
        assertFalse(SameBsts.sameBsts(List.of(1), List.of()));
        assertTrue(SameBsts.sameBsts(List.of(5, 5, 5), List.of(5, 5, 5)));
        assertFalse(SameBsts.sameBsts(List.of(1, 2, 3), List.of(1, 3, 2)));
    }

    @Test void validateThreeNodes() {
        BST t = BST.of(5, 2, 7, 1, 4, 6, 8, 0, 3);
        BST n2 = t.left, n4 = t.left.right, n3 = t.left.right.left;
        assertTrue(ValidateThreeNodes.validateThreeNodes(t, n2, n3));
        assertTrue(ValidateThreeNodes.validateThreeNodes(n3, n2, t), "order can be reversed");
        assertFalse(ValidateThreeNodes.validateThreeNodes(n2, n3, n4));
        assertFalse(ValidateThreeNodes.validateThreeNodes(t.right, t, n2), "siblings don't qualify");
    }

    @Test void repairBst() {
        BST bad = BST.of(10, 7, 20, 3, 12, 8, 22, 2, 14);
        int tmp = bad.left.value; bad.left.value = bad.right.left.value; bad.right.left.value = tmp;
        RepairBst.repairBst(bad);
        assertEquals(List.of(2, 3, 7, 8, 10, 12, 14, 20, 22), BST.inOrder(bad));
        BST adj = BST.of(2, 1, 3);
        adj.value = 1; adj.left.value = 2;
        RepairBst.repairBst(adj);
        assertEquals(List.of(1, 2, 3), BST.inOrder(adj), "adjacent swapped nodes");
    }

    @Test void sumBsts() {
        BinaryTree sample = new BinaryTree(8, new BinaryTree(2, new BinaryTree(1), new BinaryTree(10)), new BinaryTree(9, null, new BinaryTree(5)));
        assertEquals(13, SumBsts.sumBsts(sample));
        assertEquals(6, SumBsts.sumBsts(BinaryTree.fromLevelOrder(2, 1, 3)));
        assertEquals(0, SumBsts.sumBsts(BinaryTree.fromLevelOrder(2, 3, 1)));
        assertEquals(0, SumBsts.sumBsts(BinaryTree.fromLevelOrder(2, 1)), "fewer than 3 nodes");
        assertEquals(1 + 2 + 3 + 4 + 5 + 6 + 7, SumBsts.sumBsts(BinaryTree.fromLevelOrder(4, 2, 6, 1, 3, 5, 7)), "whole tree counted once");
    }

    // ---------- Binary trees ----------
    @Test void maxPathSumInBinaryTree() {
        assertEquals(18, MaxPathSumInBinaryTree.maxPathSum(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7)));
        assertEquals(-2, MaxPathSumInBinaryTree.maxPathSum(new BinaryTree(-2)));
        assertEquals(5, MaxPathSumInBinaryTree.maxPathSum(BinaryTree.fromLevelOrder(-10, 5, -20)));
    }

    @Test void findNodesDistanceK() {
        var d = FindNodesDistanceK.findNodesDistanceK(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, null, 6, null, null, null, null, 7, 8), 3, 2);
        d.sort(null);
        assertEquals(List.of(2, 7, 8), d);
        assertTrue(FindNodesDistanceK.findNodesDistanceK(new BinaryTree(1), 1, 3).isEmpty());
        assertEquals(List.of(1), FindNodesDistanceK.findNodesDistanceK(new BinaryTree(1), 1, 0));
    }

    // ---------- Dynamic programming ----------
    @Test void maxSumIncreasingSubsequence() {
        assertEquals(List.of(List.of(110), List.of(10, 20, 30, 50)), MaxSumIncreasingSubsequence.maxSumIncreasingSubsequence(new int[]{10, 70, 20, 30, 50, 11, 30}));
        assertEquals(List.of(List.of(-1), List.of(-1)), MaxSumIncreasingSubsequence.maxSumIncreasingSubsequence(new int[]{-5, -1, -3}));
        assertEquals(List.of(List.of(8), List.of(8)), MaxSumIncreasingSubsequence.maxSumIncreasingSubsequence(new int[]{8}));
        assertEquals(List.of(List.of(5), List.of(5)), MaxSumIncreasingSubsequence.maxSumIncreasingSubsequence(new int[]{5, 5}), "strictly increasing");
    }

    @Test void longestCommonSubsequence() {
        assertEquals(List.of('X', 'Y', 'Z', 'W'), LongestCommonSubsequence.longestCommonSubsequence("ZXVVYZW", "XKYKZPW"));
        assertEquals(List.of(), LongestCommonSubsequence.longestCommonSubsequence("abc", "xyz"));
        assertEquals(List.of(), LongestCommonSubsequence.longestCommonSubsequence("", "abc"));
        assertEquals(List.of('a', 'a'), LongestCommonSubsequence.longestCommonSubsequence("aa", "aaa"));
    }

    @Test void minNumberOfJumps() {
        assertEquals(4, MinNumberOfJumps.minNumberOfJumps(new int[]{3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3}));
        assertEquals(0, MinNumberOfJumps.minNumberOfJumps(new int[]{1}));
        assertEquals(1, MinNumberOfJumps.minNumberOfJumps(new int[]{5, 1, 1}));
    }

    @Test void waterArea() {
        assertEquals(48, WaterArea.waterArea(new int[]{0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3}));
        assertEquals(0, WaterArea.waterArea(new int[]{}));
        assertEquals(0, WaterArea.waterArea(new int[]{1, 2, 3}));
        assertEquals(2, WaterArea.waterArea(new int[]{2, 0, 2}));
    }

    @Test void knapsackProblem() {
        assertEquals(List.of(List.of(10), List.of(1, 3)), KnapsackProblem.knapsackProblem(new int[][]{{1, 2}, {4, 3}, {5, 6}, {6, 7}}, 10));
        assertEquals(List.of(List.of(0), List.of()), KnapsackProblem.knapsackProblem(new int[][]{{5, 20}}, 10));
        assertEquals(List.of(List.of(0), List.of()), KnapsackProblem.knapsackProblem(new int[][]{}, 10));
        assertEquals(List.of(List.of(7), List.of(0)), KnapsackProblem.knapsackProblem(new int[][]{{7, 10}}, 10), "exact fit");
    }

    @Test void diskStacking() {
        var ds = DiskStacking.diskStacking(List.of(new Integer[]{2, 1, 2}, new Integer[]{3, 2, 3}, new Integer[]{2, 2, 8}, new Integer[]{2, 3, 4}, new Integer[]{1, 3, 1}, new Integer[]{4, 4, 5}));
        assertEquals(3, ds.size());
        assertEquals(10, ds.stream().mapToInt(x -> x[2]).sum());
        assertEquals(1, DiskStacking.diskStacking(List.of(new Integer[]{1, 1, 1}, new Integer[]{1, 1, 1})).size(), "equal disks can't stack");
        assertEquals(1, DiskStacking.diskStacking(List.<Integer[]>of(new Integer[]{3, 3, 3})).size());
    }

    @Test void numbersInPi() {
        assertEquals(2, NumbersInPi.numbersInPi("3141592653589793238462643383279", new String[]{"314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"}));
        assertEquals(-1, NumbersInPi.numbersInPi("31", new String[]{"3"}));
        assertEquals(0, NumbersInPi.numbersInPi("314", new String[]{"314"}));
    }

    @Test void maximumSumSubmatrix() {
        assertEquals(18, MaximumSumSubmatrix.maximumSumSubmatrix(new int[][]{{5, 3, -1, 5}, {-7, 3, 7, 4}, {12, 8, 0, 0}, {1, -8, -8, 2}}, 2));
        assertEquals(-1, MaximumSumSubmatrix.maximumSumSubmatrix(new int[][]{{-1, -2}}, 1));
        assertEquals(10, MaximumSumSubmatrix.maximumSumSubmatrix(new int[][]{{1, 2}, {3, 4}}, 2));
    }

    @Test void maximizeExpression() {
        assertEquals(4, MaximizeExpression.maximizeExpression(new int[]{3, 6, 1, -3, 2, 7}));
        assertEquals(0, MaximizeExpression.maximizeExpression(new int[]{1, 2, 3}));
        assertEquals(0, MaximizeExpression.maximizeExpression(new int[]{}));
        assertEquals(0, MaximizeExpression.maximizeExpression(new int[]{5, 5, 5, 5}));
    }

    @Test void diceThrows() {
        assertEquals(6, DiceThrows.diceThrows(2, 6, 7));
        assertEquals(0, DiceThrows.diceThrows(1, 2, 3));
        assertEquals(1, DiceThrows.diceThrows(3, 6, 18));
        assertEquals(1, DiceThrows.diceThrows(1, 4, 4));
    }

    @Test void juiceBottling() {
        int[] prices = {0, 1, 3, 2};
        var jb = JuiceBottling.juiceBottling(prices);
        assertEquals(3, jb.stream().mapToInt(Integer::intValue).sum());
        assertEquals(4, jb.stream().mapToInt(s -> prices[s]).sum());
        assertEquals(List.of(), JuiceBottling.juiceBottling(new int[]{0}));
        assertEquals(List.of(1, 1), JuiceBottling.juiceBottling(new int[]{0, 5, 6}));
    }

    // ---------- Famous algorithms ----------
    @Test void dijkstrasAlgorithm() {
        int[][][] g = {{{1, 7}}, {{2, 6}, {3, 20}, {4, 3}}, {{3, 14}}, {{4, 2}}, {}, {}};
        assertArrayEquals(new int[]{0, 7, 13, 27, 10, -1}, DijkstrasAlgorithm.dijkstrasAlgorithm(0, g));
        assertArrayEquals(new int[]{0}, DijkstrasAlgorithm.dijkstrasAlgorithm(0, new int[][][]{{}}));
        assertArrayEquals(new int[]{0, 1}, DijkstrasAlgorithm.dijkstrasAlgorithm(0, new int[][][]{{{1, 5}, {1, 1}}, {}}), "parallel edges");
    }

    @Test void topologicalSort() {
        var order = TopologicalSort.topologicalSort(List.of(1, 2, 3, 4), List.of(new Integer[]{1, 2}, new Integer[]{1, 3}, new Integer[]{3, 2}, new Integer[]{4, 2}, new Integer[]{4, 3}));
        assertTrue(order.indexOf(1) < order.indexOf(3) && order.indexOf(3) < order.indexOf(2) && order.indexOf(4) < order.indexOf(3));
        assertTrue(TopologicalSort.topologicalSort(List.of(1, 2), List.of(new Integer[]{1, 2}, new Integer[]{2, 1})).isEmpty());
        assertEquals(List.of(1), TopologicalSort.topologicalSort(List.of(1), List.of()));
    }

    private static int weight(int[][][] g) {
        int s = 0;
        for (int[][] adj : g) for (int[] e : adj) s += e[1];
        return s / 2;
    }

    @Test void kruskalsAlgorithm() {
        int[][][] u = {{{1, 3}, {2, 5}}, {{0, 3}, {2, 10}, {3, 12}}, {{0, 5}, {1, 10}}, {{1, 12}}};
        assertEquals(20, weight(KruskalsAlgorithm.kruskalsAlgorithm(u)));
        assertEquals(0, weight(KruskalsAlgorithm.kruskalsAlgorithm(new int[][][]{{}})));
        assertEquals(2, weight(KruskalsAlgorithm.kruskalsAlgorithm(new int[][][]{{{1, 1}}, {{0, 1}}, {{3, 1}}, {{2, 1}}})), "forest");
    }

    @Test void primsAlgorithm() {
        int[][][] u = {{{1, 3}, {2, 5}}, {{0, 3}, {2, 10}, {3, 12}}, {{0, 5}, {1, 10}}, {{1, 12}}};
        assertEquals(20, weight(PrimsAlgorithm.primsAlgorithm(u)));
        assertEquals(0, weight(PrimsAlgorithm.primsAlgorithm(new int[][][]{{}})));
        assertEquals(-3, weight(PrimsAlgorithm.primsAlgorithm(new int[][][]{{{1, -3}, {1, 4}}, {{0, -3}, {0, 4}}})), "negative weights ok");
    }

    // ---------- Graphs ----------
    @Test void boggleBoard() {
        char[][] b = {{'t', 'h', 'i', 's'}, {'w', 'a', 't', 's'}, {'o', 'a', 'n', 'z'}};
        var w = BoggleBoard.boggleBoard(b, new String[]{"this", "is", "not", "that", "a", "zzz"});
        assertTrue(w.containsAll(List.of("this", "is", "that", "a")));
        assertFalse(w.contains("not"));
        assertFalse(w.contains("zzz"), "cells can't be reused");
        assertEquals(List.of(), BoggleBoard.boggleBoard(new char[][]{{'a'}}, new String[]{}));
    }

    @Test void largestIsland() {
        assertEquals(5, LargestIsland.largestIsland(new int[][]{{0, 1, 1}, {0, 0, 1}, {1, 1, 0}}));
        assertEquals(1, LargestIsland.largestIsland(new int[][]{{1}}));
        assertEquals(4, LargestIsland.largestIsland(new int[][]{{0, 0}, {0, 0}}), "all land");
    }

    // ---------- Heaps ----------
    @Test void continuousMedian() {
        var h = new ContinuousMedian.ContinuousMedianHandler();
        h.insert(5);
        assertEquals(5, h.getMedian());
        h.insert(10);
        assertEquals(7.5, h.getMedian());
        h.insert(100);
        assertEquals(10, h.getMedian());
        h.insert(-3); h.insert(-3);
        assertEquals(5, h.getMedian());
    }

    @Test void sortKSortedArray() {
        assertArrayEquals(new int[]{1, 2, 3, 3, 4, 5, 6, 8}, SortKSortedArray.sortKSortedArray(new int[]{3, 2, 1, 5, 4, 3, 6, 8}, 3));
        assertArrayEquals(new int[]{}, SortKSortedArray.sortKSortedArray(new int[]{}, 2));
        assertArrayEquals(new int[]{1, 2}, SortKSortedArray.sortKSortedArray(new int[]{1, 2}, 0));
        assertArrayEquals(new int[]{-2, -1}, SortKSortedArray.sortKSortedArray(new int[]{-1, -2}, 5), "k larger than n");
    }

    @Test void laptopRentals() {
        assertEquals(3, LaptopRentals.laptopRentals(new int[][]{{0, 2}, {1, 4}, {4, 6}, {0, 4}, {7, 8}, {9, 11}, {3, 10}}));
        assertEquals(1, LaptopRentals.laptopRentals(new int[][]{{0, 1}, {1, 2}}), "back-to-back reuse");
        assertEquals(0, LaptopRentals.laptopRentals(new int[][]{}));
        assertEquals(2, LaptopRentals.laptopRentals(new int[][]{{0, 5}, {0, 5}}));
    }

    // ---------- Linked lists ----------
    @Test void findLoop() {
        var l = LinkedListNode.of(0, 1, 2, 3, 4, 5, 6);
        LinkedListNode n4 = l.next.next.next.next, end = n4.next.next;
        end.next = n4;
        assertSame(n4, FindLoop.findLoop(l));
        var whole = LinkedListNode.of(1, 2);
        whole.next.next = whole;
        assertSame(whole, FindLoop.findLoop(whole));
    }

    @Test void reverseLinkedList() {
        assertEquals(List.of(3, 2, 1), LinkedListNode.toList(ReverseLinkedList.reverseLinkedList(LinkedListNode.of(1, 2, 3))));
        assertNull(ReverseLinkedList.reverseLinkedList(null));
        assertEquals(List.of(1), LinkedListNode.toList(ReverseLinkedList.reverseLinkedList(LinkedListNode.of(1))));
    }

    @Test void mergeLinkedLists() {
        assertEquals(List.of(1, 2, 3, 4, 5, 6), LinkedListNode.toList(MergeLinkedLists.mergeLinkedLists(LinkedListNode.of(2, 6), LinkedListNode.of(1, 3, 4, 5))));
        assertEquals(List.of(1, 1), LinkedListNode.toList(MergeLinkedLists.mergeLinkedLists(LinkedListNode.of(1), LinkedListNode.of(1))));
        assertEquals(List.of(-1, 0), LinkedListNode.toList(MergeLinkedLists.mergeLinkedLists(LinkedListNode.of(-1, 0), null)));
    }

    @Test void shiftLinkedList() {
        assertEquals(List.of(4, 5, 0, 1, 2, 3), LinkedListNode.toList(ShiftLinkedList.shiftLinkedList(LinkedListNode.of(0, 1, 2, 3, 4, 5), 2)));
        assertEquals(List.of(2, 3, 4, 5, 0, 1), LinkedListNode.toList(ShiftLinkedList.shiftLinkedList(LinkedListNode.of(0, 1, 2, 3, 4, 5), -2)));
        assertEquals(List.of(0, 1, 2), LinkedListNode.toList(ShiftLinkedList.shiftLinkedList(LinkedListNode.of(0, 1, 2), 3)));
        assertEquals(List.of(7), LinkedListNode.toList(ShiftLinkedList.shiftLinkedList(LinkedListNode.of(7), 5)));
    }

    // ---------- Recursion ----------
    @Test void lowestCommonManager() {
        var A = new LowestCommonManager.OrgChart('A'); var B = new LowestCommonManager.OrgChart('B');
        var C = new LowestCommonManager.OrgChart('C'); var D = new LowestCommonManager.OrgChart('D');
        var E = new LowestCommonManager.OrgChart('E');
        A.add(B, C); B.add(D, E);
        assertEquals('B', LowestCommonManager.getLowestCommonManager(A, D, E).name);
        assertEquals('A', LowestCommonManager.getLowestCommonManager(A, E, C).name);
        assertEquals('B', LowestCommonManager.getLowestCommonManager(A, B, D).name, "a manager can be one of the reports");
    }

    @Test void interweavingStrings() {
        assertTrue(InterweavingStrings.interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjob"));
        assertFalse(InterweavingStrings.interweavingStrings("a", "b", "ba1"));
        assertTrue(InterweavingStrings.interweavingStrings("", "", ""));
        assertTrue(InterweavingStrings.interweavingStrings("aa", "a", "aaa"));
        assertFalse(InterweavingStrings.interweavingStrings("ab", "c", "bac"), "order within a string must hold");
    }

    @Test void solveSudoku() {
        int[][] board = {
                {7, 8, 0, 4, 0, 0, 1, 2, 0}, {6, 0, 0, 0, 7, 5, 0, 0, 9}, {0, 0, 0, 6, 0, 1, 0, 7, 8},
                {0, 0, 7, 0, 4, 0, 2, 6, 0}, {0, 0, 1, 0, 5, 0, 9, 3, 0}, {9, 0, 4, 0, 6, 0, 0, 0, 5},
                {0, 7, 0, 3, 0, 0, 0, 1, 2}, {1, 2, 0, 0, 0, 7, 4, 0, 0}, {0, 4, 9, 2, 0, 6, 0, 0, 7}};
        SolveSudoku.solveSudoku(board);
        for (int[] row : board) assertEquals(45, Arrays.stream(row).sum());
        assertArrayEquals(new int[]{7, 8, 5, 4, 3, 9, 1, 2, 6}, board[0]);
        int[][] empty = new int[9][9];
        SolveSudoku.solveSudoku(empty);
        for (int c = 0; c < 9; c++) { int s = 0; for (int r = 0; r < 9; r++) s += empty[r][c]; assertEquals(45, s); }
    }

    @Test void generateDivTags() {
        assertEquals(List.of("<div><div></div></div>", "<div></div><div></div>"), GenerateDivTags.generateDivTags(2));
        assertEquals(5, GenerateDivTags.generateDivTags(3).size());
        assertEquals(List.of("<div></div>"), GenerateDivTags.generateDivTags(1));
    }

    @Test void ambiguousMeasurements() {
        assertTrue(AmbiguousMeasurements.ambiguousMeasurements(new int[][]{{200, 210}, {450, 465}, {800, 850}}, 2100, 2300));
        assertFalse(AmbiguousMeasurements.ambiguousMeasurements(new int[][]{{200, 210}}, 10, 20));
        assertFalse(AmbiguousMeasurements.ambiguousMeasurements(new int[][]{{10, 20}}, 1, 5));
        assertTrue(AmbiguousMeasurements.ambiguousMeasurements(new int[][]{{5, 5}}, 15, 15), "exact cups chain");
        assertFalse(AmbiguousMeasurements.ambiguousMeasurements(new int[][]{{0, 0}}, 1, 1), "empty cup can't progress");
    }

    // ---------- Searching ----------
    @Test void shiftedBinarySearch() {
        assertEquals(8, ShiftedBinarySearch.shiftedBinarySearch(new int[]{45, 61, 71, 72, 73, 0, 1, 21, 33, 37}, 33));
        assertEquals(-1, ShiftedBinarySearch.shiftedBinarySearch(new int[]{5, 1, 3}, 4));
        assertEquals(-1, ShiftedBinarySearch.shiftedBinarySearch(new int[]{}, 4));
        assertEquals(0, ShiftedBinarySearch.shiftedBinarySearch(new int[]{-1}, -1));
    }

    @Test void searchForRange() {
        assertArrayEquals(new int[]{4, 9}, SearchForRange.searchForRange(new int[]{0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73}, 45));
        assertArrayEquals(new int[]{-1, -1}, SearchForRange.searchForRange(new int[]{1, 3}, 2));
        assertArrayEquals(new int[]{-1, -1}, SearchForRange.searchForRange(new int[]{}, 2));
        assertArrayEquals(new int[]{0, 2}, SearchForRange.searchForRange(new int[]{7, 7, 7}, 7));
    }

    @Test void quickselect() {
        assertEquals(5, Quickselect.quickselect(new int[]{8, 5, 2, 9, 7, 6, 3}, 3));
        assertEquals(9, Quickselect.quickselect(new int[]{8, 5, 2, 9, 7, 6, 3}, 7));
        assertEquals(4, Quickselect.quickselect(new int[]{4}, 1));
        assertEquals(2, Quickselect.quickselect(new int[]{2, 2, 2, 1}, 3), "duplicates");
    }

    @Test void indexEqualsValue() {
        assertEquals(3, IndexEqualsValue.indexEqualsValue(new int[]{-5, -3, 0, 3, 4, 5, 9}));
        assertEquals(-1, IndexEqualsValue.indexEqualsValue(new int[]{1, 2}));
        assertEquals(-1, IndexEqualsValue.indexEqualsValue(new int[]{}));
        assertEquals(0, IndexEqualsValue.indexEqualsValue(new int[]{0, 1, 2}), "smallest index wins");
    }

    // ---------- Sorting ----------
    private static void checkSort(java.util.function.UnaryOperator<int[]> sorter) {
        assertArrayEquals(new int[]{2, 3, 5, 5, 6, 8, 9}, sorter.apply(new int[]{8, 5, 2, 9, 5, 6, 3}));
        assertArrayEquals(new int[]{}, sorter.apply(new int[]{}));
        assertArrayEquals(new int[]{1}, sorter.apply(new int[]{1}));
        assertArrayEquals(new int[]{-3, -1, 0, 0}, sorter.apply(new int[]{0, -1, 0, -3}));
        assertArrayEquals(new int[]{1, 2, 3, 4}, sorter.apply(new int[]{4, 3, 2, 1}));
    }

    @Test void quickSort() { checkSort(QuickSort::quickSort); }
    @Test void heapSort() { checkSort(HeapSort::heapSort); }

    @Test void radixSort() {
        assertEquals(List.of(2, 24, 45, 66, 75, 90, 170, 802), RadixSort.radixSort(new ArrayList<>(List.of(170, 45, 75, 90, 802, 24, 2, 66))));
        assertEquals(List.of(), RadixSort.radixSort(new ArrayList<>()));
        assertEquals(List.of(0, 0, 1), RadixSort.radixSort(new ArrayList<>(List.of(1, 0, 0))));
    }

    // ---------- Stacks ----------
    @Test void shortenPath() {
        assertEquals("/foo/bar/baz", ShortenPath.shortenPath("/foo/../test/../test/../foo//bar/./baz"));
        assertEquals("../../a", ShortenPath.shortenPath("../../a/b/.."));
        assertEquals("/", ShortenPath.shortenPath("/../.."));
        assertEquals("", ShortenPath.shortenPath("a/.."));
    }

    @Test void largestRectangleUnderSkyline() {
        assertEquals(9, LargestRectangleUnderSkyline.largestRectangleUnderSkyline(new int[]{1, 3, 3, 2, 4, 1, 5, 3, 2}));
        assertEquals(0, LargestRectangleUnderSkyline.largestRectangleUnderSkyline(new int[]{}));
        assertEquals(5, LargestRectangleUnderSkyline.largestRectangleUnderSkyline(new int[]{5}));
        assertEquals(6, LargestRectangleUnderSkyline.largestRectangleUnderSkyline(new int[]{2, 2, 2}));
    }

    // ---------- Strings ----------
    @Test void longestSubstringWithoutDuplication() {
        assertEquals("mentisac", LongestSubstringWithoutDuplication.longestSubstringWithoutDuplication("clementisacap"));
        assertEquals("a", LongestSubstringWithoutDuplication.longestSubstringWithoutDuplication("aaa"));
        assertEquals("", LongestSubstringWithoutDuplication.longestSubstringWithoutDuplication(""));
        assertEquals("abc", LongestSubstringWithoutDuplication.longestSubstringWithoutDuplication("abcabc"));
    }

    @Test void underscorifySubstring() {
        assertEquals("_test_this is a _testtest_ to see if _testestest_ it works",
                UnderscorifySubstring.underscorifySubstring("testthis is a testtest to see if testestest it works", "test"));
        assertEquals("abc", UnderscorifySubstring.underscorifySubstring("abc", "z"));
        assertEquals("_aaa_", UnderscorifySubstring.underscorifySubstring("aaa", "a"));
    }

    @Test void patternMatcher() {
        assertArrayEquals(new String[]{"go", "powerranger"}, PatternMatcher.patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"));
        assertArrayEquals(new String[]{"a", ""}, PatternMatcher.patternMatcher("xxx", "aaa"));
        assertArrayEquals(new String[]{}, PatternMatcher.patternMatcher("xy", "a"));
        assertArrayEquals(new String[]{"b", "a"}, PatternMatcher.patternMatcher("yx", "ab"), "pattern starting with y");
    }

    // ---------- Tries ----------
    @Test void multiStringSearch() {
        assertEquals(List.of(true, false, true, true, false, true, false),
                MultiStringSearch.multiStringSearch("this is a big string", new String[]{"this", "yo", "is", "a", "bigger", "string", "kappa"}));
        assertEquals(List.of(), MultiStringSearch.multiStringSearch("abc", new String[]{}));
        assertEquals(List.of(false), MultiStringSearch.multiStringSearch("", new String[]{"a"}));
    }

    @Test void longestMostFrequentPrefix() {
        assertEquals("algo", LongestMostFrequentPrefix.longestMostFrequentPrefix(new String[]{"algoexpert", "algorithm", "frontendexpert", "mlexpert"}));
        assertEquals("fo", LongestMostFrequentPrefix.longestMostFrequentPrefix(new String[]{"hello", "world", "fossil", "worldly", "food", "forrest", "helium", "algoexpert", "algorithm"}));
        assertEquals("mnop", LongestMostFrequentPrefix.longestMostFrequentPrefix(new String[]{"abc", "def", "ghi", "jkl", "mnop", "qrs", "tuv", "wxy", "z"}));
        assertEquals("solo", LongestMostFrequentPrefix.longestMostFrequentPrefix(new String[]{"solo"}));
    }

    @Test void shortestUniquePrefixes() {
        assertArrayEquals(new String[]{"algoe", "algor", "f", "m"}, ShortestUniquePrefixes.shortestUniquePrefixes(new String[]{"algoexpert", "algorithm", "frontendexpert", "mlexpert"}));
        assertArrayEquals(new String[]{"food", "foodi"}, ShortestUniquePrefixes.shortestUniquePrefixes(new String[]{"food", "foodie"}));
        assertArrayEquals(new String[]{"a"}, ShortestUniquePrefixes.shortestUniquePrefixes(new String[]{"abc"}));
        assertArrayEquals(new String[]{}, ShortestUniquePrefixes.shortestUniquePrefixes(new String[]{}));
    }
}
