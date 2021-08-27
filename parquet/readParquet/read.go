package main

import (
	"encoding/json"
	"github.com/xitongsys/parquet-go-source/local"
	"github.com/xitongsys/parquet-go/reader"
	"log"
)

func main() {
	///read
	fr, err := local.NewLocalFileReader("../shoes.parquet")
	if err != nil {
		log.Println("Can't open file")
		return
	}

	pr, err := reader.NewParquetReader(fr, nil, 1)
	if err != nil {
		log.Println("Can't create parquet reader", err)
		return
	}

	num := int(pr.GetNumRows())
	log.Println(num)
	res, err := pr.ReadByNumber(num)
	if err != nil {
		log.Println("Can't read", err)
		return
	}

	jsonBs, err := json.Marshal(res)
	if err != nil {
		log.Println("Can't to json", err)
		return
	}

	log.Println(string(jsonBs))

	pr.ReadStop()
	fr.Close()

}