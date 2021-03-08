package easy.question6_sorted_square_array

object SortedSquareArray extends App {

  def sortedSquares(nums: Array[Int]): Array[Int] = {
    val (negNums, posNums) = nums.span(_ < 0)
    merge(negNums.reverse.map(x => x*x), posNums.map(x => x*x))
  }

  def merge(l1: Array[Int], l2: Array[Int]): Array[Int] = (l1, l2) match {
    case (Array(), Array()) => Array()
    case (Array(), _) => l2
    case (_, Array()) => l1
    case (Array(x, _*), Array(y, _*)) =>
      if(x<y) x+: merge(l1.tail, l2) else y +: merge(l1, l2.tail)
  }

  println(sortedSquares(Array(-9, -3, -1, 2, 4, 5)).mkString(", "))
}
