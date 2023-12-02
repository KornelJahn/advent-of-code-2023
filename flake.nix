{
  description = "Advent of Code 2023 Python solutions flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    poetry2nix.url = "github:nix-community/poetry2nix";
    poetry2nix.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { nixpkgs, poetry2nix, ... }:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs {
      inherit system;
      overlays = builtins.attrValues poetry2nix.overlays;
    };
  in
  {
    devShells.${system}.default = import ./shell.nix { inherit pkgs; };
  };
}
