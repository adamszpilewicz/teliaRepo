package line

import (
	"bufio"
	"os"
	"strings"
)

type Finder struct {
	File *os.File
	MappedFile map[int]string
}

func New(file *os.File) *Finder {
	finder :=  &Finder{
		File: file,
	}
	finder.MappedFile = finder.ReadLines()
	return finder
}

func (f *Finder) ReadLines() map[int]string {
	defer f.File.Close()
	var mapLines = make(map[int]string)
	var counter int = 0

	scanner := bufio.NewScanner(f.File)
	for scanner.Scan() {
		mapLines[counter] = scanner.Text()
		counter++
	}
	return mapLines
}

func (f *Finder) FilterLines(substr string) map[int]string {
	var filteredMap = make(map[int]string)

	for k, v := range f.MappedFile {
		if strings.Contains(v, substr) {
			filteredMap[k] = v
		}
	}

	return filteredMap

}



