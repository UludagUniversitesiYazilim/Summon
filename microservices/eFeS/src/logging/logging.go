package logging

/**
 *
 **/

import (
	"fmt"
	"time"
)

//-- DEFAULTS --

var defaultTimeFormat = time.ANSIC

/**
 *
 **/
func General(category string, message string) {
	fmt.Printf("[G] -- [%s] ❱❱  %s => %s \n", getReadableNow(), category, message)
}

func Error(category string, message string) {
	fmt.Printf("[E] -- [%s] ❱❱  %s => %s \n", getReadableNow(), category, message)
}

func Info(category string, message string) {
	fmt.Printf("[I] -- [%s] ❱❱  %s => %s \n", getReadableNow(), category, message)
}

/**
 *
 **/
func getReadableNow() string { return time.Now().Format(defaultTimeFormat) }

/**
 *
 **/
func SetDefaultTimeFormat(format string) { defaultTimeFormat = format }
