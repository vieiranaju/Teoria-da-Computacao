quickSort :: (Ord a) => [a] -> [a]
quickSort [] = []
quickSort (pivo:resto) =
  let menores = [x | x <- resto, x <= pivo]
      maiores = [x | x <- resto, x > pivo]
  in quickSort menores ++ [pivo] ++ quickSort maiores

main :: IO ()
main = do
  let vetor = [25, 40, 55, 20, 44, 35, 38, 99, 10, 65, 50]
  print (quickSort vetor)
