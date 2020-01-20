package src

import "github.com/go-redis/redis/v7"
import "strconv"

func RediSetFileState(state *FileState){
	client := redis.NewClient(&redis.Options{
		Addr:     "0.0.0.0:6379",
		Password: "",
		DB:       0,
	})
	
	client.HMSet(state.StateId,
		"file", state.FileId,
		"user", state.UserId,
		"expire", state.ExpireTime)
}

func RediGetFileState(key string) FileState{
	client := redis.NewClient(&redis.Options{
		Addr:     "0.0.0.0:6379",
		Password: "",
		DB:       0,
	})

	resp := client.HGetAll(key).Val()

	expire, _ := strconv.ParseInt(resp["expire"], 10, 64)
	state := FileState{
		StateId : key,
		ExpireTime: expire,
		FileId: resp["file"],
		UserId: resp["user"],
	}

	return state
}


