package grep

import (
	"bytes"
	"os"
	"os/exec"
)


func ExecCmd(s string, src, dst string) (string, error) {


	cmd := &exec.Cmd{
		Path: s,
		Args: []string{s, src, dst},
		//Stdout: os.Stdout,
		Stdin: os.Stdin,
	}
	var out bytes.Buffer
	cmd.Stdout = &out

	if err := cmd.Run(); err != nil {
		return "", err
	}



	//cmd.Wait()


	return out.String(), nil

}
