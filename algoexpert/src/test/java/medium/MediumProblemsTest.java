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
import java.util.HashSet;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/** One test per Medium problem, each covering the sample plus edge cases. */
class MediumProblemsTest {
    // ---------- Arrays ----------
    @Test void threeNumberSum() {
        var t = ThreeNumberSum.threeNumberSum(new int[]{12, 3, 1, 2, -6, 5, -8, 6}, 0);
        assertEquals(3, t.size());
        assertArrayEquals(new Integer[]{-8, 2, 6}, t.get(0));
        assertArrayEquals(new Integer[]{-6, 1, 5}, t.get(2));
        assertTrue(ThreeNumberSum.threeNumberSum(new int[]{1, 2, 3}, 100).isEmpty());
        assertTrue(ThreeNumberSum.threeNumberSum(new int[]{}, 0).isEmpty());
    }

    @Test void smallestDifference() {
        assertArrayEquals(new int[]{28, 26}, SmallestDifference.smallestDifference(new int[]{-1, 5, 10, 20, 28, 3}, new int[]{26, 134, 135, 15, 17}));
        assertArrayEquals(new int[]{10, 10}, SmallestDifference.smallestDifference(new int[]{10, 0}, new int[]{10, 50}));
        assertArrayEquals(new int[]{-5, -4}, SmallestDifference.smallestDifference(new int[]{-5}, new int[]{-4, 100}));
    }

    @Test void moveElementToEnd() {
        var m = MoveElementToEnd.moveElementToEnd(new ArrayList<>(List.of(2, 1, 2, 2, 2, 3, 4, 2)), 2);
        assertEquals(List.of(2, 2, 2, 2, 2), m.subList(3, 8));
        assertEquals(List.of(), MoveElementToEnd.moveElementToEnd(new ArrayList<>(), 3));
        assertEquals(List.of(1, 2), MoveElementToEnd.moveElementToEnd(new ArrayList<>(List.of(1, 2)), 5));
        assertEquals(List.of(4, 4), MoveElementToEnd.moveElementToEnd(new ArrayList<>(List.of(4, 4)), 4));
    }

    @Test void monotonicArray() {
        assertTrue(MonotonicArray.isMonotonic(new int[]{-1, -5, -10, -1100, -1100, -1101}));
        assertFalse(MonotonicArray.isMonotonic(new int[]{1, 2, 1}));
        assertTrue(MonotonicArray.isMonotonic(new int[]{}));
        assertTrue(MonotonicArray.isMonotonic(new int[]{3, 3, 3}));
    }

