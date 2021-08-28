package main

import (
	"github.com/adamszpilewicz/go-grep/cmds/grep"
	"log"
	"os"
)

func main() {
	s := "./scripts/grep.sh"

	//if len(os.Args)==1 {
	//	log.Println("no arguments provided")
	//	return
	//}

	arg1 := os.Args[1]
	arg2 := os.Args[2]

	//arg1 := "look.txt"
	//arg2 := "main"

	res, err := grep.ExecCmd(s, arg1, arg2)
	if err != nil {
		log.Println(err)
		return
	}

	f, err := os.Create("./found.csv")
	if err != nil {
		log.Fatal(err)
	}
	f.Write([]byte(res))





}
