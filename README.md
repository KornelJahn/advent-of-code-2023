# Advent of Code 2023

My Python solutions to [Advent of Code 2023](https://adventofcode.com/2023)
puzzles.

After cloning this repo, to enter a development shell to edit the package and
run tests, execute
```sh
cd advent-of-code-2023
nix develop --experimental-features 'nix-command flakes' .#
```
and then `pytest` in the subshell.

To run the tests only without manual cloning:
```sh
nix develop --experimental-features 'nix-command flakes' github:KornelJahn/advent-of-code-2023 --command pytest
```
