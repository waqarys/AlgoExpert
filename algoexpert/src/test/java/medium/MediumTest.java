package medium;

import common.BST;
import common.BinaryTree;
import common.LinkedListNode;
import medium.arrays.*;
import medium.binarysearchtrees.*;
import medium.binarytrees.*;
import medium.dynamicprogramming.*;
import medium.famousalgorithms.*;
import medium.graphs.*;
import medium.greedyalgorithms.*;
import medium.heaps.MinHeapConstruction;
import medium.linkedlists.*;
import medium.recursion.*;
import medium.searching.SearchInSortedMatrix;
import medium.sorting.ThreeNumberSort;
import medium.stacks.*;
import medium.strings.*;
import medium.tries.SuffixTrieConstruction;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class MediumTest {
    @Test void arrays() {
        var t = ThreeNumberSum.threeNumberSum(new int[]{12, 3, 1, 2, -6, 5, -8, 6}, 0);
        assertEquals(3, t.size());
        assertArrayEquals(new Integer[]{-8, 2, 6}, t.get(0));
        assertTrue(ThreeNumberSum.threeNumberSum(new int[]{1, 2, 3}, 100).isEmpty());
        assertArrayEquals(new int[]{28, 26}, SmallestDifference.smallestDifference(new int[]{-1, 5, 10, 20, 28, 3}, new int[]{26, 134, 135, 15, 17}));
        assertArrayEquals(new int[]{10, 10}, SmallestDifference.smallestDifference(new int[]{10, 0}, new int[]{10, 50}));
        var m = MoveElementToEnd.moveElementToEnd(new ArrayList<>(List.of(2, 1, 2, 2, 2, 3, 4, 2)), 2);
        assertEquals(List.of(2, 2, 2, 2, 2), m.subList(3, 8));
        assertTrue(MonotonicArray.isMonotonic(new int[]{-1, -5, -10, -1100, -1100, -1101}));
        assertFalse(MonotonicArray.isMonotonic(new int[]{1, 2, 1}));
        assertEquals(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), SpiralTraverse.spiralTraverse(new int[][]{{1, 2, 3, 4}, {10, 11, 12, 5}, {9, 8, 7, 6}}));
        assertEquals(List.of(1, 2, 3), SpiralTraverse.spiralTraverse(new int[][]{{1}, {2}, {3}}));
        assertEquals(6, LongestPeak.longestPeak(new int[]{1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3}));
        assertEquals(0, LongestPeak.longestPeak(new int[]{1, 2, 3}));
        assertArrayEquals(new int[]{8, 40, 10, 20}, ArrayOfProducts.arrayOfProducts(new int[]{5, 1, 4, 2}));
        assertEquals(2, FirstDuplicateValue.firstDuplicateValue(new int[]{2, 1, 5, 2, 3, 3, 4}));
        assertEquals(-1, FirstDuplicateValue.firstDuplicateValue(new int[]{1, 2, 3}));
        assertArrayEquals(new int[][]{{1, 2}, {3, 8}, {9, 10}}, MergeOverlappingIntervals.mergeOverlappingIntervals(new int[][]{{1, 2}, {3, 5}, {4, 7}, {6, 8}, {9, 10}}));
        assertEquals(4, BestSeat.bestSeat(new int[]{1, 0, 1, 0, 0, 0, 1}));
        assertEquals(-1, BestSeat.bestSeat(new int[]{1, 1}));
        assertTrue(ZeroSumSubarray.zeroSumSubarray(new int[]{-5, -5, 2, 3, -2}));
        assertFalse(ZeroSumSubarray.zeroSumSubarray(new int[]{1, 2, 3}));
        assertArrayEquals(new int[]{2, 5}, MissingNumbers.missingNumbers(new int[]{1, 4, 3}));
        assertArrayEquals(new int[]{1, 2}, MissingNumbers.missingNumbers(new int[]{}));
        assertEquals(2, MajorityElement.majorityElement(new int[]{1, 2, 3, 2, 2, 1, 2}));
        assertArrayEquals(new int[]{-3, 7}, SweetAndSavory.sweetAndSavory(new int[]{-3, -5, 1, 7}, 8));
        assertArrayEquals(new int[]{0, 0}, SweetAndSavory.sweetAndSavory(new int[]{2, 5, -4, -7, 12, 100, -25}, -50));
    }

    @Test void bst() {
        var b = new BstConstruction.BST(10).insert(5).insert(15).insert(2).insert(5).insert(13).insert(22).insert(1).insert(14).insert(12);
        b.remove(10);
        assertFalse(b.contains(10));
        assertEquals(12, b.value);
        assertTrue(b.contains(15));
        var single = new BstConstruction.BST(1).remove(1);
        assertTrue(single.contains(1));
        BST t = BST.of(10, 5, 15, 2, 5, 13, 22, 1, 14);
        assertTrue(ValidateBst.validateBst(t));
        t.left.value = 11;
        assertFalse(ValidateBst.validateBst(t));
        BST u = BST.of(10, 5, 15, 2, 5, 22, 1);
        assertEquals(List.of(1, 2, 5, 5, 10, 15, 22), BstTraversal.inOrderTraverse(u, new ArrayList<>()));
        assertEquals(List.of(10, 5, 2, 1, 5, 15, 22), BstTraversal.preOrderTraverse(u, new ArrayList<>()));
        assertEquals(List.of(1, 2, 5, 5, 22, 15, 10), BstTraversal.postOrderTraverse(u, new ArrayList<>()));
        var mh = MinHeightBst.minHeightBst(List.of(1, 2, 5, 7, 10, 13, 14, 15, 22));
        assertEquals(4, MinHeightBst.height(mh));
        assertTrue(ValidateBst.validateBst(mh));
        assertEquals(17, FindKthLargestValueInBst.findKthLargestValueInBst(BST.of(15, 5, 20, 2, 5, 17, 22, 1, 3), 3));
        assertEquals(1, FindKthLargestValueInBst.findKthLargestValueInBst(BST.of(15, 5, 20, 2, 5, 17, 22, 1, 3), 9));
        var r = ReconstructBst.reconstructBst(List.of(10, 4, 2, 1, 5, 17, 19, 18));
        assertEquals(List.of(10, 4, 2, 1, 5, 17, 19, 18), BstTraversal.preOrderTraverse(r, new ArrayList<>()));
    }

    @Test void binaryTrees() {
        BinaryTree t = BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7);
        InvertBinaryTree.invertBinaryTree(t);
        assertEquals(List.of(7, 3, 6, 1, 5, 2, 4), BinaryTree.inOrder(t));
        assertEquals(6, BinaryTreeDiameter.binaryTreeDiameter(BinaryTree.fromLevelOrder(1, 3, 2, 7, 4, null, null, 8, null, null, 5, 9, null, null, 6)));
        assertEquals(0, BinaryTreeDiameter.binaryTreeDiameter(new BinaryTree(1)));
        BinaryTree s = BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, null, null, 6);
        assertEquals(1, FindSuccessor.findSuccessor(s, s.left.right).value);
        assertEquals(2, FindSuccessor.findSuccessor(s, s.left.left).value);
        assertNull(FindSuccessor.findSuccessor(s, s.right));
        assertTrue(HeightBalancedBinaryTree.heightBalancedBinaryTree(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, null, 6)));
        assertFalse(HeightBalancedBinaryTree.heightBalancedBinaryTree(BinaryTree.fromLevelOrder(1, 2, null, 3)));
        var merged = MergeBinaryTrees.mergeBinaryTrees(BinaryTree.fromLevelOrder(1, 3, 2, 7, 4), BinaryTree.fromLevelOrder(1, 5, 9, 2, null, 7, 6));
        assertEquals(List.of(9, 8, 4, 2, 7, 11, 6), BinaryTree.inOrder(merged));
        assertTrue(SymmetricalTree.symmetricalTree(BinaryTree.fromLevelOrder(1, 2, 2, 3, 4, 4, 3)));
        assertFalse(SymmetricalTree.symmetricalTree(BinaryTree.fromLevelOrder(1, 2, 2, 3, null, 3)));
        assertEquals(3, SplitBinaryTree.splitBinaryTree(BinaryTree.fromLevelOrder(1, 2, 3)));
        assertEquals(0, SplitBinaryTree.splitBinaryTree(BinaryTree.fromLevelOrder(1, 2)));
    }

    @Test void dp() {
        assertEquals(330, MaxSubsetSumNoAdjacent.maxSubsetSumNoAdjacent(new int[]{75, 105, 120, 75, 90, 135}));
        assertEquals(0, MaxSubsetSumNoAdjacent.maxSubsetSumNoAdjacent(new int[]{}));
        assertEquals(2, NumberOfWaysToMakeChange.numberOfWaysToMakeChange(6, new int[]{1, 5}));
        assertEquals(1, NumberOfWaysToMakeChange.numberOfWaysToMakeChange(0, new int[]{2}));
        assertEquals(3, MinNumberOfCoinsForChange.minNumberOfCoinsForChange(7, new int[]{1, 5, 10}));
        assertEquals(-1, MinNumberOfCoinsForChange.minNumberOfCoinsForChange(3, new int[]{2}));
        assertEquals(2, LevenshteinDistance.levenshteinDistance("abc", "yabd"));
        assertEquals(3, LevenshteinDistance.levenshteinDistance("", "abc"));
        assertEquals(10, NumberOfWaysToTraverseGraph.numberOfWaysToTraverseGraph(4, 3));
        assertEquals(1, NumberOfWaysToTraverseGraph.numberOfWaysToTraverseGraph(1, 5));
    }

    @Test void famous() {
        assertEquals(19, KadanesAlgorithm.kadanesAlgorithm(new int[]{3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4}));
        assertEquals(-1, KadanesAlgorithm.kadanesAlgorithm(new int[]{-3, -1, -2}));
        int[][] m = StableInternships.stableInternships(new int[][]{{0, 1}, {1, 0}}, new int[][]{{1, 0}, {1, 0}});
        assertArrayEquals(new int[][]{{0, 0}, {1, 1}}, m);
        var uf = new UnionFind();
        assertNull(uf.find(1));
        uf.createSet(1); uf.createSet(2); uf.createSet(3);
        uf.union(1, 2);
        assertEquals(uf.find(1), uf.find(2));
        assertNotEquals(uf.find(1), uf.find(3));
    }

    @Test void graphs() {
        var a = new BreadthFirstSearch.Node("A").addChild("B").addChild("C");
        a.children.get(0).addChild("D");
        assertEquals(List.of("A", "B", "C", "D"), a.breadthFirstSearch(new ArrayList<>()));
        assertTrue(SingleCycleCheck.hasSingleCycle(new int[]{2, 3, 1, -4, -4, 2}));
        assertFalse(SingleCycleCheck.hasSingleCycle(new int[]{1, -1, 1, -1}));
        var sizes = RiverSizes.riverSizes(new int[][]{{1, 0, 0, 1, 0}, {1, 0, 1, 0, 0}, {0, 0, 1, 0, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 0}});
        sizes.sort(null);
        assertEquals(List.of(1, 2, 2, 2, 5), sizes);
        var A = new YoungestCommonAncestor.AncestralTree('A');
        var B = new YoungestCommonAncestor.AncestralTree('B'); B.ancestor = A;
        var C = new YoungestCommonAncestor.AncestralTree('C'); C.ancestor = A;
        var D = new YoungestCommonAncestor.AncestralTree('D'); D.ancestor = B;
        assertEquals('A', YoungestCommonAncestor.getYoungestCommonAncestor(A, D, C).name);
        assertEquals('B', YoungestCommonAncestor.getYoungestCommonAncestor(A, D, B).name);
        int[][] isl = {{1, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}};
        assertArrayEquals(new int[][]{{1, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 1}}, RemoveIslands.removeIslands(isl));
        assertTrue(CycleInGraph.cycleInGraph(new int[][]{{1, 3}, {2, 3, 4}, {0}, {}, {2, 5}, {}}));
        assertFalse(CycleInGraph.cycleInGraph(new int[][]{{1}, {2}, {}}));
        assertEquals(3, MinimumPassesOfMatrix.minimumPassesOfMatrix(new int[][]{{0, -1, -3, 2, 0}, {1, -2, -5, -1, -3}, {3, 0, 0, -4, -1}}));
        assertEquals(-1, MinimumPassesOfMatrix.minimumPassesOfMatrix(new int[][]{{-1, 0, 1}}));
        assertTrue(TwoColorable.twoColorable(new int[][]{{1}, {0, 2}, {1}}));
        assertFalse(TwoColorable.twoColorable(new int[][]{{1, 2}, {0, 2}, {0, 1}}));
    }

    @Test void greedy() {
        var r = TaskAssignment.taskAssignment(3, List.of(1, 3, 5, 3, 1, 4));
        assertEquals(6, r.stream().mapToInt(p -> List.of(1, 3, 5, 3, 1, 4).get(p.get(0)) + List.of(1, 3, 5, 3, 1, 4).get(p.get(1))).max().getAsInt());
        assertEquals(4, ValidStartingCity.validStartingCity(new int[]{5, 25, 15, 10, 15}, new int[]{1, 2, 1, 0, 3}, 10));
        assertEquals(0, ValidStartingCity.validStartingCity(new int[]{10}, new int[]{1}, 10));
    }

    @Test void heapsAndLists() {
        var h = new MinHeapConstruction.MinHeap(List.of(48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41));
        h.insert(76);
        assertEquals(-5, h.peek());
        assertEquals(-5, h.remove());
        assertEquals(2, h.remove());
        var dll = new LinkedListConstruction.DoublyLinkedList();
        var n1 = new LinkedListConstruction.Node(1); var n2 = new LinkedListConstruction.Node(2);
        var n3 = new LinkedListConstruction.Node(3); var n4 = new LinkedListConstruction.Node(3);
        dll.setHead(n1); dll.setTail(n2); dll.setTail(n3); dll.insertAtPosition(1, n4);
        assertEquals(List.of(3, 1, 2, 3), dll.values());
        dll.removeNodesWithValue(3);
        assertEquals(List.of(1, 2), dll.values());
        dll.setHead(n2);
        assertEquals(List.of(2, 1), dll.values());
        assertFalse(dll.containsNodeWithValue(3));
        var l = LinkedListNode.of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9);
        RemoveKthNodeFromEnd.removeKthNodeFromEnd(l, 4);
        assertEquals(List.of(0, 1, 2, 3, 4, 5, 7, 8, 9), LinkedListNode.toList(l));
        var l2 = LinkedListNode.of(1, 2);
        RemoveKthNodeFromEnd.removeKthNodeFromEnd(l2, 2);
        assertEquals(List.of(2), LinkedListNode.toList(l2));
        assertEquals(List.of(1, 9, 2, 2), LinkedListNode.toList(SumOfLinkedLists.sumOfLinkedLists(LinkedListNode.of(2, 4, 7, 1), LinkedListNode.of(9, 4, 5))));
        assertEquals(List.of(0, 1), LinkedListNode.toList(SumOfLinkedLists.sumOfLinkedLists(LinkedListNode.of(5), LinkedListNode.of(5))));
        var shared = LinkedListNode.of(7, 8);
        var x = LinkedListNode.of(1, 2); x.next.next = shared;
        var y = LinkedListNode.of(5); y.next = shared;
        assertSame(shared, MergingLinkedLists.mergingLinkedLists(x, y));
        assertNull(MergingLinkedLists.mergingLinkedLists(LinkedListNode.of(1), LinkedListNode.of(2)));
    }

    @Test void recursion() {
        assertEquals(6, Permutations.getPermutations(List.of(1, 2, 3)).size());
        assertTrue(Permutations.getPermutations(List.of()).isEmpty());
        assertEquals(8, Powerset.powerset(List.of(1, 2, 3)).size());
        assertEquals(List.of(List.of()), Powerset.powerset(List.of()));
        assertEquals(List.of("1a", "1b", "1c"), PhoneNumberMnemonics.phoneNumberMnemonics("12"));
        assertEquals(12, PhoneNumberMnemonics.phoneNumberMnemonics("1905").size());
        assertEquals(5, StaircaseTraversal.staircaseTraversal(4, 2));
        assertEquals(1, StaircaseTraversal.staircaseTraversal(0, 3));
        assertEquals(0.45f, BlackjackProbability.blackjackProbability(21, 15), 1e-6);
        assertEquals(0f, BlackjackProbability.blackjackProbability(21, 21), 1e-6);
        String[][] board = {{"H", "H", "H"}, {"H", "H", "M"}, {"H", "H", "H"}};
        RevealMinesweeper.revealMinesweeper(board, 0, 0);
        assertArrayEquals(new String[][]{{"0", "1", "H"}, {"0", "1", "M"}, {"0", "1", "H"}}, board);
        String[][] b2 = {{"M"}};
        assertEquals("X", RevealMinesweeper.revealMinesweeper(b2, 0, 0)[0][0]);
    }

    @Test void searchingSorting() {
        int[][] m = {{1, 4, 7, 12, 15, 1000}, {2, 5, 19, 31, 32, 1001}, {3, 8, 24, 33, 35, 1002}, {40, 41, 42, 44, 45, 1003}, {99, 100, 103, 106, 128, 1004}};
        assertArrayEquals(new int[]{3, 3}, SearchInSortedMatrix.searchInSortedMatrix(m, 44));
        assertArrayEquals(new int[]{-1, -1}, SearchInSortedMatrix.searchInSortedMatrix(m, 43));
        assertArrayEquals(new int[]{0, 0, -1, -1, -1, 1, 1}, ThreeNumberSort.threeNumberSort(new int[]{1, 0, -1, 0, -1, 1, -1}, new int[]{0, -1, 1}));
        assertArrayEquals(new int[]{}, ThreeNumberSort.threeNumberSort(new int[]{}, new int[]{0, 1, 2}));
    }

    @Test void stacks() {
        assertTrue(BalancedBrackets.balancedBrackets("([])(){}(())()()"));
        assertFalse(BalancedBrackets.balancedBrackets("(]"));
        assertEquals(List.of(1, 3, 6, 7), SunsetViews.sunsetViews(new int[]{3, 5, 4, 4, 3, 1, 3, 2}, "EAST"));
        assertEquals(List.of(0, 1), SunsetViews.sunsetViews(new int[]{3, 5, 4, 4, 3, 1, 3, 2}, "WEST"));
        assertEquals("772", BestDigits.bestDigits("1772", 1));
        assertEquals("6839", BestDigits.bestDigits("462839", 2));
        assertEquals(List.of(-5, -2, -1, 2, 3, 4), SortStack.sortStack(new ArrayList<>(List.of(-5, 2, -2, 4, 3, -1))));
        assertArrayEquals(new int[]{5, 6, 6, 6, 7, -1, 5}, NextGreaterElement.nextGreaterElement(new int[]{2, 5, -3, -4, 6, 7, 2}));
        var s = new MinMaxStackConstruction.MinMaxStack();
        s.push(5); s.push(7); s.push(2);
        assertEquals(2, s.getMin()); assertEquals(7, s.getMax());
        s.pop();
        assertEquals(5, s.getMin()); assertEquals(7, s.peek());
        assertEquals(2, ReversePolishNotation.reversePolishNotation(new String[]{"50", "3", "17", "+", "2", "-", "/"}));
        assertEquals(-1, ReversePolishNotation.reversePolishNotation(new String[]{"2", "3", "-"}));
        assertArrayEquals(new int[]{-3, -8, 6}, CollidingAsteroids.collidingAsteroids(new int[]{-3, 5, -8, 6, 7, -4, -7}));
        assertArrayEquals(new int[]{}, CollidingAsteroids.collidingAsteroids(new int[]{5, -5}));
    }

    @Test void strings() {
        assertEquals("xyzzyx", LongestPalindromicSubstring.longestPalindromicSubstring("abaxyzzyxf"));
        assertEquals("a", LongestPalindromicSubstring.longestPalindromicSubstring("a"));
        var g = GroupAnagrams.groupAnagrams(List.of("yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"));
        assertEquals(4, g.size());
        assertEquals(List.of("act", "tac", "cat"), g.get(1));
        var ips = ValidIpAddresses.validIPAddresses("1921680");
        assertEquals(11, ips.size());
        assertTrue(ips.contains("19.216.8.0"));
        assertFalse(ips.contains("192.168.0"));
        assertTrue(ValidIpAddresses.validIPAddresses("0000").contains("0.0.0.0"));
        assertEquals("best! the is AlgoExpert", ReverseWordsInString.reverseWordsInString("AlgoExpert is the best!"));
        assertEquals("b  a ", ReverseWordsInString.reverseWordsInString(" a  b"));
        char[] mc = MinimumCharactersForWords.minimumCharactersForWords(new String[]{"this", "that", "did", "deed", "them!", "a"});
        assertEquals(12, mc.length);
        assertTrue(OneEdit.oneEdit("hello", "helo"));
        assertTrue(OneEdit.oneEdit("abc", "abd"));
        assertFalse(OneEdit.oneEdit("abc", "acd"));
        var trie = new SuffixTrieConstruction.SuffixTrie("babc");
        assertTrue(trie.contains("abc"));
        assertFalse(trie.contains("ab"));
    }
}
