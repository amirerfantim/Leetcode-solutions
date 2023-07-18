import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution36 {
    public static boolean isValidSudoku(char[][] board) {
        for (int row = 0; row < 9; row++){
            Set<Character> set = new HashSet<>();
            for (int col = 0; col < 9; col++){
                if (board[row][col] != '.' && set.contains(board[row][col])){
                    System.out.println("x1");
                    return false;
                }
                set.add(board[row][col]);
            }
        }
        for (int col = 0; col < 9; col++){
            Set<Character> set = new HashSet<>();
            for (int row = 0; row < 9; row++){
                if (board[row][col] != '.' && set.contains(board[row][col])){
                    System.out.println("x2");
                    return false;
                }
                set.add(board[row][col]);
            }
        }
        for (int v_square = 0; v_square < 3; v_square++){
            for (int h_square = 0; h_square < 3; h_square++){
                Set<Character> set = new HashSet<>();
                for (int row = 0; row < 3; row++){
                    for (int col = 0; col < 3; col++){
                        if (board[row +  3 * h_square][col +  3 * v_square] != '.'
                                && set.contains(board[row +  3 * h_square][col + 3 * v_square])){
                            System.out.println("x3");
                            return false;
                        }
                        set.add(board[row + 3 * h_square][col + 3 * v_square]);
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        char[][] board = {
                {'5','3','.','.','7','.','.','.','.'},
                {'6','.','.','1','9','5','.','.','.'},
                {'.','9','8','.','.','.','.','6','.'},
                {'8','.','.','.','6','.','.','.','3'},
                {'4','.','.','8','.','3','.','.','1'},
                {'7','.','.','.','2','.','.','.','6'},
                {'.','6','.','.','.','.','2','8','.'},
                {'.','.','.','4','1','9','.','.','5'},
                {'.','.','.','.','8','.','.','7','9'}
        };
        System.out.println(isValidSudoku(board));
    }
}