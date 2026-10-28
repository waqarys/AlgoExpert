package datastructures

sealed trait BinaryTree[+A]
case object Leaf extends BinaryTree[Nothing]
case class Branch[A](value: A, left: BinaryTree[A], right: BinaryTree[A]) extends BinaryTree[A]

object BinaryTreeApp {
  def main(args: Array[String]): Unit = {
    val myList = List(1,2,3,4,5,6)
    val myBinTree = createTree(myList)
    println(myBinTree)
    println(size(myBinTree))
    println(depth(myBinTree))
  }

  def createTree[A](list: List[A]): BinaryTree[A] =
    list match {
      case Nil => Leaf
      case x :: xs => {
        val halfLength = xs.length / 2
        Branch(x, createTree(xs.take(halfLength)), createTree(xs.drop(halfLength)))
      }
    }

  def size[A](binTree: BinaryTree[A]): Int = binTree match {
    case Leaf => 0
    case Branch(_, leftBranch, rightBranch) => 1 + size(leftBranch) + size(rightBranch)
  }

  def depth[A](binTree: BinaryTree[Int]): Int = binTree match {
    case Leaf => 0
    case Branch(_, leftBranch, rightBranch) => 1 + (depth(leftBranch) max depth(rightBranch))
  }
}
