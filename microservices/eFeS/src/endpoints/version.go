// Date: 19.11.2019 - 17.58
// Author: Berkay Dedeoğlu

package endpoints

import (
	"github.com/gin-gonic/gin"
)

const API_VERSION string = "0.1" 

func GetApiVersion(context *gin.Context) {
	context.JSON(200, gin.H{"Version" : API_VERSION})
}

