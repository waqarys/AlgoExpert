package easy.question1

object TwoNumbers extends App {

  def twoNums(nums: List[Int], target: Int): List[Int] =
    nums.combinations(2).find(_.sum == target).get.map(nums.indexOf)

  def twoSum1(nums: List[Int], target: Int): List[List[Int]] =
    nums.combinations(2).collect {
      case couple if couple.sum == target =>
        couple.map(nums.indexOf)
    }.toList

  def twoNums2(nums: List[Int], target: Int): List[Int] =
    nums.combinations(2).filter{case List(x, y) => x + y == target}.next.map(nums.zipWithIndex.toMap)

  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    import scala.collection.immutable.HashMap
    def run(index: Int, map: HashMap[Int, Int]): Array[Int] = {
      val value = nums(index)
      map get (target - value) match {
        case Some(foundInd) => Array(foundInd, index)
        case None => run(index + 1, map + (value -> index))
      }
    }
    run(0, HashMap())
  }

  println(twoNums(List(3, 5, -4, 8, 11, 1, -1, 6), 10))
  twoSum(Array(3, 5, -4, 8, 11, 1, -1, 6), 10).foreach(println)
  println(twoSum1(List(3, 5, -4, 8, 11, 1, -1, 6), 10))
  println(twoNums2(List(3, 5, -4, 8, 11, 1, -1, 6), 10))
}
