package main

import (
	"log"
)

func exist(board [][]byte, word string) bool {
	selected := make([][]int, len(board))
	for i := 0; i < len(board); i++ {
		selected[i] = make([]int, len(board[0]))
	}
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if board[i][j] != word[0] {
				continue
			}
			if search(i, j, board, selected, word) {
				return true
			}
		}
	}
	return false
}

func search(i, j int, board [][]byte, selected [][]int, word string) bool {
	if board[i][j] != word[0] {
		selected[i][j] = 0
		return false
	}

	selected[i][j] = 1
	if len(word) == 1 {
		return true
	}
	if i+1 < len(board) && selected[i+1][j] == 0 && search(i+1, j, board, selected, word[1:]) {
		return true
	}
	if i-1 >= 0 && selected[i-1][j] == 0 && search(i-1, j, board, selected, word[1:]) {
		return true
	}
	if j+1 < len(board[0]) && selected[i][j+1] == 0 && search(i, j+1, board, selected, word[1:]) {
		return true
	}
	if j-1 >= 0 && selected[i][j-1] == 0 && search(i, j-1, board, selected, word[1:]) {
		return true
	}
	selected[i][j] = 0
	return false
}

func main() {
	cases := []struct {
		board [][]byte
		word  string
		res   bool
	}{
		{
			board: [][]byte{
				{'A', 'B', 'C', 'E'},
				{'S', 'F', 'E', 'S'},
				{'A', 'D', 'E', 'E'},
			},
			word: "ABCESEEEFS",
			res:  true,
		},
		{
			board: [][]byte{
				{'A', 'B', 'C', 'E'},
				{'S', 'F', 'C', 'S'},
				{'A', 'D', 'E', 'E'},
			},
			word: "ABCCED",
			res:  true,
		},
		{
			board: [][]byte{
				{'A', 'B', 'C', 'E'},
				{'S', 'F', 'C', 'S'},
				{'A', 'D', 'E', 'E'},
			},
			word: "SEE",
			res:  true,
		},
		{
			board: [][]byte{
				{'A', 'B', 'C', 'E'},
				{'S', 'F', 'C', 'S'},
				{'A', 'D', 'E', 'E'},
			},
			word: "ABCB",
			res:  false,
		},
		{
			board: [][]byte{
				{'A', 'A', 'A', 'A', 'A', 'A'},
				{'A', 'A', 'A', 'A', 'A', 'A'},
				{'A', 'A', 'A', 'A', 'A', 'A'},
				{'A', 'A', 'A', 'A', 'A', 'A'},
				{'A', 'A', 'A', 'A', 'A', 'B'},
				{'A', 'A', 'A', 'A', 'B', 'A'},
			},
			word: "AAAAAAAAAAAAABB",
			res:  false,
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := exist(c.board, c.word); res != c.res {
			log.Fatalf("expect: %+v, got: %+v", c.res, res)
		}
	}
}
