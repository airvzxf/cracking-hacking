# CTF: Beginner

## [osandamalith](./osandamalith/)

It is a quick tutorial to understand the logic behind a password validation, the author talk in general bout the **Linux Reverse Engineering**.

Interesting discoveries:

- **Reverse Debugging:** Needs to create a start breakpoint and a finish breakpoint, maybe it could be a function or piece of code. GDB has the instruction `commands` to execute commands when it hits the breakpoints. We start with the `record` and `continue` after these we will put a command in the final breakpoint with `end`. It causes that the program stop in the last breakpoint then execute manually the `reverse-nexti` to go back.
- The [run.sh](./osandamalith/run.sh) script contains the examples of the apps and options to get additional information about the target application, refers from the [web tutorial](https://osandamalith.com/2019/02/11/linux-reverse-engineering-ctfs-for-beginners/).
