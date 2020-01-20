package main

import (
	"eFes/src"
	"eFes/src/endpoints"
	"fmt"
	"github.com/gin-gonic/gin"
)

const (
	SERVE_ADDRESS = "0.0.0.0:6565"
)

func hello(c *gin.Context) {
	c.JSON(200, gin.H{"message": "Welcome to eFeS"})
}


func main() {
	gin.SetMode(gin.ReleaseMode)
	fmt.Println(src.GetAllFiles())
	fmt.Println(src.CreateBlock("1"))
	fmt.Println(src.CreateBlock("2"))
	fmt.Println(src.CreateBlock("3"))
	

	router := gin.Default()

	router.PUT("/upload/:state", endpoints.UploadFile)
	router.GET("/", hello)
	router.GET("/version", endpoints.GetApiVersion)
	router.GET("/file/:user/:file", endpoints.ServeFile)
	router.POST("/psu", endpoints.PreSignedUrl)
	
	router.Run(SERVE_ADDRESS)
}
