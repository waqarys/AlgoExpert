package easy.question8_node_depts

case class TreeNode(value: Int, left: TreeNode, right: TreeNode)
//Max Depth
object MaxTreeDepth extends App {

  def maxDepth(root: TreeNode): Int = {
    if(root == null) return 0
    1 + scala.math.max(maxDepth(root.left), maxDepth(root.right))
  }

  val root = TreeNode(1,
    TreeNode(2, null, null),
    TreeNode(3, TreeNode(4, null, null), TreeNode(5, null, null))
  )
  println(maxDepth(root))
}
