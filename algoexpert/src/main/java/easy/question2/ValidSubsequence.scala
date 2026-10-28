package easy.question2

import scala.util.control.Breaks.break


object ValidSubsequenceS extends App {
  //ValidSubsequenceS().isValidSubsequence(List[Int](5, 1, 22, 25, 6, -1, 8, 10), List[Int](1, 6, -1, 10))

  println(ValidSubsequenceS().lcs(List[Int](5, 1, 22, 25, 6, -1, 8, 10), List[Int](1, 6, -1, 10)))
}

case class ValidSubsequenceS() {
  def isValidSubsequence(array: List[Int], sequence: List[Int]) = {
    var seqIdx = 0
    for(v <- array){
      if (seqIdx == sequence.length) break
      if(sequence(seqIdx) == v) seqIdx +=1
    }
    seqIdx == sequence.length
  }

  def lcs[T]: (List[T], List[T]) => List[T] = {
    case (_, Nil) => Nil
    case (Nil, _) => Nil
    case (x :: xs, y :: ys) if x == y => x :: lcs(xs, ys)
    case (x :: xs, y :: ys)           => {
      (lcs(x :: xs, ys), lcs(xs, y :: ys)) match {
        case (xs, ys) if xs.length > ys.length => xs
        case (xs, ys)                          => ys
      }
    }
  }
}
