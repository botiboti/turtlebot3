with import <nixpkgs> { };
let
  pythonEnv = python3.withPackages (ps: [
    ps.matplotlib
    ps.numpy
  ]);
in
mkShell {
  buildInputs = [
    pythonEnv
  ];
}
