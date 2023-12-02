{ pkgs ? import <nixpkgs> {} }:

let
  myEnv = pkgs.poetry2nix.mkPoetryEnv {
    projectDir = ./.;
    python = pkgs.python311;
    editablePackageSources = {
      aoc2023 = ./src;
    };
  };
in
myEnv.env
