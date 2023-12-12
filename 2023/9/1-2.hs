main :: IO ()
main = do
    contents <- getContents
    let l = map words (lines contents)
    let h = map (map read) l
    putStrLn ("Part 1: " ++ show (sum (map part h)))
    putStrLn ("Part 2: " ++ show (sum (map (part . reverse) h)))

pairwise :: [a] -> [(a,a)]
pairwise v = zip v (tail v)

diff :: [Int] -> [Int]
diff v = map (\(x,y) -> y-x) (pairwise v)

tails :: [Int] -> [Int]
tails v 
    | all (==0) v = [0]
    | otherwise = tails (diff v) ++ [last v]

part :: [Int] -> Int
part history = 
    let t = tails history 
    in last (scanl (+) 0 t)

