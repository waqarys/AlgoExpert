package easy.quesstion3

object ClosestValueInBST extends App {

  def findClosestValueInBST(tree: BST, target: Int, closest: Int = 0): Int = tree match {

    case bst if(target < bst.value) =>
      if(Math.abs(target - closest) > Math.abs(target - tree.value)) findClosestValueInBST(tree.left, target, tree.value)
      else findClosestValueInBST(tree.left, target, closest)
    case bst if target > bst.value =>
      if(Math.abs(target - closest) > Math.abs(target - tree.value)) findClosestValueInBST(tree.right, target, tree.value)
      else findClosestValueInBST(tree.right, target, closest)
    case _ => closest
  }

}

case class BST(val value: Int, val left: BST, right: BST)