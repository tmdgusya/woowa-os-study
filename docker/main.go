package main

import (
	"bytes"
	"log"
	"os/exec"
)

func main() {
	log.Print("====================================")
	buildWoowaOs()
	log.Print("====================================")
	printInstalledImage()
	log.Print("====================================")
	runWoowaOS()
	log.Print("====================================")
	printExecutedContainer()
	log.Print("====================================")
	log.Print("====================================")
	log.Print("====================================")
}

func printExecutedContainer() {
	dockerImages := exec.Command("/bin/sh", "-c", "docker container ls")
	filter := exec.Command("grep", "woowa/os")
	woowaOs := grep(dockerImages, filter)
	log.Print("currently executed woowa/os container is : ", string(woowaOs))
}

func printInstalledImage() {
	dockerImages := exec.Command("/bin/sh", "-c", "docker image ls")
	filter := exec.Command("grep", "woowa/os")
	woowaOs := grep(dockerImages, filter)
	log.Print("woowa/os image : ", string(woowaOs))
}

func buildWoowaOs() {
	log.Print("build docker image....")
	dockerBuildCmd := exec.Command("/bin/sh", "-c", "docker build -t woowa/os - < Dockerfile")
	output := executeShell(dockerBuildCmd)
	log.Printf("Dockerfile is built successfully %s\n", string(output))
}

func runWoowaOS() {
	log.Print("run docker image with some arguments")
	executeCmd := exec.Command("/bin/sh", "-c", "docker run -dit woowa/os")
	output := executeShell(executeCmd)
	log.Printf("docker run sucessfully %s", string(output))
}

func executeShell(cmd *exec.Cmd) []byte {
	output, err := cmd.CombinedOutput()

	if err != nil {
		log.Fatal(err)
	}

	return output
}

func grep(before *exec.Cmd, filter *exec.Cmd) []byte {
	beforeStdout, err := before.StdoutPipe()
	var buf bytes.Buffer
	filter.Stdout = &buf
	filter.Stdin = beforeStdout

	if err != nil {
		log.Fatal("where is log - 1", err)
	}

	if err := filter.Start(); err != nil {
		log.Fatal("where is log - 2", err)
	}

	if err := before.Run(); err != nil {
		log.Fatal("where is log - 3", err)
	}

	if err := filter.Wait(); err != nil {
		log.Fatal("where is log - 4", err)
	}

	return buf.Bytes()
}
