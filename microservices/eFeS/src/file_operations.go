// Date: 02.11.2019
// Author: Berkay Dedeoğlu

package src

import (
	"fmt"
	"os"
	"path/filepath"
	"errors"
)

const ROOT_DIR = "./DATABLOCKS/"

func GetAllFiles() []string {
	files, err := filepath.Glob(ROOT_DIR + "*")

	if err != nil {
		fmt.Println("Hata meydana geldi")
		return nil
	}

	return files
}

func CreateBlock(id string) bool {
	err := os.Mkdir(ROOT_DIR+id, 0700)

	if err != nil {
		fmt.Println("There is already a block named: ", id, err)
		return false
	}
	return true
}

func GetFilePath(user_id string, file_id string) (string, error) {
	path := ROOT_DIR + user_id + "/" + file_id

	if _, err := os.Stat(path); os.IsNotExist(err) {
		return "Error Occured", errors.New("File Not Exist")
	}
	return path, nil
}
