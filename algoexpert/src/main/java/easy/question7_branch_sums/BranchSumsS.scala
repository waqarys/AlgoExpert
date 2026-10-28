package easy.question7_branch_sums

case class BinaryTree(value: Int, left: BinaryTree, right: BinaryTree)

//TODO - In-progress
object BranchSumsS extends App{
  def branchSums(root: BinaryTree): List[Int] = {
    def calculateBranchSums(node: BinaryTree, runningSum: Int, sums: List[Int]): List[Int] = {
      if(node == null) List()
      else {
        if(node.left == null && node.right == null) sums.::(runningSum + node.value)
        else{
          val newRunningSum = runningSum + node.value
          calculateBranchSums(node.left, newRunningSum, sums)
          calculateBranchSums(node.right, newRunningSum, sums)
        }
      }
    }
    calculateBranchSums(root, 0, List[Int]())
  }

  val root: BinaryTree = BinaryTree(2, BinaryTree(1, null, null), BinaryTree(3, null, null))
  println(branchSums(root))
}
