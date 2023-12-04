import qualified Data.Set as Set

type Pad = (Set.Set Int, Set.Set Int)
process :: String -> Pad 
process line =
    let card = drop 2 ( words line )
    in (
        Set.fromList (map read (takeWhile ( /= "|" ) card)),
        Set.fromList (map read (drop 1 (dropWhile ( /= "|" ) card)))
    )

score :: Int -> Int
score n = if n > 0 then 2 ^ (n-1) else 0


incr :: [Int] -> Int -> Int -> [Int]
incr a 0 x = a
incr (a:as) n x = (a + x) : (incr as (n - 1) x )


part2 :: Int -> [Int] -> [Int] -> Int
part2 result [] [] = result
part2 result (s:scored) (c:counts) = 
    part2 (result + s * c + 1) scored (incr counts s c)
    

main :: IO ()
main = do
    contents <- getContents
    let pads = map process (lines contents)
        processed = map (length . uncurry Set.intersection) pads
    
    -- part 1 
    putStrLn (show (sum (map score processed)))

    -- part 2
    putStrLn (show (part2 0 processed (replicate (length processed) 1)))

