package src

import (
	"os/exec"
	"time"
	"strings"
	"fmt"
)

const EXPIRE = 85 //seconds

type FileState struct {
	StateId string

	ExpireTime int64
	FileId string
	UserId string
}

func CreateState(file string, user string) FileState {
	state := FileState{}

	state.StateId = create_uuid()

	state.FileId = file
	state.UserId = user
	state.ExpireTime = generate_expire_time()

	return state
}


func create_uuid() (string) {
	uuid, err := exec.Command("uuidgen").Output()

	if (err != nil) {
		return "" 
	}

	uuids := string(uuid)
	uuids = strings.TrimSpace(uuids)
	
	return uuids
}


func generate_expire_time() int64 {
	now := time.Now()
	fmt.Println("olu", now)
	now = now.Add(time.Second * EXPIRE)
	fmt.Println("olu", now)
	
	return now.Unix()
}
