impl Solution {
    pub fn add_digits(num: i32) -> i32 {
        match (num, num % 9) {
            (0, _) => 0,
            (_, 0) => 9,
            (_, r) => r
        }
    }
}