    @Test void spiralTraverse() {
        assertEquals(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), SpiralTraverse.spiralTraverse(new int[][]{{1, 2, 3, 4}, {10, 11, 12, 5}, {9, 8, 7, 6}}));
        assertEquals(List.of(1, 2, 3), SpiralTraverse.spiralTraverse(new int[][]{{1}, {2}, {3}}));
        assertEquals(List.of(1, 2, 3), SpiralTraverse.spiralTraverse(new int[][]{{1, 2, 3}}));
        assertEquals(List.of(), SpiralTraverse.spiralTraverse(new int[][]{}));
    }

    @Test void longestPeak() {
        assertEquals(6, LongestPeak.longestPeak(new int[]{1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3}));
        assertEquals(0, LongestPeak.longestPeak(new int[]{1, 2, 3}));
        assertEquals(0, LongestPeak.longestPeak(new int[]{}));
        assertEquals(0, LongestPeak.longestPeak(new int[]{1, 1, 1}), "plateaus are not peaks");
        assertEquals(3, LongestPeak.longestPeak(new int[]{1, 3, 2}));
    }

    @Test void arrayOfProducts() {
        assertArrayEquals(new int[]{8, 40, 10, 20}, ArrayOfProducts.arrayOfProducts(new int[]{5, 1, 4, 2}));
        assertArrayEquals(new int[]{0, 0, 6}, ArrayOfProducts.arrayOfProducts(new int[]{2, 3, 0}));
        assertArrayEquals(new int[]{-2, 1}, ArrayOfProducts.arrayOfProducts(new int[]{1, -2}));
    }

    @Test void firstDuplicateValue() {
        assertEquals(2, FirstDuplicateValue.firstDuplicateValue(new int[]{2, 1, 5, 2, 3, 3, 4}));
        assertEquals(-1, FirstDuplicateValue.firstDuplicateValue(new int[]{1, 2, 3}));
        assertEquals(-1, FirstDuplicateValue.firstDuplicateValue(new int[]{1}));
        assertEquals(1, FirstDuplicateValue.firstDuplicateValue(new int[]{1, 1, 1}));
    }

    @Test void mergeOverlappingIntervals() {
        assertArrayEquals(new int[][]{{1, 2}, {3, 8}, {9, 10}}, MergeOverlappingIntervals.mergeOverlappingIntervals(new int[][]{{1, 2}, {3, 5}, {4, 7}, {6, 8}, {9, 10}}));
        assertArrayEquals(new int[][]{{1, 10}}, MergeOverlappingIntervals.mergeOverlappingIntervals(new int[][]{{2, 3}, {1, 10}}));
        assertArrayEquals(new int[][]{{-5, -1}}, MergeOverlappingIntervals.mergeOverlappingIntervals(new int[][]{{-5, -1}}));
        assertArrayEquals(new int[][]{{1, 4}}, MergeOverlappingIntervals.mergeOverlappingIntervals(new int[][]{{1, 2}, {2, 4}}), "touching intervals merge");
    }

    @Test void bestSeat() {
        assertEquals(4, BestSeat.bestSeat(new int[]{1, 0, 1, 0, 0, 0, 1}));
        assertEquals(-1, BestSeat.bestSeat(new int[]{1, 1}));
        assertEquals(1, BestSeat.bestSeat(new int[]{1, 0, 1}));
        assertEquals(1, BestSeat.bestSeat(new int[]{1, 0, 0, 1}), "ties go to the lowest index");
    }

    @Test void zeroSumSubarray() {
        assertTrue(ZeroSumSubarray.zeroSumSubarray(new int[]{-5, -5, 2, 3, -2}));
        assertFalse(ZeroSumSubarray.zeroSumSubarray(new int[]{1, 2, 3}));
        assertFalse(ZeroSumSubarray.zeroSumSubarray(new int[]{}));
        assertTrue(ZeroSumSubarray.zeroSumSubarray(new int[]{0}));
    }

    @Test void missingNumbers() {
        assertArrayEquals(new int[]{2, 5}, MissingNumbers.missingNumbers(new int[]{1, 4, 3}));
        assertArrayEquals(new int[]{1, 2}, MissingNumbers.missingNumbers(new int[]{}));
        assertArrayEquals(new int[]{4, 5}, MissingNumbers.missingNumbers(new int[]{3, 1, 2}));
    }

    @Test void majorityElement() {
        assertEquals(2, MajorityElement.majorityElement(new int[]{1, 2, 3, 2, 2, 1, 2}));
        assertEquals(7, MajorityElement.majorityElement(new int[]{7}));
        assertEquals(-1, MajorityElement.majorityElement(new int[]{-1, -1, 5}));
    }

    @Test void sweetAndSavory() {
        assertArrayEquals(new int[]{-3, 7}, SweetAndSavory.sweetAndSavory(new int[]{-3, -5, 1, 7}, 8));
        assertArrayEquals(new int[]{0, 0}, SweetAndSavory.sweetAndSavory(new int[]{2, 5, -4, -7, 12, 100, -25}, -50));
        assertArrayEquals(new int[]{0, 0}, SweetAndSavory.sweetAndSavory(new int[]{}, 3));
        assertArrayEquals(new int[]{0, 0}, SweetAndSavory.sweetAndSavory(new int[]{1, 2}, 3), "needs one of each kind");
    }

    // ---------- BST ----------
    @Test void bstConstruction() {
        var b = new BstConstruction.BST(10).insert(5).insert(15).insert(2).insert(5).insert(13).insert(22).insert(1).insert(14).insert(12);
        b.remove(10);
        assertFalse(b.contains(10));
        assertEquals(12, b.value);
        assertTrue(b.contains(15));
        assertTrue(new BstConstruction.BST(1).remove(1).contains(1), "removing the lone root is a no-op");
        var two = new BstConstruction.BST(5).insert(3).remove(5);
        assertEquals(3, two.value);
        assertFalse(two.contains(5));
        assertTrue(new BstConstruction.BST(5).insert(5).remove(5).contains(5), "duplicate survives single removal");
    }

    @Test void validateBst() {
        BST t = BST.of(10, 5, 15, 2, 5, 13, 22, 1, 14);
        assertTrue(ValidateBst.validateBst(t));
        assertTrue(ValidateBst.validateBst(new BST(1)));
        t.left.value = 11;
        assertFalse(ValidateBst.validateBst(t));
        BST dupLeft = new BST(5);
        dupLeft.left = new BST(5);
        assertFalse(ValidateBst.validateBst(dupLeft), "equal values must go right");
    }

    @Test void bstTraversal() {
        BST u = BST.of(10, 5, 15, 2, 5, 22, 1);
        assertEquals(List.of(1, 2, 5, 5, 10, 15, 22), BstTraversal.inOrderTraverse(u, new ArrayList<>()));
        assertEquals(List.of(10, 5, 2, 1, 5, 15, 22), BstTraversal.preOrderTraverse(u, new ArrayList<>()));
        assertEquals(List.of(1, 2, 5, 5, 22, 15, 10), BstTraversal.postOrderTraverse(u, new ArrayList<>()));
        assertEquals(List.of(), BstTraversal.inOrderTraverse(null, new ArrayList<>()));
    }

    @Test void minHeightBst() {
        var mh = MinHeightBst.minHeightBst(List.of(1, 2, 5, 7, 10, 13, 14, 15, 22));
        assertEquals(4, MinHeightBst.height(mh));
        assertTrue(ValidateBst.validateBst(mh));
        assertEquals(1, MinHeightBst.height(MinHeightBst.minHeightBst(List.of(8))));
        assertNull(MinHeightBst.minHeightBst(List.of()));
    }

    @Test void findKthLargestValueInBst() {
        BST t = BST.of(15, 5, 20, 2, 5, 17, 22, 1, 3);
        assertEquals(17, FindKthLargestValueInBst.findKthLargestValueInBst(t, 3));
        assertEquals(22, FindKthLargestValueInBst.findKthLargestValueInBst(t, 1));
        assertEquals(1, FindKthLargestValueInBst.findKthLargestValueInBst(t, 9));
        assertEquals(5, FindKthLargestValueInBst.findKthLargestValueInBst(t, 5), "duplicates counted separately");
    }

    @Test void reconstructBst() {
        var r = ReconstructBst.reconstructBst(List.of(10, 4, 2, 1, 5, 17, 19, 18));
        assertEquals(List.of(10, 4, 2, 1, 5, 17, 19, 18), BstTraversal.preOrderTraverse(r, new ArrayList<>()));
        assertNull(ReconstructBst.reconstructBst(List.of()));
        var dup = ReconstructBst.reconstructBst(List.of(2, 2, 2));
        assertEquals(2, dup.right.right.value, "duplicates go right");
    }

    // ---------- Binary trees ----------
    @Test void invertBinaryTree() {
        BinaryTree t = BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, 6, 7);
        InvertBinaryTree.invertBinaryTree(t);
        assertEquals(List.of(7, 3, 6, 1, 5, 2, 4), BinaryTree.inOrder(t));
        assertDoesNotThrow(() -> InvertBinaryTree.invertBinaryTree(null));
        BinaryTree single = new BinaryTree(1);
        InvertBinaryTree.invertBinaryTree(single);
        assertEquals(List.of(1), BinaryTree.inOrder(single));
    }

    @Test void binaryTreeDiameter() {
        assertEquals(6, BinaryTreeDiameter.binaryTreeDiameter(BinaryTree.fromLevelOrder(1, 3, 2, 7, 4, null, null, 8, null, null, 5, 9, null, null, 6)));
        assertEquals(0, BinaryTreeDiameter.binaryTreeDiameter(new BinaryTree(1)));
        assertEquals(2, BinaryTreeDiameter.binaryTreeDiameter(BinaryTree.fromLevelOrder(1, 2, 3)));
    }

    @Test void findSuccessor() {
        BinaryTree s = BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, null, null, 6);
        assertEquals(1, FindSuccessor.findSuccessor(s, s.left.right).value);
        assertEquals(2, FindSuccessor.findSuccessor(s, s.left.left).value);
        assertNull(FindSuccessor.findSuccessor(s, s.right));
        BinaryTree one = new BinaryTree(9);
        assertNull(FindSuccessor.findSuccessor(one, one));
    }

    @Test void heightBalancedBinaryTree() {
        assertTrue(HeightBalancedBinaryTree.heightBalancedBinaryTree(BinaryTree.fromLevelOrder(1, 2, 3, 4, 5, null, 6)));
        assertFalse(HeightBalancedBinaryTree.heightBalancedBinaryTree(BinaryTree.fromLevelOrder(1, 2, null, 3)));
        assertTrue(HeightBalancedBinaryTree.heightBalancedBinaryTree(new BinaryTree(1)));
        assertTrue(HeightBalancedBinaryTree.heightBalancedBinaryTree(null));
    }

    @Test void mergeBinaryTrees() {
        var merged = MergeBinaryTrees.mergeBinaryTrees(BinaryTree.fromLevelOrder(1, 3, 2, 7, 4), BinaryTree.fromLevelOrder(1, 5, 9, 2, null, 7, 6));
        assertEquals(List.of(9, 8, 4, 2, 7, 11, 6), BinaryTree.inOrder(merged));
        assertEquals(List.of(5), BinaryTree.inOrder(MergeBinaryTrees.mergeBinaryTrees(null, new BinaryTree(5))));
        assertEquals(List.of(-1), BinaryTree.inOrder(MergeBinaryTrees.mergeBinaryTrees(new BinaryTree(2), new BinaryTree(-3))));
    }

    @Test void symmetricalTree() {
        assertTrue(SymmetricalTree.symmetricalTree(BinaryTree.fromLevelOrder(1, 2, 2, 3, 4, 4, 3)));
        assertFalse(SymmetricalTree.symmetricalTree(BinaryTree.fromLevelOrder(1, 2, 2, 3, null, 3)));
        assertTrue(SymmetricalTree.symmetricalTree(new BinaryTree(1)));
        assertFalse(SymmetricalTree.symmetricalTree(BinaryTree.fromLevelOrder(1, 2, 3)));
    }

    @Test void splitBinaryTree() {
        assertEquals(3, SplitBinaryTree.splitBinaryTree(BinaryTree.fromLevelOrder(1, 2, 3)));
        assertEquals(0, SplitBinaryTree.splitBinaryTree(BinaryTree.fromLevelOrder(1, 2)));
        assertEquals(0, SplitBinaryTree.splitBinaryTree(new BinaryTree(0)), "a single node has no edge to cut");
        assertEquals(0, SplitBinaryTree.splitBinaryTree(BinaryTree.fromLevelOrder(0, 0)), "zero-sum halves");
    }

    // ---------- Dynamic programming ----------
    @Test void maxSubsetSumNoAdjacent() {
        assertEquals(330, MaxSubsetSumNoAdjacent.maxSubsetSumNoAdjacent(new int[]{75, 105, 120, 75, 90, 135}));
        assertEquals(0, MaxSubsetSumNoAdjacent.maxSubsetSumNoAdjacent(new int[]{}));
        assertEquals(7, MaxSubsetSumNoAdjacent.maxSubsetSumNoAdjacent(new int[]{7}));
        assertEquals(10, MaxSubsetSumNoAdjacent.maxSubsetSumNoAdjacent(new int[]{5, 5, 5}));
    }

    @Test void numberOfWaysToMakeChange() {
        assertEquals(2, NumberOfWaysToMakeChange.numberOfWaysToMakeChange(6, new int[]{1, 5}));
        assertEquals(1, NumberOfWaysToMakeChange.numberOfWaysToMakeChange(0, new int[]{2}));
        assertEquals(0, NumberOfWaysToMakeChange.numberOfWaysToMakeChange(3, new int[]{2}));
        assertEquals(4, NumberOfWaysToMakeChange.numberOfWaysToMakeChange(10, new int[]{1, 5, 10, 25}));
    }

    @Test void minNumberOfCoinsForChange() {
        assertEquals(3, MinNumberOfCoinsForChange.minNumberOfCoinsForChange(7, new int[]{1, 5, 10}));
        assertEquals(-1, MinNumberOfCoinsForChange.minNumberOfCoinsForChange(3, new int[]{2}));
        assertEquals(0, MinNumberOfCoinsForChange.minNumberOfCoinsForChange(0, new int[]{1}));
        assertEquals(2, MinNumberOfCoinsForChange.minNumberOfCoinsForChange(6, new int[]{1, 3, 4}), "greedy would give 3");
    }

    @Test void levenshteinDistance() {
        assertEquals(2, LevenshteinDistance.levenshteinDistance("abc", "yabd"));
        assertEquals(3, LevenshteinDistance.levenshteinDistance("", "abc"));
        assertEquals(0, LevenshteinDistance.levenshteinDistance("same", "same"));
        assertEquals(0, LevenshteinDistance.levenshteinDistance("", ""));
    }

    @Test void numberOfWaysToTraverseGraph() {
        assertEquals(10, NumberOfWaysToTraverseGraph.numberOfWaysToTraverseGraph(4, 3));
        assertEquals(1, NumberOfWaysToTraverseGraph.numberOfWaysToTraverseGraph(1, 5));
        assertEquals(1, NumberOfWaysToTraverseGraph.numberOfWaysToTraverseGraph(1, 1));
        assertEquals(48620, NumberOfWaysToTraverseGraph.numberOfWaysToTraverseGraph(10, 10));
    }

    // ---------- Famous algorithms ----------
    @Test void kadanesAlgorithm() {
        assertEquals(19, KadanesAlgorithm.kadanesAlgorithm(new int[]{3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4}));
        assertEquals(-1, KadanesAlgorithm.kadanesAlgorithm(new int[]{-3, -1, -2}));
        assertEquals(5, KadanesAlgorithm.kadanesAlgorithm(new int[]{5}));
    }

    @Test void stableInternships() {
        assertArrayEquals(new int[][]{{0, 0}, {1, 1}}, StableInternships.stableInternships(new int[][]{{0, 1}, {1, 0}}, new int[][]{{1, 0}, {1, 0}}));
        assertArrayEquals(new int[][]{{0, 0}}, StableInternships.stableInternships(new int[][]{{0}}, new int[][]{{0}}));
        // both interns want team 0; team 0 prefers intern 1
        assertArrayEquals(new int[][]{{0, 1}, {1, 0}}, StableInternships.stableInternships(new int[][]{{0, 1}, {0, 1}}, new int[][]{{1, 0}, {0, 1}}));
    }

    @Test void unionFind() {
        var uf = new UnionFind();
        assertNull(uf.find(1));
        uf.createSet(1); uf.createSet(2); uf.createSet(3);
        uf.union(1, 2);
        assertEquals(uf.find(1), uf.find(2));
        assertNotEquals(uf.find(1), uf.find(3));
        uf.union(1, 99);
        assertNull(uf.find(99), "union with unknown value is ignored");
        uf.union(2, 2);
        assertEquals(uf.find(1), uf.find(2));
    }

    // ---------- Graphs ----------
    @Test void breadthFirstSearch() {
        var a = new BreadthFirstSearch.Node("A").addChild("B").addChild("C");
        a.children.get(0).addChild("D");
        assertEquals(List.of("A", "B", "C", "D"), a.breadthFirstSearch(new ArrayList<>()));
        assertEquals(List.of("Z"), new BreadthFirstSearch.Node("Z").breadthFirstSearch(new ArrayList<>()));
    }

    @Test void singleCycleCheck() {
        assertTrue(SingleCycleCheck.hasSingleCycle(new int[]{2, 3, 1, -4, -4, 2}));
        assertFalse(SingleCycleCheck.hasSingleCycle(new int[]{1, -1, 1, -1}));
        assertTrue(SingleCycleCheck.hasSingleCycle(new int[]{0}));
        assertTrue(SingleCycleCheck.hasSingleCycle(new int[]{3, -5}), "large jumps wrap");
    }

    @Test void riverSizes() {
        var sizes = RiverSizes.riverSizes(new int[][]{{1, 0, 0, 1, 0}, {1, 0, 1, 0, 0}, {0, 0, 1, 0, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 0}});
        sizes.sort(null);
        assertEquals(List.of(1, 2, 2, 2, 5), sizes);
        assertEquals(List.of(), RiverSizes.riverSizes(new int[][]{{0}}));
        assertEquals(List.of(4), RiverSizes.riverSizes(new int[][]{{1, 1}, {1, 1}}));
    }

    @Test void youngestCommonAncestor() {
        var A = new YoungestCommonAncestor.AncestralTree('A');
        var B = new YoungestCommonAncestor.AncestralTree('B'); B.ancestor = A;
        var C = new YoungestCommonAncestor.AncestralTree('C'); C.ancestor = A;
        var D = new YoungestCommonAncestor.AncestralTree('D'); D.ancestor = B;
        assertEquals('A', YoungestCommonAncestor.getYoungestCommonAncestor(A, D, C).name);
        assertEquals('B', YoungestCommonAncestor.getYoungestCommonAncestor(A, D, B).name);
        assertEquals('A', YoungestCommonAncestor.getYoungestCommonAncestor(A, A, A).name);
    }

    @Test void removeIslands() {
        int[][] isl = {{1, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}};
        assertArrayEquals(new int[][]{{1, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 1}}, RemoveIslands.removeIslands(isl));
        assertArrayEquals(new int[][]{{1}}, RemoveIslands.removeIslands(new int[][]{{1}}));
        assertArrayEquals(new int[][]{{1, 1, 1}, {1, 1, 1}, {1, 1, 1}}, RemoveIslands.removeIslands(new int[][]{{1, 1, 1}, {1, 1, 1}, {1, 1, 1}}), "centre connects to border");
    }

    @Test void cycleInGraph() {
        assertTrue(CycleInGraph.cycleInGraph(new int[][]{{1, 3}, {2, 3, 4}, {0}, {}, {2, 5}, {}}));
        assertFalse(CycleInGraph.cycleInGraph(new int[][]{{1}, {2}, {}}));
        assertTrue(CycleInGraph.cycleInGraph(new int[][]{{0}}), "self loop");
        assertFalse(CycleInGraph.cycleInGraph(new int[][]{{1, 2}, {2}, {}}), "diamond is not a cycle");
    }

    @Test void minimumPassesOfMatrix() {
        assertEquals(3, MinimumPassesOfMatrix.minimumPassesOfMatrix(new int[][]{{0, -1, -3, 2, 0}, {1, -2, -5, -1, -3}, {3, 0, 0, -4, -1}}));
        assertEquals(-1, MinimumPassesOfMatrix.minimumPassesOfMatrix(new int[][]{{-1, 0, 1}}));
        assertEquals(0, MinimumPassesOfMatrix.minimumPassesOfMatrix(new int[][]{{1, 2}}));
        assertEquals(-1, MinimumPassesOfMatrix.minimumPassesOfMatrix(new int[][]{{-1}}));
    }

    @Test void twoColorable() {
        assertTrue(TwoColorable.twoColorable(new int[][]{{1}, {0, 2}, {1}}));
        assertFalse(TwoColorable.twoColorable(new int[][]{{1, 2}, {0, 2}, {0, 1}}));
        assertTrue(TwoColorable.twoColorable(new int[][]{{}}));
        assertFalse(TwoColorable.twoColorable(new int[][]{{0}}), "self loop");
    }

    // ---------- Greedy ----------
    @Test void taskAssignment() {
        List<Integer> tasks = List.of(1, 3, 5, 3, 1, 4);
        var r = TaskAssignment.taskAssignment(3, tasks);
        assertEquals(6, r.stream().mapToInt(p -> tasks.get(p.get(0)) + tasks.get(p.get(1))).max().getAsInt());
        var used = new HashSet<Integer>();
        r.forEach(used::addAll);
        assertEquals(6, used.size(), "every task assigned once");
        assertEquals(1, TaskAssignment.taskAssignment(1, List.of(2, 2)).size());
    }

    @Test void validStartingCity() {
        assertEquals(4, ValidStartingCity.validStartingCity(new int[]{5, 25, 15, 10, 15}, new int[]{1, 2, 1, 0, 3}, 10));
        assertEquals(0, ValidStartingCity.validStartingCity(new int[]{10}, new int[]{1}, 10));
        assertEquals(1, ValidStartingCity.validStartingCity(new int[]{10, 10}, new int[]{0, 2}, 10));
    }

    // ---------- Heaps ----------
    @Test void minHeapConstruction() {
        var h = new MinHeapConstruction.MinHeap(List.of(48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41));
        h.insert(76);
        assertEquals(-5, h.peek());
        assertEquals(-5, h.remove());
        assertEquals(2, h.remove());
        var e = new MinHeapConstruction.MinHeap(List.of());
        assertTrue(e.isEmpty());
        e.insert(3); e.insert(3); e.insert(1);
        assertEquals(1, e.remove());
        assertEquals(3, e.remove());
        assertEquals(3, e.remove());
        assertTrue(e.isEmpty());
    }

    // ---------- Linked lists ----------
    @Test void linkedListConstruction() {
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
        dll.remove(n1); dll.remove(n2);
        assertNull(dll.head);
        assertNull(dll.tail);
        var single = new LinkedListConstruction.Node(7);
        dll.setTail(single);
        assertSame(dll.head, dll.tail);
    }

    @Test void removeKthNodeFromEnd() {
        var l = LinkedListNode.of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9);
        RemoveKthNodeFromEnd.removeKthNodeFromEnd(l, 4);
        assertEquals(List.of(0, 1, 2, 3, 4, 5, 7, 8, 9), LinkedListNode.toList(l));
        var l2 = LinkedListNode.of(1, 2);
        RemoveKthNodeFromEnd.removeKthNodeFromEnd(l2, 2);
        assertEquals(List.of(2), LinkedListNode.toList(l2));
        var l3 = LinkedListNode.of(1, 2, 3);
        RemoveKthNodeFromEnd.removeKthNodeFromEnd(l3, 1);
        assertEquals(List.of(1, 2), LinkedListNode.toList(l3));
    }

    @Test void sumOfLinkedLists() {
        assertEquals(List.of(1, 9, 2, 2), LinkedListNode.toList(SumOfLinkedLists.sumOfLinkedLists(LinkedListNode.of(2, 4, 7, 1), LinkedListNode.of(9, 4, 5))));
        assertEquals(List.of(0, 1), LinkedListNode.toList(SumOfLinkedLists.sumOfLinkedLists(LinkedListNode.of(5), LinkedListNode.of(5))));
        assertEquals(List.of(0), LinkedListNode.toList(SumOfLinkedLists.sumOfLinkedLists(LinkedListNode.of(0), LinkedListNode.of(0))));
    }

    @Test void mergingLinkedLists() {
        var shared = LinkedListNode.of(7, 8);
        var x = LinkedListNode.of(1, 2); x.next.next = shared;
        var y = LinkedListNode.of(5); y.next = shared;
        assertSame(shared, MergingLinkedLists.mergingLinkedLists(x, y));
        assertNull(MergingLinkedLists.mergingLinkedLists(LinkedListNode.of(1), LinkedListNode.of(2)));
        assertSame(shared, MergingLinkedLists.mergingLinkedLists(shared, shared));
    }

    // ---------- Recursion ----------
    @Test void permutations() {
        assertEquals(6, Permutations.getPermutations(List.of(1, 2, 3)).size());
        assertEquals(6, new HashSet<>(Permutations.getPermutations(List.of(1, 2, 3))).size());
        assertTrue(Permutations.getPermutations(List.of()).isEmpty());
        assertEquals(List.of(List.of(4)), Permutations.getPermutations(List.of(4)));
    }

    @Test void powerset() {
        assertEquals(8, Powerset.powerset(List.of(1, 2, 3)).size());
        assertEquals(List.of(List.of()), Powerset.powerset(List.of()));
        assertEquals(List.of(List.of(), List.of(-1)), Powerset.powerset(List.of(-1)));
    }

    @Test void phoneNumberMnemonics() {
        assertEquals(List.of("1a", "1b", "1c"), PhoneNumberMnemonics.phoneNumberMnemonics("12"));
        assertEquals(12, PhoneNumberMnemonics.phoneNumberMnemonics("1905").size());
        assertEquals(List.of("0"), PhoneNumberMnemonics.phoneNumberMnemonics("0"));
        assertEquals(16, PhoneNumberMnemonics.phoneNumberMnemonics("99").size());
    }

    @Test void staircaseTraversal() {
        assertEquals(5, StaircaseTraversal.staircaseTraversal(4, 2));
        assertEquals(1, StaircaseTraversal.staircaseTraversal(0, 3));
        assertEquals(1, StaircaseTraversal.staircaseTraversal(5, 1));
        assertEquals(8, StaircaseTraversal.staircaseTraversal(4, 4));
    }

    @Test void blackjackProbability() {
        assertEquals(0.45f, BlackjackProbability.blackjackProbability(21, 15), 1e-6);
        assertEquals(0f, BlackjackProbability.blackjackProbability(21, 21), 1e-6);
        assertEquals(1f, BlackjackProbability.blackjackProbability(21, 22), 1e-6);
        assertEquals(0f, BlackjackProbability.blackjackProbability(21, 17), 1e-6, "dealer stands at target-4");
    }

    @Test void revealMinesweeper() {
        String[][] board = {{"H", "H", "H"}, {"H", "H", "M"}, {"H", "H", "H"}};
        RevealMinesweeper.revealMinesweeper(board, 0, 0);
        assertArrayEquals(new String[][]{{"0", "1", "H"}, {"0", "1", "M"}, {"0", "1", "H"}}, board);
        assertEquals("X", RevealMinesweeper.revealMinesweeper(new String[][]{{"M"}}, 0, 0)[0][0]);
        assertEquals("0", RevealMinesweeper.revealMinesweeper(new String[][]{{"H"}}, 0, 0)[0][0]);
        String[][] b2 = {{"H", "M"}};
        assertArrayEquals(new String[][]{{"1", "M"}}, RevealMinesweeper.revealMinesweeper(b2, 0, 0));
    }

    // ---------- Searching / Sorting ----------
    @Test void searchInSortedMatrix() {
        int[][] m = {{1, 4, 7, 12, 15, 1000}, {2, 5, 19, 31, 32, 1001}, {3, 8, 24, 33, 35, 1002}, {40, 41, 42, 44, 45, 1003}, {99, 100, 103, 106, 128, 1004}};
        assertArrayEquals(new int[]{3, 3}, SearchInSortedMatrix.searchInSortedMatrix(m, 44));
        assertArrayEquals(new int[]{-1, -1}, SearchInSortedMatrix.searchInSortedMatrix(m, 43));
        assertArrayEquals(new int[]{0, 0}, SearchInSortedMatrix.searchInSortedMatrix(new int[][]{{-3}}, -3));
    }

    @Test void threeNumberSort() {
        assertArrayEquals(new int[]{0, 0, -1, -1, -1, 1, 1}, ThreeNumberSort.threeNumberSort(new int[]{1, 0, -1, 0, -1, 1, -1}, new int[]{0, -1, 1}));
        assertArrayEquals(new int[]{}, ThreeNumberSort.threeNumberSort(new int[]{}, new int[]{0, 1, 2}));
        assertArrayEquals(new int[]{2, 2}, ThreeNumberSort.threeNumberSort(new int[]{2, 2}, new int[]{0, 1, 2}), "only one value present");
    }

    // ---------- Stacks ----------
    @Test void balancedBrackets() {
        assertTrue(BalancedBrackets.balancedBrackets("([])(){}(())()()"));
        assertFalse(BalancedBrackets.balancedBrackets("(]"));
        assertTrue(BalancedBrackets.balancedBrackets(""));
        assertFalse(BalancedBrackets.balancedBrackets("(("));
        assertTrue(BalancedBrackets.balancedBrackets("(a)[b]"), "non-bracket characters ignored");
    }

    @Test void sunsetViews() {
        assertEquals(List.of(1, 3, 6, 7), SunsetViews.sunsetViews(new int[]{3, 5, 4, 4, 3, 1, 3, 2}, "EAST"));
        assertEquals(List.of(0, 1), SunsetViews.sunsetViews(new int[]{3, 5, 4, 4, 3, 1, 3, 2}, "WEST"));
        assertEquals(List.of(), SunsetViews.sunsetViews(new int[]{}, "EAST"));
        assertEquals(List.of(1), SunsetViews.sunsetViews(new int[]{2, 2}, "EAST"), "equal height blocks view");
    }

    @Test void bestDigits() {
        assertEquals("772", BestDigits.bestDigits("1772", 1));
        assertEquals("6839", BestDigits.bestDigits("462839", 2));
        assertEquals("", BestDigits.bestDigits("5", 1));
        assertEquals("33", BestDigits.bestDigits("333", 1));
    }

    @Test void sortStack() {
        assertEquals(List.of(-5, -2, -1, 2, 3, 4), SortStack.sortStack(new ArrayList<>(List.of(-5, 2, -2, 4, 3, -1))));
        assertEquals(List.of(), SortStack.sortStack(new ArrayList<>()));
        assertEquals(List.of(1, 1, 2), SortStack.sortStack(new ArrayList<>(List.of(1, 2, 1))));
    }

    @Test void nextGreaterElement() {
        assertArrayEquals(new int[]{5, 6, 6, 6, 7, -1, 5}, NextGreaterElement.nextGreaterElement(new int[]{2, 5, -3, -4, 6, 7, 2}));
        assertArrayEquals(new int[]{}, NextGreaterElement.nextGreaterElement(new int[]{}));
        assertArrayEquals(new int[]{-1, -1}, NextGreaterElement.nextGreaterElement(new int[]{3, 3}));
    }

    @Test void minMaxStackConstruction() {
        var s = new MinMaxStackConstruction.MinMaxStack();
        s.push(5); s.push(7); s.push(2);
        assertEquals(2, s.getMin()); assertEquals(7, s.getMax());
        assertEquals(2, s.pop());
        assertEquals(5, s.getMin()); assertEquals(7, s.peek());
        s.push(7);
        s.pop();
        assertEquals(7, s.getMax(), "duplicate max survives one pop");
    }

    @Test void reversePolishNotation() {
        assertEquals(2, ReversePolishNotation.reversePolishNotation(new String[]{"50", "3", "17", "+", "2", "-", "/"}));
        assertEquals(-1, ReversePolishNotation.reversePolishNotation(new String[]{"2", "3", "-"}));
        assertEquals(42, ReversePolishNotation.reversePolishNotation(new String[]{"42"}));
        assertEquals(-2, ReversePolishNotation.reversePolishNotation(new String[]{"-7", "3", "/"}), "truncates toward zero");
    }

    @Test void collidingAsteroids() {
        assertArrayEquals(new int[]{-3, -8, 6}, CollidingAsteroids.collidingAsteroids(new int[]{-3, 5, -8, 6, 7, -4, -7}));
        assertArrayEquals(new int[]{}, CollidingAsteroids.collidingAsteroids(new int[]{5, -5}));
        assertArrayEquals(new int[]{}, CollidingAsteroids.collidingAsteroids(new int[]{}));
        assertArrayEquals(new int[]{-1, 1}, CollidingAsteroids.collidingAsteroids(new int[]{-1, 1}), "moving apart never collide");
    }

    // ---------- Strings / Tries ----------
    @Test void longestPalindromicSubstring() {
        assertEquals("xyzzyx", LongestPalindromicSubstring.longestPalindromicSubstring("abaxyzzyxf"));
        assertEquals("a", LongestPalindromicSubstring.longestPalindromicSubstring("a"));
        assertEquals("", LongestPalindromicSubstring.longestPalindromicSubstring(""));
        assertEquals("aaaa", LongestPalindromicSubstring.longestPalindromicSubstring("aaaa"));
    }

    @Test void groupAnagrams() {
        var g = GroupAnagrams.groupAnagrams(List.of("yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"));
        assertEquals(4, g.size());
        assertEquals(List.of("act", "tac", "cat"), g.get(1));
        assertEquals(List.of(), GroupAnagrams.groupAnagrams(List.of()));
        assertEquals(List.of(List.of("a", "a")), GroupAnagrams.groupAnagrams(List.of("a", "a")));
    }

    @Test void validIpAddresses() {
        var ips = ValidIpAddresses.validIPAddresses("1921680");
        assertEquals(11, ips.size());
        assertTrue(ips.contains("19.216.8.0"));
        assertEquals(List.of("0.0.0.0"), ValidIpAddresses.validIPAddresses("0000"));
        assertEquals(List.of(), ValidIpAddresses.validIPAddresses("123"));
        assertEquals(List.of(), ValidIpAddresses.validIPAddresses("1234567890123"));
    }

    @Test void reverseWordsInString() {
        assertEquals("best! the is AlgoExpert", ReverseWordsInString.reverseWordsInString("AlgoExpert is the best!"));
        assertEquals("b  a ", ReverseWordsInString.reverseWordsInString(" a  b"));
        assertEquals("", ReverseWordsInString.reverseWordsInString(""));
        assertEquals("word", ReverseWordsInString.reverseWordsInString("word"));
    }

    @Test void minimumCharactersForWords() {
        char[] mc = MinimumCharactersForWords.minimumCharactersForWords(new String[]{"this", "that", "did", "deed", "them!", "a"});
        assertEquals(12, mc.length);
        assertArrayEquals(new char[]{}, MinimumCharactersForWords.minimumCharactersForWords(new String[]{}));
        assertArrayEquals(new char[]{'a', 'a', 'b'}, MinimumCharactersForWords.minimumCharactersForWords(new String[]{"aa", "ab"}));
    }

    @Test void oneEdit() {
        assertTrue(OneEdit.oneEdit("hello", "helo"));
        assertTrue(OneEdit.oneEdit("abc", "abd"));
        assertFalse(OneEdit.oneEdit("abc", "acd"));
        assertTrue(OneEdit.oneEdit("", "a"));
        assertTrue(OneEdit.oneEdit("same", "same"));
        assertFalse(OneEdit.oneEdit("a", "abc"));
    }

    @Test void suffixTrieConstruction() {
        var trie = new SuffixTrieConstruction.SuffixTrie("babc");
        assertTrue(trie.contains("abc"));
        assertTrue(trie.contains("babc"));
        assertFalse(trie.contains("ab"), "not a suffix");
        assertTrue(new SuffixTrieConstruction.SuffixTrie("aa").contains("a"));
    }
}
