package endpoints

import "github.com/gin-gonic/gin"
import "eFes/src"



func ServeFile(context *gin.Context) {
	user_id := context.Param("user")
	file_id := context.Param("file")

	var path, err= src.GetFilePath(user_id, file_id)

	if (err != nil) { context.String(404, "File does not exist \n\n")}
	
	context.FileAttachment(path, "duzelecek")
}
