package endpoints

import (
	"github.com/gin-gonic/gin"
	"eFes/src"
	"time"
	"fmt"
)


func UploadFile(context *gin.Context) {
	state_id := context.Param("state")

	state := src.RediGetFileState(state_id)

	now := time.Now().Unix()
	
	if (now > state.ExpireTime){
		fmt.Println("%d, %d", now, state.ExpireTime) 
		context.String(204, "")
		return
	}
	
	user := state.UserId

	//file := state.FileId

	formfile, err := context.FormFile("file")

	if (err != nil){
		context.String(502, "")
		fmt.Println(err.Error())
		return
	}
	
	err = context.SaveUploadedFile(formfile, user)

	if err != nil {
		fmt.Println(err.Error())
		context.String(502, "")
	}

	
	context.String(200, "")
}

func PreSignedUrl(context *gin.Context) {
	user := context.PostForm("user")
	file := context.PostForm("file")

	state := src.CreateState(file, user)
	
	src.RediSetFileState(&state)
	
	context.String(200, generatePresignedUrl(state.StateId))
}

func generatePresignedUrl(state_id string) string {
	return state_id
}
